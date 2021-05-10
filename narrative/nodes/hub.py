from util.colors import ColorToColor
from util.variable.instances import characters, enemies
from util.variable.variables import locations

keywords = {
  "names": ("", "self", "__self__"),
}

def convert_name_to_global(name, prefix):
  """Returns the global version of name"""
  if name.startswith("this."): #Explicit local name
    name = prefix + name[5:] #Replace with global name
  elif '.' not in name:
    name = prefix + name
  return name

def remove_trailing_newline(text):
  return text[:-1] if (text!="" and text[-1]=='\n') else text
def clean_text(text, remove_trailing_newline=True):
  clean_text = ""
  is_comment = False
  for c in text:
    if c == '\n':
      clean_text += c if not is_comment else ""
      is_comment = False
    elif c == '#':
      is_comment = True
    else:
      clean_text += c if not is_comment else ""
  return clean_text[:-1] if (remove_trailing_newline and text!="" and text[-1]=='\n') else clean_text #Removing trailing newline is simple enough to write out

def section_strip(section):
  if len(section) <= 1:
    return section #Do nothing to it
  stripped_section = section.strip() #Uses builtin .strip() to remove whitespace at beginning and end
  start = 0
  if (stripped_section[0] == '!' and (stripped_section[1].isspace() or stripped_section[1] == '!')):
    start += 1 #Move start past the first character (exclamation mark)
  end = len(stripped_section)
  if (stripped_section[-1] == '!' and (stripped_section[-2].isspace() or stripped_section[-2] == '!')):
    end -= 1
  stripped_section = stripped_section[start:end]
  return stripped_section

def check_escape(section, variables, node_dict, prefix, has_braces=False):
  """Returns a string containing all error messages found (empty string if none found)"""
  split_section = text_to_split_section(section, ":", has_braces)
  err_text = ""
  if split_section[0] == "COLOR":
    if split_section[1] not in ColorToColor:
      err_text = "Unknown color: \"" + split_section[1] + "\""
  elif split_section[1] == "TIME":
    if not is_valid_float(split_section[1]):
      err_text = "Invalid value: \"" + split_section[1] + "\""
  elif split_section[0] == "ENTER" or split_section[0] == "RETURN_TO":
    global_node_name = convert_name_to_global(split_section[1], prefix)
    if global_node_name not in node_dict:
      err_text = "Unknown node name: \"" + global_node_name + "\""
  elif split_section[0] == "ADD_ITEM":
    errs = []
    item_args = text_to_split_section(split_section[1], ";")
    num_args = len(item_args)
    if num_args < 4:
      errs.append("Too few values for item creation")
    elif num_args > 4:
      errs.append("Too many values for item creation")
    if (num_args > 2) and (not is_valid_float(item_args[2])):
      errs.append("Invalid value: \"" + item_args[2] + "\"")
    if (num_args > 3) and (not is_valid_float(item_args[3])):
      errs.append("Invalid value: \"" + item_args[3] + "\"")
    err_text = ", ".join(errs)
  elif split_section[0] == "CHANGE":
    global_var_name = convert_name_to_global(split_section[1], prefix)
    found = value_in_dicts(variables, global_var_name)[1]
    if not found:
      err_text = "Unknown variable name: \"" + global_var_name + "\""
  elif split_section[0] == "CHARACTER":
    character_name = split_section[1]
    if character_name not in characters:
      err_text = "Unknown character name: \"" + character_name + "\""
  elif split_section[0] == "BATTLE":
    errs = []
    battle_args = text_to_split_section(split_section[1], ";")
    num_args = len(battle_args)
    if num_args < 5:
      errs.append("Too few values for battle")
    elif num_args > 6:
      errs.append("Too many values for battle")
    if num_args > 0:
      unknown_character_names = [character_name for character_name in text_to_split_section(battle_args[0], ",") if (character_name not in characters)]
      num_unknown = len(unknown_character_names)
      err = ("Unknown character names: " if num_unknown > 1 else "Unknown character name: ") + ", ".join(unknown_character_names)
      if num_unknown > 0:
        errs.append(err)
    if num_args > 1:
      unknown_enemy_names = [enemy_name for enemy_name in text_to_split_section(battle_args[1], ",") if enemy_name not in enemies]
      num_unknown = len(unknown_enemy_names)
      err = ("Unknown enemy names: " if num_unknown > 1 else "Unknown enemy name: ") + ", ".join(unknown_enemy_names)
      if num_unknown > 0:
        errs.append(err)
    if (num_args > 2) and (battle_args[2] not in locations):
      errs.append("Unknown location: \"" + battle_args[2] + "\"")
    if (num_args > 4) and (battle_args[4] not in enemies):
      errs.append("Unknown enemy name: \"" + battle_args[4] + "\"")
    err_text = ", ".join(errs)
  return err_text  

def split_with_escape(string_to_split, split_sequence,  split_sequence_mode=-1, escape_sequence="\\", strip=False):
  """split_sequence_mode: Negative means ignore split_sequence, 0 means include split_sequence at the end of each resulting word if present, and positive means include split_sequence as separate items in the final list.
  Unspecified behavior if split_sequence and escape_sequence have the same beginning."""
  split_list = []
  is_escape = False
  cur_escape = ""
  cur_split = ""
  cur_val = ""
  for c in string_to_split:
    if split_sequence == cur_split+c:
      if is_escape:
        cur_val += split_sequence
        is_escape = False
        cur_split = ""
      else:
        cur_val = section_strip(cur_val) if strip else cur_val
        split_list.append(cur_val)
        if split_sequence_mode == 0:
          split_list[-1] += split_sequence #Add split_sequence to the last string
        elif split_sequence_mode > 0:
          split_list.append(split_sequence) #Add split_sequence as another item to list
        cur_val = ""
        cur_split = ""
    elif split_sequence.startswith(cur_split+c):
      cur_split += c
    elif escape_sequence == cur_escape+c:
      if is_escape: #Repeated escape_sequence
        cur_val += escape_sequence
      is_escape = not is_escape #If is_escape was previously True, then this is repeated sequence and is_escape should be False. Otherwise, it should become True.
      cur_escape = ""
    elif escape_sequence.startswith(cur_escape+c):
      cur_escape += c
    else:
      cur_escape = escape_sequence if is_escape else cur_escape #If is_escape, cur_escape was erased- recover what it should be.
      cur_val += cur_split + cur_escape + c #c must be after cur_split and cur_escape, which store characters
      cur_split = ""
      cur_escape = ""
      is_escape = False
  if cur_val != "":
    cur_val = section_strip(cur_val) if strip else cur_val
    split_list.append(cur_val)
  return split_list

def text_to_split_section(section, splitter, has_braces=False):
  text_to_split = section[1:-1] if has_braces else section #Remove braces
  return split_with_escape(text_to_split, splitter, -1, "\\", True) #-1: Exclude splitter from result, "\\": Escape sequence, True: Strip each subsection
def split_section_to_text(split_section, splitter, include_braces=False):
  new_text = "{" if include_braces else ""
  for val in split_section:
    new_text += val + splitter
  new_text = new_text[:-len(splitter)] + ("}" if include_braces else "") #Remove last splitter, add right brace if needed
  return new_text

def value_in_dicts(dicts, key, new_value=None):
  """new_value==None indicates get, otherwise set.
  Returns a tuple (value, True) if key found in dicts, otherwise (None, False). If the call is used to set a value, the value returned is the new value."""
  is_set = new_value != None
  for dictionary in dicts:
    if key in dictionary:
      if is_set:
        dictionary[key] = new_value
      return dictionary[key], True
  #No dictionary with key found
  return None, False

def dict_with_key(dicts, key):
  """Returns the dictionary in dicts which has key."""
  for dictionary in dicts:
    if key in dictionary:
      return dictionary
  return None

def type_name(obj):
  return str(type(obj)).split("\'")[1]

def is_valid_float(string):
  stripped = string.strip()
  stripped = stripped[1:] if (stripped[0] == '+' or stripped[0] == '-') else stripped
  split = stripped.split('.')
  num_split = len(split)
  return (((num_split == 1) and (split[0].isdigit())) or
          ((num_split == 2) and (split[0].isdigit() and 
                (split[1].isdigit() or split[1]==""))))
    
