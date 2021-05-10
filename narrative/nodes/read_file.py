from util.colors import ColorToColor

from narrative.nodes.node import Node
from narrative.nodes.sections import generate_sections
from narrative.nodes.hub import keywords, clean_text, remove_trailing_newline, text_to_split_section, split_section_to_text, convert_name_to_global, check_escape

_cur_reading_files = []

#Traversing sections
def traverse_sections(outermost_section, section_func=None, args_for_func=tuple(), kwargs_for_func=dict(), include_outermost_in_ancestors=False):
  """Uses postorder traversal to traverse through every descendent of outermost_section, excluding outermost_section itself.

  Calls section_func at every section, passing in the section and its ancestors (including the section). If include_outermost_in_ancestors is True, the ancestors list will include outermost_section, otherwise not.
  
  Passes additional positional and keyword arguments to section_func."""
  call_func = section_func != None
  if not hasattr(outermost_section, "children"):
    raise TypeError("Expected outermost_section to have attribute children")
  if call_func and not callable(section_func):
    raise TypeError("Expected callable section_func")
  if type(args_for_func) != type(tuple()):
    raise TypeError("args_for_func must be a tuple")
  if type(kwargs_for_func) != type(dict()):
    raise TypeError("kwargs_for_func must be a dictionary")

  section_stack = list(reversed(outermost_section.children))
  all_ancestors = [outermost_section] #Currently unused
  children_remaining = [len(outermost_section.children)] #Keeps track of how many children are left for each ancestor in all_ancestors.
  call_ancestors = [outermost_section] if include_outermost_in_ancestors else [] #List of ancestors to pass into call

  while section_stack != []: #While sections in tree remain
    if children_remaining[-1] != 0: #Next child has untraversed siblings- First iteration
      #Get current section
      cur_section = section_stack[-1] #First iteration, leave section in stack ([-1] is like .peek())
      
      #Add children to stack
      section_stack += list(reversed(cur_section.children)) #Reversed so first child is last, which gets popped first
      
      #Add section to ancestor stacks for its descendents
      num_children = len(cur_section.children) #Only used once, doesn't save computation
      all_ancestors.append(cur_section)
      children_remaining.append(num_children)
      call_ancestors.append(cur_section)
    else: #Last iteration
      #Get current section
      cur_section = section_stack.pop() #Remove the section from stack
      
      if call_func:
        #Call function (with current section in ancestors)
        section_func(cur_section, call_ancestors, *args_for_func, **kwargs_for_func)
      
      #Remove section from ancestor stacks for its siblings
      all_ancestors.pop()
      children_remaining.pop()
      call_ancestors.pop()
      
      #Finished a child of the most recent ancestor
      children_remaining[-1] -= 1


#Section handling
def unknown_header(start_line_num, headers, index=-1):
  raise ValueError("Line " + str(start_line_num) + ": Unknown header \"" + headers[index] + "\"")

def set_prefix(instruction, start_line_num, settings): #Currently raises no errors, start_line_num passed just in case
  prefix = clean_text(instruction)
  prefix += "." if (prefix!="" and prefix[-1]!='.') else "" #Add a dot to non-empty strings without a dot at the end.
  settings["Prefix"] = prefix

def handle_settings(instruction, start_line_num, full_headers, header_index, settings, pass_num): #Currently does nothing with pass_num
  sub_headers = full_headers[header_index:]
  if sub_headers == []: #End of settings section
    pass
  elif sub_headers[0] == "PREFIX":
    if pass_num == 0:
      set_prefix(instruction, start_line_num, settings)
    elif pass_num == 1:
      pass
  else:
    unknown_header(start_line_num, full_headers, header_index)

def import_data(instruction, start_line_num, variables, node_dict):
  line_num = start_line_num #For clarity- start_line_num not used elsewhere.
  file_name = ""
  for c in instruction:
    if c == ',':
      imported_data = _priv_generate_nodes(file_name)
      node_dict.update(imported_data[0])
      variables += imported_data[1] #Add dictionaries of variables
      file_name = ""
    elif c == '\n':
      line_num += 1
    elif c != ' ' and c != '#':
      file_name += c
  if file_name != "":
    imported_data = _priv_generate_nodes(file_name)
    node_dict.update(imported_data[0])
    variables += imported_data[1]

def create_variable(line_num, var_data, variables):
  #var_data: [name, type, value]
  if var_data[2] == "":
    raise ValueError("Line " + str(line_num) + ": Cannot create variable with empty string")
  var_data[1] = var_data[1].upper() #Capitalize type
  if var_data[1] == "BOOL":
    if var_data[2].upper() not in ["TRUE", "T", "FALSE", "F"]:
      raise ValueError("Line " + str(line_num) + ": Expected TRUE, T, FALSE, or F: Got \"" + var_data[2] + "\"")
    value = var_data[2].upper() == "TRUE" or var_data[2].upper() == "T"
  elif var_data[1] == "INT":
    value = int(var_data[2])
  else:
    raise ValueError("Line: " + str(line_num) + "Unknown type: \"" + var_data[1] + "\"")
  variables[0][var_data[0]] = [var_data[1], value]
def add_variables(instruction, start_line_num, variables, settings):
  line_num = start_line_num #For clarity, start_line_num is not used again
  var_data = [settings["Prefix"], "", ""] #name, type, value
  current_field = 0 #0 for name, 1 for type, 2 for value; indices of var_data
  for c in instruction:
    if c == '(':
      if current_field != 0:
        raise ValueError("Line " + str(line_num) + ": Unexpected '('")
      current_field += 1
    elif c == ':':
      if current_field != 1:
        raise ValueError("Line " + str(line_num) + ": Unexpected ':'")
      current_field += 1
    elif c == ',':
      create_variable(line_num, var_data, variables)
      var_data = [settings["Prefix"], "", ""]
      current_field = 0
    elif c == '\n':
      line_num += 1
    elif c != ' ' and c != ')' and c != '#':
      var_data[current_field] += c
  if var_data[0] != "":
    create_variable(line_num, var_data, variables)

def declare_node_from_name(instruction, start_line_num, node_dict, local_names, settings):
  local_name = clean_text(instruction)
  global_name = settings["Prefix"] + local_name
  try:
    virtual_node = Node.add_virtual_node(global_name)
  except:
    print("Line " + str(start_line_num))
    raise
  local_names.add(local_name)
  node_dict[global_name] = virtual_node

def reset_node_data(node_data, default_node_data):
  for key in default_node_data:
    #Using hasattr() doesn't get around the expensive catch action- hasattr() itself uses try-except
    try:
      node_data[key] = default_node_data[key].copy()
    except AttributeError: #Has no .copy() method, presumably because not affected by reference semantics.
      node_data[key] = default_node_data[key]

def add_node(line_num, node_data, node_dict, local_names, settings):
  local_name = node_data["Name"]
  if local_name in keywords["names"]:
    raise ValueError("Line " + str(line_num) + ": Illegal node name: \"" + local_name + "\"")
  global_name = settings["Prefix"] + local_name
  value = node_data["Value"]
  children = node_data["Children"] #Copying unnecessary- lists get reassigned.
  choices = node_data["Choices"]
  err_message = node_data["Err_message"]
  prompt = node_data["Prompt"]
  if err_message == "":
    err_message = "Invalid input.\n" #Default value, trailing newline gets trimmed
  
  local_names.add(local_name)
  new_err = None
  try:
    new_node = Node(global_name, children, value, choices, err_message, prompt)
  except ValueError as err:
    if err.args[0].startswith("Got duplicate"):
      new_err = ValueError("Line " + str(line_num) + ": Duplicate node name \"" + local_name + "\"")
    elif err.args[0].startswith("Illegal name"):
      new_err = ValueError("Line " + str(line_num) + ": Illegal name for node \"" + local_name + "\"")
    else:
      print("Line: " + str(line_num))
      raise
  except:
    print("Line: " + str(line_num))
    raise
  if new_err != None:
    raise new_err
  node_dict[global_name] = new_node

def convert_escape(line_num, section, variables, node_dict, prefix):
  err_text = check_escape(section, variables, node_dict, prefix, True)
  if err_text != "":
    raise ValueError("Line " + str(line_num) + ": " + err_text)
  
  split_section = text_to_split_section(section, ":", True)
  value = section #Default case
  if split_section[0] == "COLOR":
    color_name = split_section[1]
    value = ColorToColor[color_name]
  elif split_section[0] == "ENTER" or split_section[0] == "RETURN_TO":
    split_section[1] = convert_name_to_global(split_section[1], prefix)
    value = split_section_to_text(split_section, ":", True)
  elif split_section[0] == "CHANGE": #Currently the same as ENTER and RETURN_TO instruction
    split_section[1] = convert_name_to_global(split_section[1], prefix)
    value = split_section_to_text(split_section, ":", True)
  
  return value
def get_data(instruction, start_line_num, variables, node_dict, prefix, strip_trailing_newline=True):
  line_num = start_line_num
  added_data = ""
  val = ""
  is_first_of_line = False
  ignore_newline = False
  for c in instruction:
    if c == '{':
      added_data += val
      val = c #Include '{'
    elif c == '}':
      val += c #Include '}' in the escape
      added_data += convert_escape(line_num, val, variables, node_dict, prefix)
      val = ""
    elif c == '\n':
      line_num += 1
      if not ignore_newline:
        val += c
    elif c != '#':
      val += c
    ignore_newline = (c == '}') or (c == '#' and is_first_of_line) #Set this before updating is_first_of_line for next iteration
    is_first_of_line = c == '\n' #Set it True for next iteration if this was a newline, otherwise false
  added_data += val
  added_data = remove_trailing_newline(added_data) if strip_trailing_newline else added_data
  return added_data

def replace_colors(instruction, start_line_num, strip_trailing_newline=True):
  line_num = start_line_num
  new_text = ""
  cur_val = ""
  is_first_of_line = False
  ignore_newline = False
  for c in instruction:
    if c == '{':
      new_text += cur_val
      cur_val = "" #Will always remove braces
    elif c == '}':
      split_section = text_to_split_section(cur_val, ":")
      if split_section[0] == "COLOR":
        if cur_val in ColorToColor:
          new_text += ColorToColor[cur_val]
        else:
          raise ValueError("Line " + str(line_num) + ": Unknown color \"" + cur_val + "\"")
      else:
        raise ValueError("Line " + str(line_num) + ": Non-color instruction \"{" + cur_val + "}\"")
      cur_val = ""
    elif c == '\n':
      line_num += 1
      if not ignore_newline:
        cur_val += c
    elif c != '#':
      cur_val += c
    ignore_newline = (c == '}') or (c == '#' and is_first_of_line)
    is_first_of_line = c == '\n' #Update this for the next iteration
  new_text += cur_val
  new_text = remove_trailing_newline(new_text) if strip_trailing_newline else new_text
  return new_text

def add_child(line_num, child_name, child_choice, children, choices, node_dict, local_names, prefix):
  """Directly modifies children and choices"""
  global_child_name = (prefix + child_name) if (child_name in local_names) else child_name
  if global_child_name in node_dict: #Automatically add the starting value for name
    children.append(node_dict[global_child_name])
  elif child_name == "__self__" or child_name == "self":
    children.append("__self__") #Node will handle this to make the child a reference to the node.
  else:
    print(node_dict.keys())
    raise ValueError("Line " + str(line_num) + ": Name \"" + child_name + "\" not found in previous nodes.")
  if child_choice != "":
    choices.append(child_choice)
def get_children(instruction, start_line_num, node_dict, local_names, prefix):
  line_num = start_line_num
  potential_trailing_newlines = 0
  new_children = []
  new_choices = []
  child_data = ["", ""] #Name, choice
  field_index = 0
  for c in instruction:
    if c == ':':
      if field_index != 0:
        raise ValueError("Line " + str(line_num) + ": Unexpected colon. Check for missing comma.")
      field_index = 1
    elif c == ',':
      name, choice = child_data #List unpacking
      add_child(line_num, name, choice, new_children, new_choices, node_dict, local_names, prefix)
      field_index = 0
      child_data = ["", ""] #Reset
    elif c == '\n':
      potential_trailing_newlines += 1
    elif c != ' ' and c != '#':
      line_num += potential_trailing_newlines
      potential_trailing_newlines = 0
      child_data[field_index] += c
  name, choice = child_data
  if name != "":
    add_child(line_num, name, choice, new_children, new_choices, node_dict, local_names, prefix)
  return new_children, new_choices

def handle_node(instruction, start_line_num, full_headers, header_index, variables, settings, node_data, node_dict, local_names, default_node_data, pass_num):
  sub_headers = full_headers[header_index:]
  if sub_headers == []: #End of section
    if pass_num == 0:
      pass
    elif pass_num == 1:
      add_node(start_line_num, node_data, node_dict, local_names, settings)
      reset_node_data(node_data, default_node_data)
  elif sub_headers[0] == "NAME":
    if pass_num == 0:
      declare_node_from_name(instruction, start_line_num, node_dict, local_names, settings)
    elif pass_num == 1:
      node_data["Name"] += clean_text(instruction) #Remove last newline
  elif sub_headers[0] == "VALUE":
    if pass_num == 0:
      pass
    elif pass_num == 1:
      node_data["Value"] += get_data(instruction, start_line_num, variables, node_dict, settings["Prefix"])
  elif sub_headers[0] == "CHILDREN":
    if pass_num == 0:
      pass
    elif pass_num == 1:
      children, choices = get_children(instruction, start_line_num, node_dict, local_names, settings["Prefix"])
      node_data["Children"] += children
      node_data["Choices"] += choices
  elif sub_headers[0] == "CHOICE":
    if pass_num == 0:
      pass
    elif pass_num == 1:
      node_data["Choices"] = convert_name_to_global(clean_text(instruction), settings["Prefix"])
  elif sub_headers[0] == "ERR_MESSAGE": #Using get_data just to handle {COLOR:___} 
    if pass_num == 0:
      pass
    elif pass_num == 1:
      node_data["Err_message"] = replace_colors(instruction, start_line_num)
  elif sub_headers[0] == "PROMPT":
    if pass_num == 0:
      pass
    elif pass_num == 1:
      node_data["Prompt"] = get_data(instruction, start_line_num)
  else:
    unknown_header(start_line_num, full_headers, header_index)

def handle_instruction(cur_section, outer_sections, variables, settings, node_dict, node_data, local_names, default_node_data, pass_num):
  instruction = cur_section.body
  start_line_num = cur_section.body_start_line_num
  headers = [outer_section.name for outer_section in outer_sections] #List comprehension
  if headers == []:
    pass
  elif headers[0] == "__COMMENT__" or headers[0] == "COMMENT":
    pass #Ignore comments
  elif headers[0] == "SETTINGS":
    handle_settings(instruction, start_line_num, headers, 1, settings, pass_num)
  elif headers[0] == "IMPORT":
    if pass_num == 0:
      pass #General pass does nothing with import
    elif pass_num == 1:
      import_data(instruction, start_line_num, variables, node_dict)
  elif headers[0] == "VARIABLES" or headers[0] == "VARIABLE":
    if pass_num == 0:
      add_variables(instruction, start_line_num, variables, settings)
    elif pass_num == 1:
      pass
  elif headers[0] == "NODE":
    handle_node(instruction, start_line_num, headers, 1, settings, node_data, node_dict, local_names, default_node_data, pass_num)
  else:
    unknown_header(start_line_num, headers, 1)



def _priv_generate_nodes(file_name, debug=0):  
  """debug- Bit 0: Header, Bit 1: Starting line num, Bit 2: Section content"""
  global _cur_reading_files
  if file_name in _cur_reading_files:
    raise ValueError("Already reading file " + file_name + ". Circular import likely.")
  _cur_reading_files.append(file_name)
  settings = {
    "Prefix": ""
  }
  node_dict = {}
  local_names = set()
  variables = [{}]
  default_node_data = {
    "Name": "",
    "Value": "",
    "Children": [],
    "Choices": [],
    "Err_message": "",
    "Prompt": ""
  }
  cur_node_data = default_node_data.copy()
  outermost_section = generate_sections(file_name, True, debug)
  for pass_num in range(2):
    traverse_sections(outermost_section, handle_instruction, (variables, settings, node_dict, cur_node_data, local_names, default_node_data, pass_num), {}, False)
  _cur_reading_files.remove(file_name)
  return node_dict, variables, local_names, settings["Prefix"]

def generate_nodes(file_name, debug=0):
  """Returns a dictionary of the nodes created in file_name and a dictionary of the variables created in file_name.
  debug- Bit 0: Header, Bit 1: Starting line num, Bit 2: Section content"""
  global _cur_reading_files
  try:
    node_dict, variables, local_names, prefix = _priv_generate_nodes(file_name, debug)
  except:
    _cur_reading_files.clear() #_cur_reading_files will only be non-empty in errors
    Node.reset() #This should only be called if there's an error- Can't be placed in a finally clause.
    raise
  local_node_dict = {}
  for local_name in local_names:
    global_name = prefix + local_name
    local_node_dict[local_name] = node_dict[global_name]
  return local_node_dict, variables
