import time #Imports for handling instructions
from util.colors import ColorToColor
from util.console.output import clearConsole, loading_effect
from util.console.input import validate_input
from util.variable.variables import add_item
from combat.battle import full_battle
from util.variable.instances import characters, enemies

from util.console.output import delay_print #Import for regular text

from narrative.nodes.hub import keywords, remove_trailing_newline, section_strip, text_to_split_section, type_name, value_in_dicts #Imports for text handling and miscellaneous functions

def color_instruct(split_instruction):
  color_name = split_instruction[1]
  print(ColorToColor[color_name], end="")

def time_instruct(split_instruction):
  duration = float(split_instruction[1])
  time.sleep(duration)

def get_node_from_instruct(split_instruction, num_colons_before_name):
  node_name = split_instruction[num_colons_before_name] #If 1 colon before name, want 2nd item, or index 1
  return StoryNode.all_nodes[node_name]

def add_item_from_instruct(split_instruction):
  arguments = text_to_split_section(split_instruction[1], ";", False)
  #item_name, [description, [price, [damageAmt]]]
  num_args = len(arguments)
  if num_args != 4:
    raise TypeError("ADD_ITEM must have 4 values")
  add_item(arguments[0], arguments[1], arguments[2], arguments[4])

def change_variable(split_instruction, variables):
  var_name = split_instruction[1]
  new_value = None if len(split_instruction) <= 2 else split_instruction[2]
  var_data, found = value_in_dicts(variables, var_name)
  if not found:
    raise ValueError("Variable \"" + var_name + "\" not found")
  if var_data[0] == "BOOL":
    var_data[1] = (new_value == None) or (new_value.upper() == "TRUE") #The default value (or when var_value == None) is True
  elif var_data[0] == "INT":
    if new_value == None:
      raise ValueError("Expected new value for integer assignment")
    elif new_value[0] == '=':
      int_val = int(new_value[1:])
      var_data[1] = int_val
    else:
      int_val = int(new_value)
      var_data[1] += int_val

def handle_character(split_instruction):
  character = characters[split_instruction[1]]
  stat = split_instruction[2]
  if stat == "HP":
    new_value = split_instruction[3]
    int_val = character.MaxHP if new_value[1:]=="MAX" else int(new_value[1:])
    if new_value[0] == '=':
      character.setHP(int_val)
    elif new_value[0] == '-':
      character.dealDamage(int_val)
    else: #new_value[0] == '+'
      character.heal(int_val)

def battle_from_instruction(split_instruction):
  variables = text_to_split_section(split_instruction[1], ";", False)
  num_variables = len(variables)
  battle_party = []
  party_member_names = variables[0].split(",") #Shouldn't have escape sequence, using builtin method
  for party_member_name in party_member_names:
    character = characters[section_strip(party_member_name)]
    battle_party.append(character)
  enemy_party = []
  enemy_names = variables[1].split(",") #Also shouldn't have escape sequence, can use builtin method
  for enemy_name in enemy_names:
    enemy_name = enemy_name.lower() #Change to match format in util/variables/instances
    template_enemy = enemies[section_strip(enemy_name)]
    enemy_party.append(template_enemy.copy()) #Make sure to copy!
  location = section_strip(variables[2])
  intro = section_strip(variables[3])
  primary_enemy_name = section_strip(variables[4])
  if num_variables == 5:
    full_battle(battle_party, enemy_party, location, intro, primary_enemy_name)
  elif num_variables == 6:
    lose_message = section_strip(variables[5]) #Stored for clarity
    full_battle(battle_party, enemy_party, location, intro, primary_enemy_name, lose_message)

def handle_instruct(instruction, variables):
  """Returns a dictionary with information about instructions for caller.

  "Return": True if caller should exit, False if not.

  "Return depth": How many calls back to go, negative if infinite.

  "Return node": A reference to the node to return until reaching if applicable, None if not.

  "Target node": A reference to the node to jump to if applicable, None if not."""
  instruct_status = {
    "Return": False,
    "Return depth": 0,
    "Return node": None,
    "Target node": None,
  }
  split_instruction = text_to_split_section(instruction, ":", False)
  if split_instruction[0] == "COLOR": #Simple instructions
    color_instruct(split_instruction)
  elif split_instruction[0] == "TIME":
    time_instruct(split_instruction)
  elif split_instruction[0] == "CLEAR":
    clearConsole()
  elif split_instruction[0] == "LOADING_EFFECT":
    loading_effect()
  elif split_instruction[0] == "EXIT_ALL": #Jump instructions
    instruct_status["Return depth"] = -1
    instruct_status["Return"] = True
  elif split_instruction[0] == "EXIT_NODE":
    instruct_status["Return depth"] = 0
    instruct_status["Return"] = True
  elif split_instruction[0] == "RETURN_TO":
    instruct_status["Return node"] = get_node_from_instruct(split_instruction, 1)
  elif split_instruction[0] == "ENTER":
    instruct_status["Target node"] = get_node_from_instruct(split_instruction, 1)
  elif split_instruction[0] == "ADD_ITEM": #Inventory, variables, characters
    add_item_from_instruct(split_instruction)
  elif split_instruction[0] == "CHANGE":
    change_variable(split_instruction, variables)
  elif split_instruction[0] == "CHARACTER":
    handle_character(split_instruction)
  elif split_instruction[0] == "BATTLE": #Battle
    battle_from_instruction(split_instruction)
  return instruct_status

class StoryNode:
  _virtual_node_names = set() #Node names which aren't yet initialized.
  all_nodes = {}
  cur_node_name = ""

  def get_cur_node():
    return StoryNode.cur_node_name

  def set_cur_node(cur_node):
    StoryNode.cur_node_name = cur_node.name

  def reset():
    StoryNode.all_nodes.clear()
    StoryNode._virtual_node_names.clear()
  
  def add_virtual_node(name): #Maybe change to a better name? This is probably okay, though.
    """Makes a minimal (or virtual) node which will update once if a node is initialized with the same name. Calls on add_virtual_node() with the same name will create a new node."""
    if type(name) != type(""):
      raise TypeError("Expected str; Got " + type_name(name))
    virtual_node = StoryNode(name, [], "", []) #Create a minimal node
    StoryNode._virtual_node_names.add(name)
    return virtual_node
  
  def __new__(cls, *args, **kwargs): #Handle construction and initialization of virtual nodes.
    name = kwargs["name"] if ("name" in kwargs) else args[0]
    if name in StoryNode._virtual_node_names:
      return StoryNode.all_nodes[name] #Don't make a new Node- Use the existing node with that name
    return object.__new__(cls) #Default case
  
  def __init__(self, name, nodes, value, choices, err_message="Enter a valid input: ", prompt=""):
    #Set self.name
    if not isinstance(name, str):
      raise TypeError("Expected str for name; got " + type_name(name))
    if name in StoryNode._virtual_node_names:
      StoryNode._virtual_node_names.remove(name) #Last check of StoryNode._virtual_node_names in creation- safe to remove name
    elif name in StoryNode.all_nodes: #Don't check this for virtual nodes
      raise ValueError("Got duplicate \"" + name + "\"")
    elif name in keywords["names"]:
      raise ValueError("Illegal name: \"" + name + "\"")
    self.name = name
    #Set self.nodes
    self.nodes = []
    for node_entry in nodes:
      if isinstance(node_entry, str):
        if node_entry == "__self__" or node_entry == "self":
          self.nodes.append(self)
        elif node_entry in StoryNode.all_nodes:
          self.nodes.append(StoryNode.all_nodes[node_entry])
        #No error in else clause because names of nodes not yet created is allowed
      elif type(node_entry) == type(self): #Is a node
        self.nodes.append(node_entry)
      else:
        raise TypeError("Unsupported type of child entry: " + str(type(node_entry)))
    #Set self.value
    self.value = remove_trailing_newline(value)
    #Set self.choices (gets set in either branch)
    if isinstance(choices, str): #Variable name
      self.choices = choices
    elif hasattr(choices, "__iter__"): #Iterable of options for the player
      self.choices = []
      for choice in choices:
        self.choices.append(str(choice))
    else:
      raise TypeError("Expected str or iterable for choices; Got " + type_name(choices))
    #Set self.err_message
    self.err_message = remove_trailing_newline(err_message)
    #Set self.prompt
    self.prompt = remove_trailing_newline(prompt)
    #Update Node.all_nodes
    StoryNode.all_nodes[name] = self
  
  def __repr__(self):
    return self.name
    
  def get_option_index(self, variables):
    if self.choices == []:
      return None
    if type(self.choices) == type(""):
      var_data, found = value_in_dicts(variables, self.choices)
      if found:
        option_index = int(var_data[1])
        return option_index
      raise ValueError("Variable \"" + self.choices + "\" not in variables")
    var_data, found = value_in_dicts(variables, self.choices[0])
    if found:
      option_index = int(var_data[1])
      return option_index
    user_input = validate_input(self.choices, self.err_message, self.prompt)
    option_index = self.choices.index(user_input) #Finds the first index user_input appears at in self.choices
    return option_index

  def priv_traverse(self, variables, debug=7):
    """debug: 1s bit: print on enter, 2s bit: print on exit, 4s bit: print instruction data"""
    if debug & 1:
      print("[ENTER: " + self.name + "]") #Testing
    StoryNode.cur_node_name = self.name
    status = { #Used for communication with other priv_traverse() calls
      "Return depth": 0,
      "Return target": None
    }
    val = "" #Stores either the current instruction or text to delay_print
    for c in self.value: #At each {, delay_prints all characters after the previous brace. At each }, handles the instruction composed of all characters after the previous brace.
      if c == '{':
        if val != "": #Separated checks for clarity
          delay_print(val, end="")
          val = ""
      elif c == '}':
        instruct_data = handle_instruct(val, variables)
        if debug & 4:
          print(instruct_data) #Testing
        status["Return depth"] = instruct_data["Return depth"]
        status["Return target"] = instruct_data["Return node"]
        enter_targ_node = instruct_data["Target node"] #targ_node to enter
        if instruct_data["Return"] and status["Return target"] is not self: #Works for None values too
          if debug & 2:
            print("[EXIT: " + self.name + "] (Return instruction)")
          return status
        elif enter_targ_node != None: #Target to enter
          targ_status = enter_targ_node.priv_traverse(variables, debug)
          StoryNode.cur_node_name = self.name #Returned back to self
          if (targ_status["Return target"] != None) and (targ_status["Return target"] is not self):
            status["Return target"] = targ_status["Return target"] #Keep on searching for return target
            if debug & 2:
              print("[EXIT: " + self.name + "] (Returning to target)")
            return status
          elif targ_status["Return depth"] > 0:
            status["Return depth"] = targ_status["Return depth"] - 1
            if debug & 2:
              print("[EXIT: " + self.name + "] (Returning set distance)")
            return status
        val = "" #Reset val
      else: #Ignore '{' and '}' in value
        val += c
    if val != "":
      delay_print(val)
    
    option_index = self.get_option_index(variables)
    if option_index == None: #No children
      if debug & 2:
        print("[EXIT: " + self.name + "] (Finished traversal, no children)")
      return status
    targ_node = self.nodes[option_index]
    if type(targ_node) == type(""): #Allow for entering node names
      targ_node = StoryNode.all_nodes[targ_node]
    targ_status = targ_node.priv_traverse(variables, debug)
    #Shouldn't need to set Node.cur_node_name to self.name because this will soon leave this node
    status["Return target"] = targ_status["Return target"]
    status["Return depth"] = targ_status["Return depth"]
    if debug & 2:
      print("[EXIT: " + self.name + "] (Finished traversal of children)")
    return status
  
  def traverse(self, variables, debug):
    """debug: 1s bit: print on enter, 2s bit: print on exit, 4s bit: print instruction data"""
    # Begin traversal
    self.priv_traverse(variables, debug)
    # Reset Node.cur_node_name to indicate no node currently traversed.
    StoryNode.cur_node_name = ""

Node = StoryNode #Support old name of StoryNode
get_cur_node = StoryNode.get_cur_node
