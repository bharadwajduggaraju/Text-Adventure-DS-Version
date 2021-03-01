#Import Libraries
import sys
import time
import os
import random
import pygame
from replit import audio

from fighting.effects import Effect
from fighting.moveList import Move
from fighting.battle import Battle
from fighting.timer import *

from entities.character import Character
from entities.enemies import Enemy

from util.colors import ColorToColor
from util.colors import *
from util.variables import *
import util.share_functions as functions

def clearConsole():
  os.system('clear')

def getTimerMode():
  #Uses global timerMode
  return timerMode

clearConsole()  #Remove text repl.it gives at the beginning

#Random Encounters
possibility = 5

def randencounter(battle):
  """Pass in a battle instance"""
  battle_happening = random.randint(0, 10)
  if battle_happening > possibility:
    battle.begin()

punc_pause = True
#Text Scrolling Function
def delay_print(s="", speed=None, end='\n', color="WHITE"):
  global long, punc_delays
  if speed != None:
    timer = speed
  else:
    timer = long
  true_delay = 0.1 / (100.0 * timer)  #Makes greater timer values correspond to greater speeds- Helpful for the user setting the scroll speed

  print(ColorToColor[color], end="")

  is_num = False
  #for i in range(len(s)):
    #c = s[i]
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    delay = true_delay
    if punc_pause and not is_num:
      try:
        delay *= punc_delays[c]
      except KeyError:  #If c is not a key in the dictionary
        pass
      # Code by Caden
    is_num = ('0' <= c <= '9') or (is_num and c == '.')
    time.sleep(delay)
  if end != "":
    sys.stdout.write(end)
    sys.stdout.flush()

  print(RESET, end="")

  time.sleep(0.5)

#Input with Error Message
def validate_input(accepted_list, errMessage, prompt="", validate=True):
  user_input = getInput(prompt).upper()
  validate = validate and accepted_list != []
  while (user_input not in accepted_list) and validate:
    print(str(errMessage))
    user_input = getInput(prompt).upper()
  return user_input

def validate_int_input(accepted_list, errMessage, prompt=""):
  options = []
  for option in accepted_list:
    options.append(str(option))
  answer = validate_input(options, errMessage, prompt)
  return int(answer)

def yes_no(allow_maybe, errMessage, prompt=""):
  options = ["YES", "Y", "N", "NO"]
  if allow_maybe:
    options += ["MAYBE", "POSSIBLY"]
  answer = validate_input(options, errMessage, prompt)
  if answer == "YES":
    answer = "Y"
  elif answer == "NO":
    answer = "N"
  return answer

#Trauma Generator
def give_trauma(character, trauma, fear_type, giveTrue=False, target=0):
  if giveTrue:
    fears = true_fear_name
    traus = true_trauma_name
    wounds = true_wound_name
  else:
    fears = fear_name
    traus = trauma_name
    wounds = wound_name

  if fear_type == 0:
    delay_print(
      "That night, " + character.Name + " had a vivid dream- of " +
      fears[trauma] + trauma_entities[target] +
      ". They awoke screaming, and despite their best efforts, the fear will not leave."
    )
  elif fear_type == 1:
    delay_print(
      "That night, " + character.Name +
      " felt the injury more than ever. Despite the care given to them, their "
      + wounds[trauma] + " is here to stay.")
  else:
    delay_print(
      "That night, " + character.Name +
      " sat with their head in their hands, the dark pressing in around them, their "
      + traus[trauma] + trauma_entities[target] +
      " gnawing at them. The pain will remain with them even after the sun rises."
    )

def death(character):
  if character.die():
    delay_print(
      "placeholder - will probably write if statements so that each character can get a customized death scene"
    )

#Game Settings
def settings():
  global long
  global punc_pause
  global timerMode
  delay_print(CYAN_BOLD + "~~~~Settings~~~~" + CYAN)
  delay_print("Here, you can modify your settings.")
  delay_print("Here are your current settings:")
  delay_print("\t1 - Text Scrolling Speed: " + str(long * 100))
  delay_print("\t2 - Punctuation Pause: " + "on" if punc_pause else "off")  #Python e1 if b else e2 is equivalent to b ? e1 : e2
  delay_print("\t3 - Battle Timer: " + str(timerMode))
  delay_print("\t4 - Leave Settings")
  delay_print("Which setting would you like to change (type the number)? ")

  modify = validate_input(['1', '2', '3', '4'], "That is an invalid number.")

  if modify == "1":
    delay_print("Type a number from 1 to 10 to act as your text scroll speed.")
    textSpeed = float(input())
    while (textSpeed < 1 or textSpeed > 10):
      delay_print("That value is not between 1 and 10.")
      delay_print("Please enter a new value between 1 and 10 as your text scroll speed.")
      textSpeed = float(input())
      print("\n")
      time.sleep(1)
    delay_print("Text scroll speed is now set to " + str(textSpeed) + ".")
    time.sleep(1)
    long = float(textSpeed) / 100
  elif modify == "2":
    delay_print("Would you like to pause for punctuation?")
    value = validate_input(["YES", "Y", "NO", "N"], "That is an invalid value.")
    punc_pause = (value == "YES") or (value == "Y")
    if punc_pause:
      punc_mode = "on"
    else:
      punc_mode = "off"
    delay_print("Punctuation pause is " + punc_mode + ".")
    time.sleep(1)
  elif (modify == "3"):
    delay_print("Would you like your battle timer to be on or off?")
    value = validate_input(["ON", "OFF"], "That is an invalid value. ")
    timerMode = value.lower()
    delay_print("Your battle timer is now set to " + timerMode + ".")
    time.sleep(1)
  print(RESET, end="")  #end="" prevents the trailing \n
  clearConsole()


#Inventory menu
def inventorymenu(clear=True):
  clearConsole()
  delay_print(RED_BOLD + "~~~~Inventory~~~~" + RED)
  delay_print("Items:")

  for i in range(len(inventory)):
    delay_print(
      str(i + 1) + ": " + inventory[i][0] + " - " + inventory[i][1])

  if not inventory:
    delay_print(RED_ITALIC + "None")
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
  delay_print(RESET + PURPLE_BOLD + "~~~~TUTORIAL~~~~" + RESET + LIGHT_PURPLE)
  delay_print(
    "When you are posed with a yes or no question and want to answer, you may type either 'yes'/'y' or 'no'/'n'. It is not case sensitive."
  )
  delay_print(
    "When posed a question, you may type 'menu' to access the menu. There, you may access the settings, inventory, and tutorial. You may also exit the game, although saving is not yet implemented."
    + RESET)
  time.sleep(1)
  clearConsole()
  #This is just the omnipresent tutorial, the original tutorial is going to be in a fight. Samiya will explain to the player how to access the omnipresent tutorial in the original tutorial.

def battle_tutorial():
  clearConsole()
  delay_print(
    "Let's learn how to play in battle!"
  )
  delay_print(
    "The first thing to note is that you are have a battle timer. You can turn this off or on in your settings menu."
  )
  delay_print(
    "You can change your settings before the battle begins, but not during."
  )
  delay_print(
    "Structure:"
  )
  delay_print(
    "1. It prints out all your enemies and their HP."
  )
  delay_print(
    "2. It prints out everyone on your team and their HP."
  )
  delay_print(
    "3. It tells you who's turn it is and the time you are given"
  )
  delay_print(
    "If it is your turn, then you are presented a set of 4 options that are customized to the current character."
  )
  delay_print(
    "What to do: "
  )
  delay_print(
    "Input #1 - Type in 1-4 based on which move you want to do."
  )
  delay_print(
    "Input #2 - Type in the enemy # that you want to attack (the corresponding number for each enemy is printed at the beginning with the HP)"
  )
  delay_print(
    "If you have your timer on, you have to do this all in the time limit given."
  )
  delay_print(
    "Good luck!"
  )

#Loading Effect()
def loading_effect():
  global long
  old = long
  long = 0.0015 * punc_delays['.']
  loading_speed = 0.0015 * punc_delays['.']
  #Because of how delay_print calculates the delay, multiplying long by punc_delays['.'] divides the time delay by punc_delays['.']

  clearConsole()
  for i in range(3):
    time.sleep(0.5)
    delay_print("...", speed=loading_speed, end="")
    clearConsole()

  long = old

def finley():
  time.sleep(1)
  clearConsole()

def otis(string):
  print(DARK_RED + string + RESET)

#Villages
minu_visits = 0
stole_something = False
minu_mad = False
def village_1():
  global minu_visits
  global stole_something
  global minu_mad
  quest_completion = True
  clearConsole()
  delay_print("Please select which location you would like to visit.")
  delay_print(" 1. Chief's House")
  delay_print(" 2. Noble House")
  delay_print(" 3. Carpenter's House")
  delay_print(" 4. Cobbler's House")
  delay_print(" 5. Tailor's House")
  delay_print(" 6. Old Lady's House")
  delay_print(" 7. Apothecary")
  delay_print(" 8. Church")
  delay_print(" 9. Town Square")
  delay_print(" 10. Servants' Quarters")
  delay_print(" 11. Dark Forest")
  if quest_completion == True:
    delay_print(" 12. Bright Forest Path")
  snowball = validate_int_input(
    range(1, 13), "Invalid input",
    "Type the number of your destination here: ")  #Limited to 1 through 11
  if snowball == 1:
    if quest_completion == False:
      print(DARK_RED + "CHIEF'S HOUSE" + DARK_RED)
      time.sleep(0.25)
      delay_print(WHITE + 
        "The door is locked!" + WHITE)
      time.sleep(1)
      clearConsole()
      village_1()
    if quest_completion == True:
      print(DARK_RED + "CHIEF'S HOUSE" + DARK_RED)
      time.sleep(0.25)
      delay_print(WHITE + 
      "You take in your surroundings. Much of the room is carved in dark stained oak. " + WHITE)
  elif snowball == 2:
    print(DARK_RED + "NOBLE HOUSE" + DARK_RED)
    time.sleep(0.25)
    if quest_completion == False:
      delay_print(WHITE + "The door is locked!" + WHITE)
      time.sleep(1)
      clearConsole()
      village_1()
    if quest_completion == True:
      delay_print(WHITE + "The knocker thumps hollowly against the door." + WHITE)
      delay_print("You hear frantic footsteps scuttling in your direction.")
      delay_print("The door creaks open, revealing a stout old butler in a tuxedo.")
      delay_print(
        "'Stay out of this house!' he whines. 'The master is not expecting visitors!'" +
        WHITE)
      delay_print("You were shoved out of the house!")
      time.sleep(1)
      clearConsole()
      village_1()
  elif snowball == 3:
    def carpenterhouse():
      global minu_visits
      global stole_something
      global minu_mad
      if stole_something == True:
        delay_print("You can't enter! They might find out that you stole Minu's amulet!")
        time.sleep(1)
        clearConsole()
        village_1()
      else:
        if quest_completion == False:
          clearConsole()
          print(DARK_RED + "CARPENTER'S HOUSE" + DARK_RED)
          time.sleep(0.25)
          delay_print("The door is locked!")
          time.sleep(1)
          clearConsole()
          village_1()
        elif quest_completion == True:
          clearConsole()
          print(DARK_RED + "CARPENTER'S HOUSE" + DARK_RED)
          time.sleep(0.25)
          delay_print(WHITE + "Who would you like to talk to?" + WHITE)
          delay_print(" 1. Carpenter")
          delay_print(" 2. Carpenter's Wife")
          delay_print(" 3. Carpenter's Daughter")
          delay_print(" 4. Exit House")
          carpenter_family = validate_input(["1", "2", "3", "4"], "Invalid input")
          clearConsole()
          if carpenter_family == "1":
            delay_print("The carpenter glances up at you with a bit of confusion. His eyes crinkle kindly when he recognizes you.")
            delay_print("'Hello, hero!' he says, standing frantically and bowing. 'I greatly appreciate your help. Thank you for saving my wife, my daughter, and I!'")
            delay_print("He looks down at his daughter for a second, expression soft and proud. 'I would never forgive myself if I let her be hurt.'")
            time.sleep(0.25)
            delay_print("You're hit by a pang of jealousy.")
            time.sleep(0.25)
            delay_print("He looks back at you, slightly disoriented. 'Where was I? Ah, yes. We're eating breakfast right now. All we have is rice, but it may be able to help you replenish your energy. Would you like to eat some?'")
            carpenter_breakfast = yes_no(False, "Invalid input").lower()
            if carpenter_breakfast == "yes" or carpenter_breakfast == "y":
              delay_print(
                "'Wonderful!' He grins and proffers a bowl of steaming-hot rice.")
              delay_print(
                "You munch on the food you were offered. It's delicious!")
              time.sleep(1)
              carpenterhouse()
            if carpenter_breakfast == "no" or carpenter_breakfast == "n":
              delay_print(
                "'That's all right,' the carpenter says, slightly disappointed. 'Don't forget to come back another time!'")
              time.sleep(1)
              clearConsole()
              village_1()
          elif carpenter_family == "2":
              delay_print("The carpenter's wife gnaws on rice. She seems distracted.")
              delay_print("'Mmmmm... such good rice...'")
              time.sleep(1)
              carpenterhouse()
          elif carpenter_family == "3":
            if minu_mad == False:
              if minu_visits == 0:
                delay_print("The carpenter's daughter looks downcast. She picks at her rice.")
                delay_print("She glances up at you.")
                delay_print("'Oh, you're the village hero!' she says, recognizing you immediately.")
                delay_print("She kneads her hands. 'What's your name?'")
                delay_print("What will you say?")
                delay_print(" 1. I'm Esteri! I'm the heir to the chiefdom of *insert village name*!")
                delay_print(" 2. You don't deserve to know.")
                delay_print(" 3. Who's the village hero?")
                carpenter_daughter_response = validate_input(["1", "2", "3"],"Invalid input")
                if carpenter_daughter_response == "1":
                  delay_print("'Nice to meet you, Esteri!'")
                  delay_print("The girl bows slightly. 'My name is Minu.'")
                  delay_print("Her expression becomes one of trepidation. 'Can I trust you with a secret?'")
                  delay_print("Choose your response.")
                  delay_print(" 1. Sure!")
                  delay_print(" 2. No way.")
                  carpenter_daughter_secret = validate_input(["1", "2"], "Invalid input")
                  if carpenter_daughter_secret == "1":
                    delay_print("She furtively flicks her gaze to her father.")
                    delay_print("'I'm afraid that my dad is disappointed that I'm not a carpenter,' she confesses.")
                    delay_print("She looks sheepish. 'I wish I could be a good carpenter, I really do. But I enjoy taking care of animals more.'")
                    delay_print("She looks down at her lap. 'Do you think he's mad at me?'")
                    delay_print("What will you say?")
                    delay_print(" 1. I'm sure he loves you a lot. He isn't angry.")
                    delay_print(" 2. I think he is... he seems angry.")
                    carpenter_daughter_disappointed = validate_input(["1", "2"], "Invalid input")
                    if carpenter_daughter_disappointed == "1":
                      delay_print("'Thank you!' Minu's face brightens. 'That makes me feel a lot more confident.'")
                      delay_print("She looks down for a second. 'It's been a while since I'd had a good friend...'")
                      time.sleep(0.5)
                      delay_print("The moment of silence passes, and Minu smiles awkwardly.")
                      time.sleep(0.5)
                      delay_print("She holds out her palm. In it is a small purple stone, pusling with blue light.")
                      delay_print("She grins. 'I'd like you to have this as thanks.'")
                      delay_print("You take the amulet and slip it into your bag.")
                      inventory.append(["Minu's Amulet", "An amulet containing a mysterious healing power."])
                      minu_visits += 1
                      time.sleep(1)
                      clearConsole()
                      carpenterhouse()
                    if carpenter_daughter_disappointed == "2":
                      delay_print("'Oh...' Minu looks concerned. 'I suppose you're right. Thank you for your time, Esteri.'")
                      delay_print("She turns away, looking disheartened.")
                      delay_print("You notice a stone next to her plate, bright red and pulsing with fiery orange streaks.")
                      delay_print("Do you take it?")
                      delay_print(" 1. Yes")
                      delay_print(" 2. No")
                      take_minus_amulet = validate_input(["1", "2"], "Invalid input")
                      if take_minus_amulet == "1":
                        delay_print("You sneak the stone into your bag. No one notices.")
                        inventory.append(["Minu's Amulet", "An amulet containing the power to harm others."])
                        delay_print("You decide to sneak out of the carpenter's house before anyone can catch you.")
                        stole_something = True
                        minu_visits += 1
                        time.sleep(1)
                        clearConsole()
                        village_1()
                      if take_minus_amulet == "2":
                        delay_print("You rescind your hand and smile stiffly.")
                        time.sleep(1)
                        clearConsole()
                        carpenterhouse()
                  if carpenter_daughter_secret == "2":
                    delay_print("Minu smiles softly. 'That's all right. Maybe you can come back another time to hear my secret!'")
                    time.sleep(1)
                    clearConsole()
                    carpenterhouse()
                if carpenter_daughter_response == "2":
                  delay_print("'Well, that was rude!' She looks slightly offended.")
                  minu_mad = True
                  time.sleep(1)
                  clearConsole()
                  carpenterhouse()
                if carpenter_daughter_response == "3":
                  delay_print("'Oh... maybe I picked the wrong person. Sorry!' She looks slightly uncomfortable.")
                  time.sleep(1)
                  clearConsole()
                  carpenterhouse()
              else:
                delay_print("'This rice is delicious!'")
            elif minu_mad == True: 
              delay_print("You shouldn't go over to her! She's angry!")
              time.sleep(1)
              clearConsole()
              carpenterhouse()
          else:  #carpenter_family == 4
              time.sleep(0.5)
              clearConsole()
              village_1()
    carpenterhouse()
  elif snowball == 4:
    #Cobbler's House
    pass
  elif snowball == 5:
    
    pass
  elif snowball == 6:
    #Old Lady's House
    pass
  elif snowball == 7:
    #Apotehcary
    pass
  elif snowball == 8:
    #Church
    pass
  elif snowball == 9:
    #Town Square
    pass
  elif snowball == 10:
    #Servants' Quarters
    pass
  elif snowball == 11:
    pass
  elif snowball == 12:
    if quest_completion == False:
      delay_print("Sorry, but you can't access this area yet. Please try again.")
      village_1()
    else:
      pass


#An ironic function for testing functions
def test_functions():
  function = input("Function: ")
  if function == "delay_print":
    global punc_delays
    yarn = input("Text to print: ")  #yarn- Pun on string
    speed = input("Scroll speed: ")
    while True:
      punc = input("Enter punctuation: ")
      delay = input("Enter delay: ")
      if punc == "" or delay == "":
        break
      punc_delays[punc] = float(delay)
    print(punc_delays)
    if speed == "":
      delay_print(yarn)
    else:
      delay_print(yarn, float(speed))
  elif function == "give_trauma":
    character = [input()]
    trauma = int(input())
    fear_type = int(input())
    arr_type = input("True or False: ")
    target = int(input())
    give_trauma(characters[character], trauma, fear_type, arr_type, target)
  elif function == "loading_effect":
    clearConsole()
    loading_effect()
  elif function == "getItemFromInventory":
    item = getItemFromInventory()
    if item != None:
      print(item[0] + ": " + item[1])
      inventory.append(item)
      time.sleep(1)
  elif function == "village_1":
    village_1()

#Call-menu
def menu():
  clearConsole()
  pauseTimers(True, True)
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
  pauseTimers(True, False)


#File writing
def file_writing(file_name):
  with open(file_name, 'r') as reader:
    arr = reader.read()
    lines = arr.split("\n\n")  #So that paragraphs can stick together
  for line in lines:
    delay_print(line)

#Formerly functionCall()
def getInput(prompt=""):
  userAnswer = input(prompt)
  while userAnswer.lower() == "menu":
    menu()
    userAnswer = input(prompt) #So that, after using the menu, the user can reenter an answer to the prompt or reenter the menu
  return userAnswer

#Give Battle and Move access to functions and necessary variables
functions.global_add_funcs([delay_print, getInput, clearConsole, validate_input, validate_int_input, getTimerMode])

#Battle.setup(party, locations, enemies)

#GAME CODE - Introduction
def introduction():
  delay_print(
    "Amaliyah scampered through the trees, ducking and dodging low-hanging branches and sliding over the slick leaves scattered on the ground."
  )
  delay_print(
    "The air was musty with the smell of petrichor as rain dribbled down around her, wetting the soil and leading it to convalesce into a muddy slush."
  )
  delay_print()
  delay_print(
    "Breath ragged, she tore down the badly marked forest path."
  )
  delay_print(
    "Her footsteps pounded with urgency."
  )
  delay_print(
    "In the distance, howls rang through the air- the distinct call of a pack of Kirin that had caught the smell of fresh meat."
  )
  delay_print(
    "Her chest seized as she thought of the bloodthirsty expressions etched on each of their psychopathic wolfish faces, foreboding masks of doom."
  )
  time.sleep(1)
  clearConsole()
  delay_print(
    "Amaliyah gripped her sword tightly in one sweaty hand and her shield in the other."
  )
  delay_print(
    "Her eyes widened instinctively with fear as she rounded the corner and saw the Clearing of the Kirin awaiting her arrival."
  )
  delay_print(
    "Feet smashing leaves into pulp as she fled across the packed dirt, she wildly attempted to escape from the circular gap in the trees."
  )
  time.sleep(1)
  delay_print(
    "But the Kirin were not so easily tricked."
  )
  delay_print(
    "A magical barrier shot up, twinkling with light and blocking her path."
  )
  delay_print(
    "She knelt on the ground, catching her breath."
  )
  delay_print(
    "The clearing was still, with the exception of a few stray leaves that twirled through the air and gently came to a rest on the grass."
  )
  delay_print(
    "Trees waved about in a leisurely fashion, flaunting the autumn leaves dangling from their branches and burning with the colors of flame."
  )
  time.sleep(1)
  clearConsole()
  delay_print(
    "Strained now, Amaliyah forced herself to stand up, drawing her sword from its scabbard with a steely hiss."
  )
  delay_print(
    "Assuming a confident fighting stance, she whipped her blade behind her suddenly as a rustle sounded in the grass."
  )
  delay_print(
    "Nothing."
  )
  delay_print(
    "Amaliyah gripped the hilt of her sword harder, nerves taut."
  )
  delay_print(
    "Jarring howls pierced through the still air."
  )
  delay_print()
  time.sleep(1)

  #Comments
  '''
  delay_print(WHITE + "You are facing a pack of fifteen kirin." + WHITE)
  delay_print("You must defeat them without letting the timer run out after every move.")
  delay_print("But be careful! They will fight back after every attack you make, so you have to choose your moves carefully.")
  delay_print("You will choose between four attack options and the option to dodge the next attack. You may also access your inventory.")
  delay_print("Dodging is useful when you need more time to think or want to learn what your opponent's attacks are.")
  delay_print("But otherwise, you should select from your move menu or utilize an item from your inventory.")
  delay_print("You'll learn more about your inventory later. For now, let's fight the Kirin using one of your four attacks.")
  '''

  #delay_print("Your four attacks are:")
  #delay_print("1. Sword Slash")
  #delay_print("2. Earthbreaking Stone Spires")
  #delay_print("3. Divine Sword Triple ")
  #delay_print("4. Basic Self-Healing")
  ##NOTE: please don't have divine sword triple or earthbreaking stone spires
  #Change ^ above in the Amaliyah character

  time.sleep(3)
  clearConsole()

def coolPygamePattern():
  introScreen = pygame.display.set_mode((800, 800))
  introScreen.fill((148, 226, 255))

  white = pygame.Color(255, 255, 255)
  lightGray = pygame.Color(230, 230, 230)
  darkGray = pygame.Color(205, 205, 205)
  pygame.draw.circle(introScreen, white, (400, 400), 75)
  pygame.draw.rect(introScreen, white, (385, 500, 30, 300))
  pygame.draw.rect(introScreen, lightGray, (385, 225, 30, 75))

  pygame.draw.rect(introScreen, lightGray, (500, 690, 30, 110))
  pygame.draw.rect(introScreen, lightGray, (600, 757, 30, 43))
  pygame.draw.rect(introScreen, lightGray, (700, 779, 30, 21))
  pygame.draw.rect(introScreen, darkGray, (270, 690, 30, 110))
  pygame.draw.rect(introScreen, darkGray, (170, 757, 30, 43))
  pygame.draw.rect(introScreen, darkGray, (70, 779, 30, 21))

  pygame.display.flip()

def welcome():
  global party
  introScreen = pygame.display.set_mode((800, 800))
  introScreen.fill((148, 226, 255))

  welcome = pygame.image.load("files/images/welcome.png")
  welcome = pygame.transform.scale(welcome, (710, 300))
  position = (40, 70)
  introScreen.blit(welcome, position)

  pygame.display.flip()
  clearConsole()
  print("\\             / |-----  |       ----    ----   |\\  /|  |----- ")
  print(" \\     /\\    /  |       |      |       |    |  | \\/ |  |")
  print("  \\   /  \\  /   |--     |      |       |    |  |    |  |--")
  print("   \\      \\/    |-----  |_____  ----    ----   |    |  |----")

  print()
  #answer = getInput("Press s to skip the intro. Press b just to play the intro battle. Else, press any key to start playing: ")
  answer = validate_input([], "", prompt="Press s to skip the intro. Press b just to play the intro battle. Else, press any key to start playing: ", validate=False).lower()

  clearConsole()

  if (answer != "s"):
    if (answer != "b"):
      introduction()
      clearConsole()
    option = yes_no(
      False, "Please decide soon...",
      "Do you want instructions on how to fight the battle? (this option will not be provided later): "
    )  #OG errMessage: "Decide quickly..."
    if (option == 'YES' or option == 'Y'):
      battle_tutorial()

    clearConsole()
    intro_battle = Battle(
      party, [NormalKirin.copy(), NormalKirin.copy(), InexperiencedKirin.copy()], "Woods",
      "And suddenly, they burst through the trees, howling and scrabbling frantically on the wet leaves.",
      "kirin"
    )
    intro_battle.begin()
    del intro_battle

  party = [Esteri]

  clearConsole()
  delay_print(
    "And as the fire consumed her, there was no pain, not anymore. It was the moment when the ice numbs your hands and the pain fades, down to the shivers of cold, now the tremors of death. And Amaliya\'s mind wandered, to the forest, to the city, to the mountains, to her village in the valley and the daughter she left behind."
  )
  clearConsole()
  time.sleep(0.5)
  delay_print("Esteri.", speed=0.01)
  time.sleep(0.5)
  clearConsole()
  pygame.quit()

#MUSIC
#source = audio.play_file('files/sound/EsteriTheme.mp3')
#source.volume += 0.01
clearConsole()

def adventureBeg():
  #Game Code
  delay_print(WHITE +
    "The voice of the chaplain rings out in sonorous tones across the hall. \"Esteri. Today, you are come of age, and eligible to ascend the throne. As it has been for the many centuries...\"\n The chaplain drones on as you kneel on the flagstones, watching the play of candlelight on the polished rock. Slowly, the chaplain's voice drones to a close."
    + WHITE)
  delay_print(
    "\"In the absence of the Chieftess Amaliyah, and with no kinswomen to anoint you, I hereby pronounce you a noble citizen of the Confederacy of Elyria.\" You rise, turning to face the assembled servants and courtiers with a graceful curtsy as the first rays of sunrise burst over the highest peak."
  )
  delay_print(
    "Beneath you, the capital unfolds in the light, with its stone causeways swooping over the lake and from the mountains. You remain there as the hall slowly empties, despite the cold."
  )
  delay_print(
    "A servant approaches, carrying a small bowl and a missive.\n\"Lady Esteri, this missive from Regent Avivaki. She requests your presence.\"\nYou nod, scanning the parchment. \"I will be there.\""
  )
  delay_print(
    "The servant shakes her head. \"I was also told to relay a second message, from Kosugadde. Er...\"  The servant shrugs. \"He says, \'But first, you should eat your breakfast!\'\""
  )

  delay_print(
    "A few minutes later, you strap your spear to your back, don your breastplate over your tunic, adjust your hair to look mildly presentable, push a bag over your shoulders, and quickly walk out of your chambers. The regent is waiting for you!"
  )
  time.sleep(1)
  clearConsole()
  delay_print(
    "You dash through the streets, veering wildly around the small stone huts that characterize your village, your spear clanking rhythmically on your back. Smoke floats leisurely out of the chimneys, and all around you can hear the sound of the village waking up as the sun begins to rise over the peaks of the snow-capped mountains.\n"
  )
  delay_print(
    "Your eyes land on a pair of stately doors with ornate staffs carved deep into the wood. You have found the regent's residence!"
  )

  option = yes_no(False, "You must decide.", "Do you want to go inside?\n")
  while (option != "YES") and (option != "Y"):
    delay_print(
      "Your aunt will be mad if you don't go..."
    )
    option = yes_no(False, "You must decide.", "Do you want to go inside?\n")

  delay_print(
    "You walk towards the door and are stopped by two guards. \n'Excuse me, miss. You're not allowed here without permission.'"
  )
  delay_print(
    "\"Don't you know who I am?\" You raise an eyebrow with some annoyance.")
  delay_print(
    "The guards look at each other, blank-faced, before one of them blinks and winces. \"Oh dear- Apologies, Lady Esteri. Please come inside. The village regent has been waiting for you.\" The guards bow and step aside."
  )
  loading_effect()

  delay_print(
    "You enter a warm, brightly lit room with ancient scripts pierced onto paintings on the walls. In the middle of the room reclines an aging woman draped with beaded necklaces and a thick woolen coat."
  )
  delay_print(
    "'Please, sit down. We have much to discuss, young one.' \n 'I possess information about your mother, Amaliyah.' Village Regent Avivaki meets your eyes with a solemn expression."
  )
  delay_print(
    "Eager to gain knowledge on your mother, you quickly take a seat and listen."
  )
  delay_print(
    "'We have reasons to believe that your mother, Chieftess Amaliyah, may in fact be alive. Your mother was sent on a mission to find new land for the people of Elyria, and it seems that she has not returned."
  )
  delay_print(
    "'However, as her descendant, the day has come for the task to be bestowed upon you. As the true future Chieftess of Elyria, and my successor, you must embark on this quest to find your mother and complete her mission.'"
  )
  delay_print(
    "'Can we trust you to complete this task with honor?' Her expression is questioning."
  )

  option = yes_no(allow_maybe=True, errMessage="You need to give her a clear answer. She's the chief!")
  if (option == 'MAYBE' or option == 'POSSIBLY'):
    delay_print(
      "'Maybe? That is no way to answer a question from your regent!'"
    )
    option = yes_no(False, "You need to decide now.")

  if (option == 'NO' or option == 'N'):
    delay_print(
      "'Then maybe I have overestimated your abilities. If you do wish to change your mind, please come back later. Elyria is counting on you.'"
    )
    option = yes_no(
      False, "You have one last chance = change your mind. Decide quickly.")
    if (option == 'NO' or option == 'N'):
      delay_print(
        "The pressure is way too much right now. And you're only 18! Maybe you could try again later when you're more prepared."
      )
      sys.exit()

  delay_print(
    "'That's excellent!' The village head smiles, mouth stretching upwards into a grimace of a smile. 'I knew that our people could count on you, Esteri.'"
  )
  delay_print(
    "'You'll require a navigator for your journey, so I've selected one of our skilled navigators-in-training to assist you.'"
  )
  delay_print(
    "The village head frowns. 'But he appears to be a bit late...'"
  )
  delay_print()
  time.sleep(1)
  clearConsole()
  delay_print(
    "The door bursts open and a young man with an unruly mop of brown hair bursts in."
  )
  delay_print(
    "The new arrival wipes sweat off of his brow, glancing up at the village head with a sheepish expression."
  )
  delay_print(
    "The village head glares down at him in indignation. 'You're late.'")
  delay_print()
  delay_print(
    "Your eyes widen as you recognize the man as your old friend, stumbling into a chair with drunken movements."
  )
  delay_print(
    "'Kosu, is that you?' You look at him with a wondrous expression."
  )
  delay_print()
  delay_print(
    "'Hey, Esteri!' Kosu grins. 'It's been a few years, hasn't it? Nice to see you!' I guess you're finally going to-'"
  )
  time.sleep(0.25)
  option = yes_no(
    False, "You need to decide quickly...",
    "Do you interrupt Kosu in order to preserve your dignity? ").lower()

  if option == "y" or option == "yes":
    delay_print(
      "You shoot Kosu a warning glance and he quiets, remorseful. Then you turn to face the village regent."
    )
    delay_print(
      "Her expression is haughty."
    )
    delay_print(
      "Choose what you would like to say to the village head."
    )
    delay_print(
      " 1. 'Apologies, ma'am.'"
    )
    delay_print(
      " 2. 'Kosu and I are friends- you can hardly begrudge us the chance to enjoy our reunion.'"
    )
    delay_print(
      "Enter the number of the answer you prefer."
    )
    

    option = validate_input(['1', '2'], "Decide now! She's the chief!").lower()
    if option == "1":
      delay_print(
        "'You're forgiven,' the village leader says with an air of superiority. 'But don't forget your manners in the future.'"
      )
      delay_print(
        "You bite your tongue to hold back further remarks."
      )
    elif option == "2":
      delay_print(
        "The village leader sniffs in indignation. 'I am a very busy woman. Please enjoy your reunion when you are no longer in my presence.'"
      )
      delay_print(
        "You bite your tongue to hold back further remarks."
      )
    delay_print(
      "Kosu pipes up. 'Is there anything else that we need to know before leaving?'"
    )
  else:
    delay_print(
      "'-get to search for your mom as you've wanted all these years,' Kosu finishes."
    )
    delay_print(
      "Your cheeks flush with embarrassment. 'Yes,' you mutter, and then turn back to face the village leader."
    )
    delay_print(
      "The village leader smirks pridefully. 'What adorable youthful enthusiasm.'"
    )
    delay_print(
      "Kosu shrinks back. 'Is there anything else we need to know before leaving?' he asks quietly."
    )
  delay_print(
    "The village regent folds her hands. 'The path will be dangerous,' she warns, and her face softens a little. 'You really don't have to complete this journey if you are afraid.'"
  )
  delay_print(
    "Kosu shakes his head in indignation. 'We aren't quitters,' he says, voice spiking with an undertone of determination. 'Esteri and I will be fine.'"
  )
  delay_print(
    "You stare at the regent for a second longer, but her stoic face doesn't shift."
  )
  delay_print(
    "'Kosu's right,' you finally assent, voice commanding. 'We will be fine.'")
  time.sleep(1)
  clearConsole()
  delay_print(
    "Regent Aviveki smiles. 'Wonderful,' she says. 'I'll instruct you on where to go.'"
  )
  delay_print(
    "Taking a map from beside her chair, she rolls it out on the table. 'This,' she instructs, 'is the continent of Suto Ratak. Here-' she points at a wide parcel of land- 'is Elyria.'"
  )
  delay_print(
    "She runs her finger along the waxed paper to a large brown spot on the map, split into four quadrants. 'This is Rakunto Ke'koate'nan. It's the largest city in Suto Ratak. It's also your target destination.'"
  )
  delay_print(
    "She moves her finger to a spot on the map closer to your village. 'Here is a small village known as Ai'ko Le'po Koate'nan. An old friend of your mother's resides here. You will begin by traveling to this village, in the hopes that your mother's friend can offer you advice or assistance.'"
  )
  delay_print(
    "She pulls a letter out of her desk and sets it in front of you. 'Deliver this letter to an old woman by the name of Kurigalu. She should be willing to help you find your mother. At the very least, she'll find you someone who can aid you on your journey.'"
  )
  delay_print()
  delay_print(
    "The regent stands up, leaving the letter on the desk in front of you. She meets your eyes."
  )
  delay_print(
    "'Your mother was a friend of mine,' she murmurs, more to herself than you. 'I hope that you can bring her back.'"
  )
  delay_print(
    "She turns, and you watch her retreating back, unable to wipe the sight of Regent Aviveki's regretful, resigned expression from your mind."
  )
  delay_print(
    "Any annoyance you felt towards her during your encounter fades."
  )
  delay_print(
    "Kosu reaches out and picks up the letter. He hands it to you. 'I believe this belongs to you.'"
  )
  delay_print(
    "You take the letter and place it in your bag."
  )
  inventory.append(["Letter for Kurigalu", "An important letter from the regent."])
  time.sleep(1)
  tutorial()
  inventorymenu()
  settings()
  delay_print(
    "'We should go,' you tell Kosu, voice quavering slightly with a near-undetectable hint of fear."
  )
  delay_print(
    "He nods. 'If we don't leave within the hour, we won't make it to Ai'ko Le'po before nightfall.'"
  )
  delay_print(
    "You rest your hand on the doorknob. Your mind wanders for a second.")
  time.sleep(0.25)
  delay_print(
    "You wonder how your mother felt when she was setting out on her journey.")
  time.sleep(1)
  clearConsole()
  delay_print(
    GREY_ITALIC +
    "Mother kneels down, caressing your cheek. 'I'll be back soon, Esi,' she whispers, smiling at you."
  )
  delay_print(
    "'Are you scared, Mommy?' You look up at her, cheeks wet with tears.")
  delay_print(
    "Mother wrings her hands. She stares up at the ceiling, watching the warm light from the lanterns flicker. 'No,' she finally says, a tremor in her voice. 'Dai'ra, Esi. I will be strong for Elyria.'"
  )
  delay_print(
    "'Yes mommy, I know you are never scared of anything'"
  )
  delay_print(
    "She stands up. 'There's nothing wrong with having fears, Esi,' she says, touching your cheek. 'Real bravery is when you're scared, but push through anyway.'She smiles, but her eyes are sad.'Can you promise to be brave for me?' You nod, looking up at her."
  )
  delay_print(
    "'Goodbye, Mommy,' you whisper, wrapping your arms around her leg. 'Come back soon, okay?'"
  )
  delay_print(
    "She looks down at you as if drinking in your appearance one last time. 'I will, Esi. I promise.'"
  )
  time.sleep(0.5)
  delay_print()
  delay_print(
    "Amaliyah walked to the door. Hand shaking, she placed her hand on the knob... and glanced back one last time, meeting Esteri's eyes and mustering a smile."
  )
  time.sleep(0.5)
  clearConsole()
  delay_print("She opened the door." + RESET)
  time.sleep(1)
  clearConsole()
  delay_print(
    "You step out into the blinding sunshine, holding a hand up to shield your eyes."
  )
  delay_print(
    "Light reflects off the snow surrounding you, casting your village in a slight eerie glow."
  )
  delay_print(
    "'Ai'ko Le'po is to the southeast,' Kosu observes, holding up the map.")
  delay_print(
    "You look at him, somewhat solemn. 'You know she was right, Kosu? We could die on this mission.'"
  )
  delay_print(
    "Kosu grins at you. 'We won't die,' he says, unwavering. 'After all, we're the best team in all of Elyria.'"
  )
  delay_print(
    "You raise your eyebrows. 'Is that so?'"
  )
  delay_print(
    "The two of you laugh and banter as you amble down the rocky foothill, traveling the same path that your mother had followed so many years earlier."
  )
  time.sleep(0.25)
  os.system('clear')
  loading_effect()
  time.sleep(0.25)
  delay_print("You slog along, grouchy, with branches snapping under your feet.")
  delay_print(
    "'Are we almost there?' you ask Kosu, with an expression of consternation. 'The woods don't seem to end anytime soon.'"
  )
  delay_print(
    "Kosu studies his map. 'Yeah,' he assures you. 'We'll arrive in the village any minute now.'"
  )
  delay_print(
    "Seconds later, the two of you break through the edge of the forest.")
  delay_print(
    "The trees have been cleared unevenly from a patch of roughly packed land, lined with small huts that creak under the weight of the sky."
  )
  delay_print(
    "'See?' Kosu points out. 'I was right.'"
  )
  delay_print(
    "You ignore him and step forward. 'Something doesn't seem right.'"
  )
  delay_print("'Let's go look,' Kosu says.")

welcome()
village_1()

