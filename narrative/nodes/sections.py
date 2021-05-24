#Section class and generation
class Section: #Section in file
  def __init__(self, body_start_line_num, name, body=""):
    if type(body_start_line_num) != type(0):
      raise TypeError("Expected int for body start line num")
    if type(name) != type(""):
      raise TypeError("Expected str for name")
    if type(body) != type(body):
      raise TypeError("Expected str for value")
    self.body_start_line_num = body_start_line_num
    self.name = name
    self.body = body
    self.children = []
  
  def add_body(self, new_body, is_append=True):
    if type(new_body) != type(""):
      raise TypeError("Expected str for new_value")
    if is_append:
      self.body += new_body
    else:
      self.body = new_body
  
  def add_child(self, child):
    if type(child) != type(self):
      raise TypeError("Expected Section for child")
    self.children.append(child)

def generate_sections(text_or_file_name, is_file_name=True, debug=0):
  """Returns a section whose children are the outermost sections"""
  if is_file_name:
    with open(text_or_file_name) as reader:
      text = reader.read()
  else:
    text = text_or_file_name
  outermost_section = Section(-1, "outer")

  body_start_line_num = 1
  cur_line_num = 1

  #All of these lists start with outermost layer and then go to smaller layers
  cur_sections = [outermost_section]
  headers = []
  indents = [None]
  vals = [""]
  output_list = vals #Switches between vals and headers

  last_char = "\0"
  unmatched_header = False #Header without matching '{'
  escape_braces = 0 #How many '}' to escape
  chars_since_newline = 0
  include_newline = True
  is_comment = False
  is_multiline_comment = False
  for c in text:
    chars_since_newline += 1
    if indents[-1] == None and (c != ' ' and c != '\n' and c != '#'):
      indents[-1] = chars_since_newline
    
    output_list += (last_char if (last_char == '/' and not is_comment and not is_multiline_comment and c != '*') else "") #Indent check unnecessary because last_char won't get set to  '/' in indent
    is_multiline_comment = (is_multiline_comment or (last_char == '/' and c == '*') and (last_char != '*' or c != '/')) #Set True if last_char == '/' and c == '*', set False if last_char == '*' and c == '/'
    if is_multiline_comment:
      last_char = c #Update last_char inside multiline comments for /* and */ check (not done for line comments or inside indents)
      continue
    elif is_comment and c != '\n':
      continue #Skip text in comments except for newlines
    elif ((indents[-1] != None and chars_since_newline < indents[-1]) and (c not in ('\n', '{', '}', '[', ']', '#'))):
      continue #Skip text in indent except for special characters
    
    if c == '{' and unmatched_header:
      unmatched_header = False
      body_start_line_num = cur_line_num
      section = Section(body_start_line_num, headers[-1]) #Create new Section instance
      cur_sections[-1].add_child(section)
      cur_sections.append(section)

      vals.append("") #New value for the section
      indents.append(None) #New (Unknown) indent for the section
      include_newline = False #Ignore a newline at the very beginning of a section body
    elif c == '}' and escape_braces <= 0:
      val = vals.pop()
      val += '\n' if (val != "" and val[-1] != '\n') else "" #Make sure all lines end with newline
      if debug & 1: #Testing
        print(headers, end=" ")
      print(str(body_start_line_num) if (debug & 2) else "", end=("\n" if (debug & 1) else "")) #Testing
      if debug & 4:
        print(val) #Testing
      leaf_section = cur_sections.pop()
      leaf_section.add_body(val)
      headers.pop() #Could save this result if needed
      indents.pop() #Same here
      include_newline = False #Ignore a newline immediately after a subsection
    elif c == '[':
      headers.append("") #New header
      output_list = headers
    elif c == ']':
      if unmatched_header:
        raise ValueError("Line " + str(cur_line_num) + ": Two headers")
      elif escape_braces > 0:
        raise ValueError("Line " + str(cur_line_num) + ": Header inside escape sequence")
      unmatched_header = True
      output_list = vals
    elif c == '\n':
      vals[-1] = vals[-1].rstrip(' ') #Remove spaces at the end of a line
      body_start_line_num += 1 if (indents[-1]==None) else 0 #If indents[-1]==None (start of new section), increase body_start_line_num
      cur_line_num += 1
      output_list[-1] += c if (include_newline or is_comment) else "" #Keep newlines in comments for line counting
      chars_since_newline = 0
      is_comment = False
    elif c == ' ':
      #If indents[-1] == None, then this is part of determining indent. If unmatched header, this is in space between header and body
      output_list[-1] += c if (indents[-1] != None and not unmatched_header) else ""
    elif c == '#':
      vals[-1] = vals[-1].rstrip(' ') #Remove spaces at the end before a comment
      output_list[-1] += c #Include '#' for other functions to know comments
      is_comment = True
    else:
      output_list[-1] += c if c != '/' else "" #If c == '/', only the first 
      escape_braces += int(c == '{') - int(c == '}') #Another right brace to escape if c == '{', and one less remaining if c == '}'
      include_newline = True
    
    last_char = c

  return outermost_section
