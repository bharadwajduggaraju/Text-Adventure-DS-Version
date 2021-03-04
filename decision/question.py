## Create a question 
import sys
sys.append("../")
from util.console.output import delay_print
from util.console.input import validate_int_input

class Node:
  def __init__(self, text, prompt, options=[]):
    """Each option should be a list with the text and the target node"""
    self.text = text
    self.prompt = prompt
    self.options = options
    self.num_options = len(options)
  
  def add_option(self, option_text, node, index=-1):
    option = [option_text, node]
    if index == -1:
      self.options.append(option)
    else:
      self.options = self.options[:index] + [option] + self.options[index:]
  
  def traverse(self, errMessage="Invalid input.\n"):
    delay_print(self.text) #Print situation
    for i in range(self.num_options): #Print options
      delay_print(str(i) + ". " + self.options[i][0])
    
    choice_ind = validate_int_input(range(1, self.num_options+1), errMessage, self.prompt) - 1 #Get index of choice

    targ_node = self.options[choice_ind][1]
    if type(targ_node) == type(self): #If the option leads to another node
      targ_node.traverse()
class Question:
  def __init__(self, nodes, value):
	  self.nodes = nodes
	  self.value = value
	  self.length = len(nodes)
  
  def option(self, currentChoices, choice=[]):
    delay_print(self.value)
    choice = validate_int_input(currentChoices, "Invalid input: ")