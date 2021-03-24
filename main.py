#Import Libraries
import sys
import time
import os
import random
import pygame
from replit import audio

from fighting.battle import Battle
from money.shop import Shop
from util.colors import *
from util.variable.variables import *
from util.variable.variables import party_money, add_party_member, add_item
from util.variable.instances import *
from util.console.output import delay_print, loading_effect, clearConsole
from util.console.input import validate_input, validate_int_input, yes_no, tutorial, inventorymenu, settings, battle_tutorial
from money.trade import *
from money.trade import Trade

from story.beginning import adventureBeg, amaliyahIntro

add_party_member(Amaliyah)

STARTING_MONEY = 100

# Shop

# shopItems = [{"name": "scarf", "price": 33, "quantity": 2200}]
# shopStats = [{
#   "name": "scarf",
#   "totalMoney": 0,
#   "unitsSold": 0,
#   "discount": False
# }]

# WinterShop = Shop("Arctic Circle", shopItems, shopStats)

# WinterShop.getInfo(STARTING_MONEY)

# Trade

tradeItems = [{"name": "Scarf", "itemsAccepted": ["boot", "shoe", "helmet"]}]

#Inventory, make dynamic later
playerInventory = ["boot", "shoe", "helmet", "sock"]

Winter_Trading_Post = Trade("Winter", tradeItems)

Winter_Trading_Post.beginTrade(playerInventory)

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

''' Beginning a village modularization.'''
def town_nav(buildingList, name):
  clearConsole()
  delay_print("Please select which location you would like to visit.")
  iteration = 0
  for building in buildingList:
      delay_print(str(iteration) + ". " + str(buildingList[iteration]))
      iteration += 1
  destination = validate_int_input(
    range(1, len(buildingList)), "Invalid input",
    "Type the number of your destination here: ") 
  #Here we'd then put the destinations we receive, and see how they react. How, I'm not too sure.

def village_1():
  global minu_visits
  global stole_something
  global minu_mad
  global square_visits
  global balliya_coat
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
    range(1, 12), "Invalid input",
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
                      add_item("Minu's Amulet", "An amulet containing a mysterious healing power.")
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
                        add_item("Minu's Amulet", "An amulet containing the power to harm others.")
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
    VillageStore.getItems()
  elif snowball == 5:
    if quest_completion == False:
          clearConsole()
          print(DARK_RED + "TAILOR'S HOUSE" + DARK_RED)
          time.sleep(0.25)
          delay_print("The door is locked!")
          time.sleep(1)
          clearConsole()
          village_1()
    elif quest_completion == True:
          clearConsole()
          otis("TAILOR'S HOUSE")
          time.sleep(0.25)
          delay_print(WHITE + "You fiddle with the doorknob and the door squeaks open, scuffing the dirt floor." + WHITE)
          delay_print("The inside of the house is filthy. Do you still want to go in?")
    pass
  elif snowball == 6:
    #Old Lady's House
    pass
  elif snowball == 7:
    if quest_completion == False:
          clearConsole()
          print(DARK_RED + "APOTHECARY" + DARK_RED)
          time.sleep(0.25)
          delay_print("The door is locked!")
          time.sleep(1)
          clearConsole()
          village_1()
    elif quest_completion == True:
          clearConsole()
          print(DARK_RED + "APOTHECARY" + DARK_RED)
          time.sleep(0.25)
          delay_print("The door squeaks open.")
  elif snowball == 8:
    #Church
    pass
  elif snowball == 9:
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
          delay_print(WHITE + """
            The town square is a bustling place, even in overcast weather. Then again, today is market day, so the people are buying goods.
            Still, it feels vaguely like a holiday. The square is decorated with banners, and everyone seems cheerful.
            You turn to Kosu and ask, "Is today a holiday?"
            Kosu shrugs. "I'm not sure. They taught us more about where things are than what people do."
            Still curious, you ask someone selling scarves, "Excuse me, is today a holiday?"
            He smiles. "Not before," he says, "but who knows about the future?" He winks at you before returning to his hawking.
          """, indent=12)
        elif square_visits == 1:
          delay_print(WHITE + """
            Kosu says, "I'm going to ask the locals about the surrounding area."
            You tell him, "Okay, don't get into trouble."
            Kosu nods. "Of course! I'll stay in the town square."

            You look around slightly uncertainly.
            "Hello!"
            You turn towards the voice. It's the scarf seller from earlier!
            "Excuse me, but where're you from? Your coat looks a little different," he asks.
            Slightly surprised, you answer, "From the mountains."
            "Hm. It looks a bit thick."
            You shrug. "It's very comfortable."
            He nods. "I can see that. But let me know if you want a thinner coat. My name's Balliya, by the way."
          """, indent=12)
          get_coat = yes_no(False, "Please choose again.", "Do you accept Balliya's offer? ")
          balliya_coat = (get_coat == "Y") or (get_coat == "YES")
          delay_print(WHITE + """
            "Okay, then. See you later!"
          """, indent=12)
        elif square_visits == 2:
          delay_print(WHITE + """
            "Hi, Esteri!"
            You wave back. "Hello... Balliya, right?"
          """, indent=12)
          if balliya_coat:
            delay_print(WHITE + """
              "Here's the coat my wife made for you. Hope you like it!"
            """, indent=14)
            add_item("Coat from Balliya", "A lighter coat Balliya's wife made for you.")

        if square_visits <= 3: #3 is placeholder max number of unique events
          square_visits += 1
  elif snowball == 10:
    if quest_completion == False:
        clearConsole()
        print(DARK_RED + "SERVANT'S QUARTERS" + DARK_RED)
        time.sleep(0.25)
        delay_print("The door is locked!")
        time.sleep(1)
        clearConsole()
        village_1()
    elif quest_completion == True:
        clearConsole()
        print(DARK_RED + "SERVANT'S QUARTERS" + DARK_RED)
        time.sleep(0.25)
        delay_print(WHITE + "You open the door and step down onto the rough dirt floor, stumbling a little." + WHITE)
  elif snowball == 11:
    pass
  elif snowball == 12:
    if quest_completion == False:
      delay_print("Sorry, but you can't access this area yet. Please try again.")
      village_1()
    else:
      pass

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
    "And as the fire consumed her, there was no pain, not anymore. It was the moment when the ice numbs your hands and the pain fades, down to the shivers of cold, now the tremors of death. And Amaliya\'s mind wandered, to the forest, to the city, to the mountains, to her village in the valley and the daughter she left behind."
  )
  clearConsole()
  time.sleep(0.5)
  delay_print("Esteri.", speed=0.01)
  time.sleep(0.5)
  clearConsole()
  pygame.quit()

#MUSIC
source = audio.play_file('files/sound/EsteriTheme.mp3')
source.volume += 0.01
clearConsole()
# adventureBeg()
welcome()

delay_print("You are lying on a cold rock.")
delay_print("You shove one arm out frantically, then retract it rapidly as you start sliding forward.")
delay_print("The surface is as smooth and chilly as ice, yet as black as obsidian. It refuses to give you grip.")
delay_print("Vision swimming, you struggle to stand up, pushing yourself even farther forward.")
delay_print("At last, you succeed.")
delay_print("The cave around you sparkles with tens of thousands of tiny pinpricks of light.")
delay_print("It's a surreal image to behold, but it produces a considerable strain on your eyes.")
delay_print("You only have a second to register when you see the dark silhouette that stands in front of you, buzzing with the same odd sound.")
cave_battle_1 = Battle([Esteri], [Dronae.copy()], "cave", "Suddenly, it leaps out at you!", "dronae")
cave_battle_1.begin()
time.sleep(1)
clearConsole()
delay_print("You stumble away from the monster's carcass, disoriented.")
delay_print("Esteri…")
delay_print("A low rumble echoes through the cave.")
delay_print("Esteri… you have not proven your worth…")
delay_print("You spin around, scrabbling to direct your rotation.")
delay_print("Before you can run, though, the walls reform around you. There are two openings in front of you, but they are guarded by a short, dragon-like figure.")
delay_print("The Dronae… will test you.")
delay_print("The short monster- the Dronae- buzzes.")
delay_print("If you can answer their questions correctly, you shall reach the end of the tunnel with no issue.")
delay_print("You stare down the Dronae.")
delay_print("But if you answer wrong… you will never be able to make it.")
delay_print("The wall lights glow brighter, as if to taunt you.")
delay_print("Oh, and one last warning: I'd suggest that you locate your friend soon- or he may be gone forever.")
delay_print("A low ringing hums through your ears, then a whistle of air as the voice floats away.")
time.sleep(1)
clearConsole()
delay_print("'Well,' the Dronae buzzes, 'you're the type to bow to your superiors, aren't you?'")
dronae_question_1 = validate_input(["y", "yes", "n", "no"], "Invalid input").lower()
if dronae_question_1 == "y" or dronae_question_1 == "yes":
    delay_print("'Good,' the Dronae buzzes. 'You may pass… via the left, in recognition of your deference.'")
    delay_print("Will you heed its instruction, or will you choose the other path?")
    delay_print(" 1. Left")
    delay_print(" 2. Right")
    dronae_path_1 = validate_input(["1", "2"], "The Dronae is beginning to look agonized… You'd better heed its instruction…").lower()
    if dronae_path_1 == "1":
      delay_print("The Dronae looks satisfied. You turn and walk down the path to the left.")
    if dronae_path_1 == "2":
        cave_battle_2 = Battle([Esteri], [Dronae.copy()], "cave", "The Dronae jumps at you in fury!", "dronae")
        cave_battle_2.begin()
        delay_print("The Dronae lies on the ground, bleeding. 'Continue…' it coughs, suddenly appearing pitiful due to the blood that saturates its muzzle. 'You have proven yourself worthy.'")
        delay_print("It fades, dissolving into the air with transience.")
if dronae_question_1 == "n" or dronae_question_1 == "no":
    cave_battle_2 = Battle([Esteri], [Dronae.copy()], "cave", "'Wrong answer!' The Dronae leaps at you, claws outstretched.", "dronae")
    cave_battle_2.begin()
    delay_print("The Dronae lies on the ground, bleeding. 'Continue…' it coughs, suddenly appearing pitiful due to the blood that saturates its muzzle. 'You have proven yourself worthy.'")
    delay_print("It fades, dissolving into the air with transience.")
    delay_print("Which way will you go?")
    delay_print(" 1. Left")
    delay_print(" 2. Right")
    dronae_path_1 = validate_input(["1", "2"], "You'd better choose quickly… Kosu is in danger…").lower()
if dronae_path_1 == "1":
    loading_effect()
    clearConsole()
    delay_print("You stumble into another lighted cavern. This one is lined with fluorescent mushrooms like the ones you saw above. The floor is woven with roots.")
    delay_print("'Esteri!' Kosu's voice rings off the walls.")
    delay_print("Your eyes adjust, and you gasp.")
    delay_print("Your friend is ensnared in a tangle of vines, wrapping around him in an intricate pattern and constricting quickly.")
    delay_print("Yet again, a Dronae stands guard in front of the structure.")
    cave_battle_3 = Battle([Esteri], [Dronae.copy()], "cave", "This one doesn't even make a noise before it launches itself at you.", "dronae")
    cave_battle_3.begin()
    delay_print("When the Dronae fades this time, the vines disappear. Kosu drops to the ground with a light thud.")
    delay_print("You rush over to him.")
    delay_print("What will you say?")
    delay_print(" 1. Are you okay?")
    delay_print(" 2. Let's go!")
    validate_input(["1", "2"], "Kosu looks up at you impatiently.").lower()
    delay_print("Kosu gets up slowly and dusts himself off. 'Yeah,' he says, forcing a smile. 'Let's go!'")
    delay_print("Without waiting for further comment, you grab his wrist and pull him towards the exit to the cavern.")
    delay_print("But you are stopped by another pair of Dronae, which jump in front of you, buzzing with impertinent fury.")
    cave_battle_4 = Battle([Esteri, Kosu], [Dronae.copy(), Dronae.copy()], "cave", "They swipe a claw at your face in synchrony!", "dronae")
    cave_battle_4.begin()
if dronae_path_1 == "2":
      loading_effect()
      clearConsole()
      delay_print("You stumble through the darkness, trying to feel for a wall.")
      delay_print("Your stomach fills with painful regret as you realize that you should have gone in the other direction.")
      delay_print("You can see nothing around you but endless black, swallowing the air and suffocating you.")
      delay_print("You trudge forward one more step and then trip, heavy with exhaustion.")
      delay_print("A Dronae looms above you. 'I'm not very happy, you know,' it buzzes. 'You dissolved my friends before the Turning Ceremony.'")
      delay_print("What will you say?")
      delay_print(" 1. What's the Turning Ceremony?")
      delay_print(" 2. Explain what's going on!")
      validate_input(["1", "2"], "Answer now! The Dronae looks agitated…").lower()
      time.sleep(1)
      clearConsole()
      delay_print("The Dronae groans. 'Of course I can't tell you that, impertinent child.'")
      delay_print("It looks over you. 'But…' It turns away, looking slightly embarrassed. 'Maybe I can heal you.'")
      delay_print("It climbs onto your stomach, and begins to mutter a few incantations.")
      delay_print("The Dronae's paws glow. You suddenly feel replenished.")
      Esteri.dealDamage(-100)
      delay_print("It scampers off your stomach and glares up at you as you sit up slowly, stretching your arms with new vigorousness.") 
      delay_print("You stare at it as it scratches the floor, looking more and more agonized.")
      delay_print("What will you say?")
      delay_print(" 1. What are you doing?")
      delay_print(" 2. Can I go now?")
      validate_input(["1", "2"], "The Dronae keeps scratching.").lower()
      delay_print("The Dronae looks up at you with surprising ferocity. 'You know, I think I might want to help you,' it says.")
      delay_print("You flinch, taken aback.")
      delay_print("'You see, I am a very helpful Dronae,' it says, puffing up its chest. 'If you keep me alive, I can help you in fights.'")
      delay_print("You burst out laughing and smile.")
      delay_print("What will you say?")
      delay_print(" 1. Yeah, you can come!")
      delay_print(" 2. No… I would rather go on my own.")
      dronae_add_to_team = validate_input(["1", "2"], "The Dronae scrapes your arm affectionately, waiting for an answer.").lower()
      if dronae_add_to_team == "1":
        delay_print("The Dronae sighs in relief. 'I won't let you down!'")
        cave_battle_3 = Battle([Esteri, Dronae], [Dronae.copy(), Dronae.copy()], "cave", "These ones don't even make a noise before they launch themselves at you.", "dronae")
        cave_battle_3.begin()
      if dronae_add_to_team == "2":
        pass
