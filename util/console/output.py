import os, sys, time
from util.colors import ColorToColor, RESET

class Output:
  long = 0.025
  punc_delays = {',': 3, '(': 4, ')': 4, ';': 4, ':': 5, '.': 5, '?': 5, '!': 5}
  punc_pause = True
  def settings(name, value=None):
    """value=None indicates get"""
    is_set = value != None
    if name == "long":
      if is_set:
        if type(value) == type(Output.long):
          Output.long = value
        else:
          raise TypeError
      return Output.long
    elif name == "punc_delays":
      if is_set:
        if type(value) == type([]):
          key = value[0]
          result = value[1]
          if type(key) == type(' ') and type(result) == type(0):
            Output.punc_delays[key] = result
          else:
            raise TypeError
        else:
          raise TypeError
      return Output.punc_delays[key]
    elif name == "punc_pause":
      if is_set:
        if type(value) == type(Output.punc_pause):
          Output.punc_pause = value
        else:
          raise TypeError
      return Output.punc_pause
    elif name == "punc_pause_str":
      if is_set:
        if type(value) == type(""):
          Output.punc_pause = value == "on"
        else:
          raise TypeError
      return "on" if Output.punc_pause else "off"
    else:
      raise ValueError

def clearConsole():
  os.system('clear')

def get_printable_len_from_end(s):
  s_length = len(s)
  printable_len = s_length
  is_format = False
  i = s_length - 1
  while i > 0:
    if not is_format and s[i] != 'm':
      return i + 1
    if s[i] == 'm':
      is_format = True
      printable_len = i + 1
    is_format = is_format and s[i] != '\033' #Forced to false when s[i] == '\033'
    i -= 1
  return printable_len
  
#Text Scrolling Function
def delay_print(s="", speed=None, end='\n', color="WHITE", reset_color=True, indent=0, line_delay=0.5):
  timer = Output.long if (speed == None) else speed
  base_delay = 0.1 / (100.0 * timer)  #Makes greater timer values correspond to greater speeds- Helpful for the user setting the scroll speed

  print(ColorToColor[color], end="")

  s_length = len(s)
  printable_len = get_printable_len_from_end(s)
  
  i = 0
  is_format = False #is in a formatting string- starts out not
  while i < s_length and (is_format or s[i] == '\033'): #Move through any formats before the multiline string
    is_format = (is_format or (s[i] == '\033')) and (s[i] != 'm') #If s[i] != 'm', False- elif s[i] == '\033', True- else, is_format
    i += 1
  print(s[:i], end="")

  if s[i] == '\n':
    i += indent + 1 #Skip starting and indent charcters after that
  is_num = False #Technically unnecessary- Doesn't need to carry information between iterations
  while i < s_length:
    if s[i:printable_len].isspace():
      break
    c = s[i]
    try:
      next_char = s[i+1] #If i == len(s)-1, this raises IndexError
    except IndexError:
      next_char = '\n' #Arbitary, just can't be a digit
    is_num = ('0' <= next_char <= '9')

    sys.stdout.write(c)
    sys.stdout.flush()
    delay = base_delay 
    if Output.punc_pause and not is_num:
      try:
        delay *= Output.punc_delays[c]
      except KeyError: #If c is not a key in the dictionary
        pass
      # Code by Caden
    if c == '\n':
      i += indent if next_char != '\n' else 0 #Skip indent characters ahead if there isn't another newline
      delay = line_delay
    time.sleep(delay)
    i += 1
  if end != "":
    sys.stdout.write(end)
    sys.stdout.flush()

  if reset_color:
    print(RESET, end="")
  print(s[printable_len:], end="")

  time.sleep(0.5)

#Loading Effect()
def loading_effect():
  loading_speed = 0.0015 * Output.punc_delays['.']
  #Because of how delay_print calculates the delay, multiplying long by punc_delays['.'] divides the time delay by punc_delays['.']

  clearConsole()
  for i in range(3):
    time.sleep(0.5)
    delay_print("...", speed=loading_speed, end="")
    clearConsole()
