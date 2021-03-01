def get_func_name(function):
  name = str(function)
  name = name[10:] #Get rid of "<function " at the front
  name_length = len(name)
  i = 0
  while i < name_length:
    if name[i] == ' ':
      break
    i += 1
  name = name[:i] #i is the index of the space, so we don't want to include it
  return name

funcs = {}

def add_func_to_dict(func_dict, function):
  function_name = get_func_name(function)
  func_dict[function_name] = function
def add_funcs_to_dict(func_dict, functions):
  for function in functions:
    function_name = get_func_name(function)
    func_dict[function_name] = function

def global_add_func(function):
  add_func_to_dict(funcs, function)
def global_add_funcs(functions):
  add_funcs_to_dict(funcs, functions)
add_func = global_add_func
add_funcs = global_add_funcs