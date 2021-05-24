#Import Libraries
import sys
import time
import os
import random
import pygame
from replit import audio

from combat.battle import Battle
from commerce.shop import Shop
from util.colors import *
from util.colors import RESET, WHITE, WHITE_ITALIC, DARK_RED
from util.variable.variables import *
from util.variable.variables import party_money, add_party_member, add_item
from util.variable.instances import Amaliyah, Esteri, Kosu, Dronae, Sentinel, NormalKirin, InexperiencedKirin
from util.variable.instances import *
from util.console.output import delay_print, loading_effect, clearConsole
from util.console.input import validate_input, validate_int_input, yes_no, tutorial, inventorymenu, settings, battle_tutorial
from commerce.trade import *
from commerce.trade import Trade
from narrative.beginning import adventureBeg, amaliyahIntro, credits
add_party_member(Amaliyah)

#Ellipses: "…"

# PLAYER_MONEY = 100
# PLAYER_INVENTORY = []

# # Shop

# shopItems = [{"name": "scarf", "price": 33, "quantity": 2200}]
# shopStats = [{
#   "name": "scarf",
#   "totalMoney": 0,
#   "unitsSold": 0,
#   "discount": False
# }]

# WinterShop = Shop("Arctic Circle", shopItems, shopStats)

# WinterShop.getInfo(PLAYER_MONEY)

# # Trade

# tradeItems = [{"name": "Scarf", "itemsAccepted": ["boot", "shoe", "helmet"]}]

# #Inventory, make dynamic later
# playerInventory = ["boot", "shoe", "helmet", "sock"]

# Winter_Trading_Post = Trade("Winter Trading Post", tradeItems)

# Winter_Trading_Post.beginTrade(playerInventory)

#Random Encounters
possibility = 5

def randencounter(battle):
  """Pass in a battle instance"""
  battle_happening = random.randint(0, 10)
  if battle_happening > possibility:
    battle.begin()

def death(character):
  if character.die():
    delay_print(
      "placeholder - will probably write if statements so that each character can get a customized death scene"
    )

def finley():
  time.sleep(1)
  clearConsole()

def otis(string):
  print(DARK_RED + string + RESET)

#Villages
minu_visits = 0
stole_something = False
minu_mad = False
square_visits = 0
balliya_coat = False

def village_1():
  global minu_visits
  global stole_something
  global minu_mad
  global square_visits
  global balliya_coat
  quest_completion = False
  clearConsole()
  
              
   
  if snowball == 8:
    if quest_completion == False:
        clearConsole()
        print(DARK_RED + "TOWN SQUARE" + DARK_RED)
        time.sleep(0.25)
        delay_print("The area seems barren...")
        time.sleep(1)
        clearConsole()
        village_1()
    elif quest_completion == True:
        clearConsole()
        print(DARK_RED + "TOWN SQUARE" + DARK_RED)
        time.sleep(0.25)
        if square_visits == 0:
          delay_print(WHITE + "The town square is a bustling place, even in overcast weather. Then again, today is market day.")
          delay_print(WHITE + "Still, it feels vaguely like a holiday. The square is decorated with banners, and everyone seems cheerful.")
          delay_print(WHITE + "You turn to Kosu and ask, \"Is today a holiday?\"")
          delay_print(WHITE + "Kosu shrugs. \"I\'m not sure. They taught us more about where things are than what people do.\"")
          delay_print(WHITE + "Still curious, you ask someone selling scarves, \"Excuse me, is today a holiday?\"")
          delay_print(WHITE + "He smiles. \"Not before,\" he says, \"but who knows about the future?\" He winks at you before returning to his hawking.")
        elif square_visits == 1:
          delay_print(WHITE + "Kosu says, \"I'm going to ask the locals about the surrounding area.\"")
          delay_print(WHITE + "You tell him, \"Okay, don't get into trouble.\"")
          delay_print(WHITE + "Kosu nods. \"Of course! I'll stay in the town square.\"")
          delay_print()
          delay_print(WHITE + "You look around slightly uncertainly.")
          delay_print(WHITE + "\"Hello!\"")
          delay_print(WHITE + "You turn towards the voice. It's the scarf seller from earlier!")
          delay_print(WHITE + "\"Excuse me, but where're you from? Your coat looks a little different,\" he asks.")
          delay_print(WHITE + "Slightly surprised, you answer, \"From the mountains.\"")
          delay_print(WHITE + "\"Hm. It looks a bit thick.\"")
          delay_print(WHITE + "You shurg. \"It's very comfortable.\"")
          delay_print(WHITE + "He nods. \" I can see that. But let me know if you want a thinner coat. My name's Balliya, by the way.\"")
          get_coat = yes_no(False, "Please choose again.", "Do you accept Balliya's offer? ")
          balliya_coat = (get_coat == "Y") or (get_coat == "YES")
          delay_print(WHITE + "\"Okay, then. See you later!\"")
        elif square_visits == 2:
          delay_print(WHITE + "\"Hi, Esteri!\"")
          delay_print(WHITE + "You wave back. \"Hello... Balliya, right?\"")
          if balliya_coat:
            delay_print(WHITE + "He nods. \"Here's the coat my wife made for you. Hope you like it!\"")
            add_item("Coat from Balliya", "A lighter coat Balliya's wife made for you.")

        if square_visits <= 3: #3 is placeholder max number of unique events
          square_visits += 1

  

  

# GAME CODE

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

  welcome = pygame.image.load("files/images/welcome2.PNG")
  welcome = pygame.transform.scale(welcome, (710, 300))
  position = (0, 0)
  introScreen.blit(welcome, position)

  pygame.display.flip()
  clearConsole()

  answer = validate_input([], "", prompt="Press s to skip the intro. Press b just to play the intro battle. Else, press any key to start playing: ", validate=False).lower()

  clearConsole()

  if (answer != "s"):
    if (answer != "b"):
      amaliyahIntro()
      clearConsole()
    option = yes_no(
      False, "Decide quickly...",
      "Do you want instructions on how to fight the battle? (this option will not be provided later): "
    )
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
    "And as the fire consumed her, there was no pain, not anymore. It was the moment when the ice numbs your hands and the pain fades, down to the shivers of cold, now the tremors of death. And Amaliyah's mind wandered, to the forest, to the city, to the mountains, to her village in the valley and the daughter she left behind."
  )
  clearConsole()
  time.sleep(0.5)
  delay_print("Esteri.", speed=0.01)
  time.sleep(0.5)
  clearConsole()
  pygame.quit()

#MUSIC
# source = audio.play_file('files/sound/EsteriTheme.mp3')
# source.volume += 0.01
clearConsole()

# Keep this at the bottom of the code please
running = True
if running == True:
  adventureBeg()
  input("Press enter at the cue. ")
  clearConsole()
  time.sleep(4.82)
  credits()
