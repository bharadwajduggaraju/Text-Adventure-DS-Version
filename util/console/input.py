import time, sys #Functions for operation
from util.console.output import delay_print, clearConsole

# from util.colors import * #Variables
import util.colors as col
from util.colors import RESET
from util.console.output import Output
from combat.timer import Timer
from util.variable.variables import inventory

#Imported for testing:
#[currently none]

def get_float_input(prompt="", print_with_delay=False):
  no_answer = True
  while no_answer:
    try:
      answer = float(getInput(prompt, print_with_delay))
      no_answer = False
    except ValueError:
      no_answer = True
  return answer

#Input with Error Message
def validate_input(accepted_list, errMessage, prompt="", print_with_delay=False, validate=True):
  for i in range(len(accepted_list)):
    accepted_list[i] = accepted_list[i].upper()
  validate = validate and accepted_list != [] #Set validate False if accepted_list == []
  user_input = getInput(prompt, print_with_delay).upper()
  while (user_input not in accepted_list) and validate:
    delay_print(str(errMessage))
    user_input = getInput(prompt, print_with_delay).upper()
  return user_input

def validate_int_input(accepted_list, errMessage, prompt="", print_with_delay=False, validate=True):
  options = []
  for option in accepted_list:
    options.append(str(option))
  answer = validate_input(options, errMessage, prompt, print_with_delay, validate)
  return int(answer)

def yes_no(allow_maybe, errMessage, prompt="", print_with_delay=False, validate=True):
  options = ["YES", "Y", "N", "NO"]
  if allow_maybe:
    options += ["MAYBE", "POSSIBLY"]
  answer = validate_input(options, errMessage, prompt, print_with_delay, validate)
  if answer == "YES":
    answer = "Y"
  elif answer == "NO":
    answer = "N"
  return answer

def getInput(prompt="", print_with_delay=False):
  outFunc = delay_print if print_with_delay else print

  prompt_end = "" if prompt=="" else "\n"
  outFunc(prompt, end=prompt_end)
  userAnswer = input()
  while userAnswer.lower() == "menu":
    menu()
    outFunc(prompt, end=prompt_end)
    userAnswer = input() #So that, after using the menu, the user can reenter an answer to the prompt or reenter the menu
  return userAnswer

#Game Settings
def settings():
  delay_print(col.CYAN_BOLD + "~~~~Settings~~~~" + col.CYAN)
  delay_print("Here, you can modify your settings.")
  delay_print("These are your current settings:")
  delay_print("\t1 - Text Scrolling Speed: " + str(Output.long * 100))
  delay_print("\t2 - Punctuation Pause: " + "on" if Output.punc_pause else "off")  #Python e1 if b else e2 is equivalent to b ? e1 : e2
  delay_print("\t3 - Battle Timer: " + str(Timer.timerMode))
  delay_print("\t4 - Leave Settings")
  delay_print("Which setting would you like to change (type the number)? ")

  modify = validate_input(['1', '2', '3', '4'], "That is an invalid number.")

  if modify == "1":
    delay_print("Type a number from 1 to 10 to act as your text scroll speed.")
    textSpeed = get_float_input()
    while (textSpeed < 1 or textSpeed > 10):
      delay_print("That value is not between 1 and 10.")
      delay_print("Please enter a new value between 1 and 10 as your text scroll speed.")
      textSpeed = get_float_input()
      print("\n")
      time.sleep(1)
    delay_print("Text scroll speed is now set to " + str(textSpeed) + ".")
    time.sleep(1)
    Output.long = float(textSpeed) / 100
  elif modify == "2":
    delay_print("Would you like to pause for punctuation?")
    value = validate_input(["YES", "Y", "NO", "N"], "That is an invalid value.")
    Output.punc_pause = (value == "YES") or (value == "Y")
    if Output.punc_pause:
      punc_mode = "on"
    else:
      punc_mode = "off"
    delay_print("Punctuation pause is " + punc_mode + ".")
    time.sleep(1)
  elif (modify == "3"):
    delay_print("Would you like your battle timer to be on or off?")
    value = validate_input(["ON", "OFF"], "That is an invalid value. ")
    Timer.timerMode = value.lower()
    delay_print("Your battle timer is now set to " + Timer.timerMode + ".")
    time.sleep(1)
  print(RESET, end="")  #end="" prevents the trailing \n
  clearConsole()

#Inventory menu
def inventorymenu(clear=True):
  clearConsole()
  delay_print(col.RED_BOLD + "~~~~Inventory~~~~" + col.RED)
  delay_print("Items:")

  for i in range(len(inventory)):
    delay_print(
      str(i + 1) + ": " + inventory[i].toString()
    )

  if not inventory:
    delay_print(col.RED_ITALIC + "None")
  print(RESET, end="")  #end="" prevents the trailing \n

  time.sleep(1)
  if clear:
    clearConsole()


def getItemFromInventory():
  global inventory
  if (len(inventory) == 0):
    delay_print("You cannot grab an item from an empty inventory.")
    return None
  inventorymenu(False)
  item_index = validate_int_input(range(1, len(inventory) + 1), "Invalid item in array.", "Enter the number for the item. ") - 1
  item = inventory[item_index]
  inventory.remove(item)
  return item

#Tutorial
def tutorial():
  clearConsole()
  global long
  global timerMode
  delay_print(RESET + col.PURPLE_BOLD + "~~~~TUTORIAL~~~~" + RESET + col.LIGHT_PURPLE)
  delay_print("""
    When you are posed with a yes or no question and want to answer, you may type either \"yes\"/\"y\" or \"no\"/\"n\". It is not case sensitive.
    When posed a question, you may type \"menu\" to access the menu. There, you may access the settings, inventory, and tutorial. You may also exit the game, although saving is not yet implemented.
  """ + RESET, indent=4)
  yes_no(False, "You must remember how to answer correctly", "Are you ready to leave?")
  time.sleep(1)
  clearConsole()
  #This is just the omnipresent tutorial, the original tutorial is going to be in a fight. Samiya will explain to the player how to access the omnipresent tutorial in the original tutorial.

def battle_tutorial():
  clearConsole()
  delay_print("""
    Let's learn how to play in battle!
    The first thing to note is that you have a battle timer. You can turn this off or on in your settings menu.
    You can change your settings before the battle begins, but not during.
    Structure:
      1. It prints out all your enemies and their HP.
      2. It prints out everyone on your team and their HP.
      3. It tells you who's turn it is and the time you are given.
    If it is your turn, then you are presented a set of 4 options that are customized to the current character.

    What to do:
    Input #1 - Type in 1-4 based on which move you want to do.
    Input #2 - Type in the enemy # that you want to attack (the corresponding number for each enemy is printed at the beginning with the HP)
    If you have your timer on, you have to do this all in the time limit given.
    Good luck!
  """, indent=4)

#An ironic function for testing functions
def test_functions():
  function = input("Function: ")
  if function == "getItemFromInventory":
    item = getItemFromInventory()
    if item != None:
      print(item[0] + ": " + item[1])
      inventory.append(item)
      time.sleep(1)
  elif function == "validate_input":
    entries = input("Enter valid inputs (comma separated: ").split(", ")
    error = input("Enter error message: ")
    prompt = input("Enter prompt: ")
    delay_in = input("Delay print output? ").lower()
    delay = delay_in == "y" or delay_in == "yes"
    validate_in = input("Validate? ").lower()
    validate = validate_in == "y" or validate_in == "yes" or validate_in == ""
    validate_input(entries, error, prompt, delay, validate)
  # elif function == "village_1":
  #   village_1()

#Call-menu
def menu():
  clearConsole()
  Timer.settings("pause_timers", True)
  print(RESET, end="")
  options = [
    "settings", "inventory", "tutorial", "leave menu", "exit game", "test function"
  ]
  leave = False
  while not leave:
    print(
      "Options:\n\"settings\", \"inventory\", \"tutorial\", \"leave menu\", and \"exit game\"."
    )
    selection = input("What would you like to do? ")
    while selection not in options:
      print("Sorry, I do not recognize that input.")
      selection = input("What would you like to do? ")
    clearConsole()

    if (selection == "settings"):
      settings()
    elif (selection == "inventory"):
      inventorymenu()
    elif (selection == "tutorial"):
      tutorial()
    elif (selection == "exit game"):
      sys.exit(0)
    elif (selection == "leave menu"):
      leave = True
    elif (selection == "test function"):
      test_functions()
    clearConsole()
  Timer.settings("pause_timers", False)
