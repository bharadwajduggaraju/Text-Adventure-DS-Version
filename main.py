#Import Libraries
import sys
import time
import os
import random
import pygame
from replit import audio

from fighting.battle import Battle
from adventures.shop import Shop
from util.colors import *
from util.variables import *
from util.variables import party_money, add_party_member, add_item
from util.instances import *
from util.console.output import delay_print, loading_effect, clearConsole
from util.console.input import validate_input, validate_int_input, yes_no, tutorial, inventorymenu, settings, battle_tutorial
from adventures.trade import *
from adventures.trade import Trade

add_party_member(Amaliyah)

STARTING_MONEY = 100

#Shop

shopItems = [{"name": "scarf", "price": 33, "quantity": 2200}]
shopStats = [{
  "name": "scarf",
  "totalMoney": 0,
  "unitsSold": 0,
  "discount": False
}]

WinterShop = Shop("Arctic Circle", shopItems, shopStats)

WinterShop.getInfo(STARTING_MONEY)

#Trade

# tradeItems = [{"name": "Scarf", "itemsAccepted": ["boot", "shoe", "helmet"]}]

# #Inventory, make dynamic later
# playerInventory = ["boot", "shoe", "helmet", "sock"]

# Winter_Trading_Post = Trade("Winter", tradeItems)

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

#GAME CODE - Introduction
def introduction():
  delay_print("""
    Amaliyah scampered through the trees, ducking and doging low-handing branches and sliding over the slick leaves scattered on the ground.
    The air was musty with the smell of petrichor as rain dibbled down around her, wetting the soil and leading it to convalesce into a muddy slush.

    Breath ragged, she tore down the badly marked forest path.
    Her footsteps pounded with urgency.
    In the distance, howls rang through the air- the distinct call of a pack of Kirin that had caught the smell of fresh meat.
    Her chest seized as she thought of the bloodthirsty expressions etched on each of their psychopathic wolfish faces, foreboding masks of doom.
  """, end="", indent=4)
  time.sleep(1)
  clearConsole()
  delay_print("""
    Amaliyah gripped her sword tightly in one sweaty hand and her shield in the other.
    Her eyes widened instinctively with fear as she rounded the corner and saw the Clearing of the Kirin awaiting her arrival.
    Feet smashing leaves into pulp as she fled across the packed dirt, she wildly attempted to escape from the circular gap in the trees.
  """, end="", indent=4)
  time.sleep(1)
  delay_print("""
    But the Kirin were not so easily tricked.
    A magical barrier shot up, twinkling with light and blocking her path.
    She knelt on the ground, catching her breath.
    The clearing was still, with the exception of a few stray leaves that twirled through the air and gently came to a rest on the grass.
    Trees waved about in a leisurely fashion, flaunting the autumn leaves dangling from their branches and burning with the colors of flame.
  """, end="", indent=4)
  time.sleep(1)
  clearConsole()
  delay_print("""
    Strained now, Amaliyah forced herself to stand up, drawing her sword from its scabbard with a steely hiss.
    Assuming a confident fighting stance, she whipped her blade behind her suddenly as a rustle sounded in the grass.
    Nothing.
    Amaliyah gripped the hilt of her sword harder, nerves taut.
    Jarring howls pierced through the still air.
  """, end="", indent=4)
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

  answer = validate_input([], "", prompt="Press s to skip the intro. Press b just to play the intro battle. Else, press any key to start playing: ", validate=False).lower()

  clearConsole()

  if (answer != "s"):
    if (answer != "b"):
      introduction()
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
#source = audio.play_file('files/sound/EsteriTheme.mp3')
#source.volume += 0.01
#clearConsole()

def adventureBeg():
  global party_money
  delay_print("""
    The voice of the chaplain rings out in sonorous tones across the hall. "Esteri. Today, you are come of age, and eligible to ascend the throne. As it has been for the many centuries..."
    The chaplain drones on as you kneel on the flagstones, watching the play of candlelight on the polished rock. Slowly, the chaplain's voice drones to a close.
    "In the absence of the Chieftess Amaliyah, and with no kinswomen to anoint you, I hereby pronounce you a noble citizen of the Confederacy of Elyria." You rise, turning to face the assembled servants and courtiers with a graceful curtsy as the first rays of sunrise burst over the highest peak.
    Beneath you, the capital unfolds in the light, with its stone causeways swooping over the lake and from the mountains. You remain there as the hall slowly empties, despite the cold.
    A servant approaches, carrying a small bowl and a missive.
    "Lady Esteri, this missive from Regent Avivaki. She requests your presence."
    You nod, scanning the parchment. "I will be there."
    The servant shakes her head. "I was also told to relay a second message, from Kosugadde. Er..." The servant shrugs. "He says, 'But first, you should eat your breakfast!'"
    A few minutes later, you strap your spear to your back, don your breastplate over your tunic, adjust your hair to look mildly presentable, push a bag over your shoulders, and quickly walk out of your chambers. The regent is waiting for you!
  """, end="", indent=4)
  time.sleep(1)
  clearConsole()
  delay_print("""
    You dash through the streets, veering wildly around the small stone huts that characterize your village, your spear clanking rhythmically on your back. Smoke floats leisurely out of the chimneys, and all around you can hear the sound of the village waking up as the sun begins to rise over the peaks of the snow-capped mountains.
    
    Your eyes land on a pair of stately doors with ornate staffs carved deep into the wood. You have found the regent's residence!
  """, indent=4)

  option = yes_no(False, "You must decide.", "Do you want to go inside?\n")
  while (option != "YES") and (option != "Y"):
    delay_print(
      "Your aunt will be mad if you don't go..."
    )
    option = yes_no(False, "You must decide.", "Do you want to go inside?\n")

  delay_print("""
    You walk towards the door and are stopped by two guards.

    "Excuse me, miss. You're not allowed here without permission."
    "Don't you know who I am?" You raise an eyebrow with some annoyance.
    The guards look at each other, blank-faced, before one of them blinks and winces. "Oh dear- Apologies, Lady Esteri. Please come inside. The village regent has been waiting for you." The guards bow and step aside.
  """, indent=4)
  loading_effect()

  delay_print("""
    You enter a warm, brightly lit room with ancient scripts pierced onto paintings on the walls. In the middle of the room reclines an aging woman draped with beaded necklaces and a thick woolen coat.
    "Please, sit down. We have much to discuss, young one.
    "I possess information about your mother, Amaliyah." Village Regent Avivaki meets your eyees with a solmen expression.
    Eager to gain knowledge on your mother, you quickly take a seat and listen.
    "We have reasons to believe that your mother, Chieftess Amaliyah, may in fact be alive. Your mother was sent on a mission to find new land for the people of Elyria, and it seems that she has not returned.
    "However, as her descendant, the day has come for the task to be bestowed upon you. As the true future Chieftess of Elyria, and my successor, you must embark on this quest to find your mother and complete her mission.
    "Can we trust you to complete this task with honor?" Her expression is questioning.
  """, indent=4)

  option = yes_no(allow_maybe=True, errMessage="You need to give her a clear answer. She's the chief!")
  if (option == 'MAYBE' or option == 'POSSIBLY'):
    delay_print(
      "\"Maybe? That is no way to answer a question from your regent!\""
    )
    option = yes_no(False, "You need to decide now.")

  if (option == 'NO' or option == 'N'):
    delay_print(
      "\"Then maybe I have overestimated your abilities. If you do wish to change your mind, please come back later. Elyria is counting on you.\""
    )
    option = yes_no(
      False, "You have one last chance = change your mind. Decide quickly.")
    if (option == 'NO' or option == 'N'):
      delay_print(
        "The pressure is way too much right now. And you're only 18! Maybe you could try again later when you're more prepared."
      )
      sys.exit()

  delay_print("""
    "That's excellent!" The village head smiles, mouth stretching upwards into a grimace of a smile. "I knew that our people could count on you, Esteri.
    "You'll require a naviagator for your journey, so I've select one of our skilled navigators-in-training to assist you."
    The village head frowns. "But he appears to be a bit late..."
  """, indent=4)
  delay_print()
  time.sleep(1)
  clearConsole()
  delay_print("""
    The door bursts open and a young man with an unruly mop of brown hair bursts in.
    The new arrival wipes sweat off of his brow, glancing up at the village head with a sheepish expression.
    The village head glares down at him in indignation. "You're late."

    Your eyes widen as you recognize the man as your old friend, stumbling into a chair with drunken movements.
    "Kosu, is that you?" You look at him with a wondrous expression.

    "Hey, Esteri!" Kosu grins. "It's been a few years, hasn't it? Nice to see you! I guess you're finally going-"
  """, indent=4)
  time.sleep(0.25)
  option = yes_no(
    False, "You need to decide quickly...",
    "Do you interrupt Kosu in order to preserve your dignity? ").lower()

  if option == "y" or option == "yes":
    delay_print("""
      You shoot Kosu a warning glance and he quiets, remorseful. Then you turn to face the village regent.
      Her expression is haughty.
      Choose what you would like to say to the village head.
      1. "Apologies, ma'am."
      2. "Kosu and I are friends- you can hardly begrudge us the chance to enjoy our reunion."
      Enter the number of the answer you prefer.
    """, indent=6)

    option = validate_input(['1', '2'], "Decide now! She's the chief!").lower()
    if option == "1":
      delay_print("""
        "You're forgive," the village leader says with an air of superiority. "But don't forget your manners in the future."
        You bite your tongue to hold back further remarks.
      """, indent=8)
    elif option == "2":
      delay_print("""
        The village leader sniffs in indignation. "I am a very busy woman. Please enjoy your reunion when you are no longer in my presence."
        You bite your tongue to hold back further remarks.
      """, indent=8)
    delay_print(
      "Kosu pipes up. 'Is there anything else that we need to know before leaving?'"
    )
  else:
    delay_print("""
      "-get to search for your mom as you've wanted all these years," Kosu finishes.
      Your cheeks flush with embarrassment. "Yes," you mutter, and then turn back to face the village leader.
      The village leader smriks pridefully. "What adorable youthful enthusiasm."
      Kosu shrinks back. "Is there anything else we need to know before leaving?" he asks quietly.
    """, indent=6)
  delay_print("""
    The village regent folds her hands. "The path will be dangerous," she warns, and her face softens a little. "You really don't have to complete this journey if you are afraid."
    Kosu shakes his head in indignation. "We aren't quitters,", he says, voice spiking with an undertone of determination. "Esteri and I will be fine."
    You stare at the regent for a second longer, but her stoic face doesn't shift.
    "Kosu's right," you finally assent, voice commanding. "We will be fine."
  """, indent=4)
  time.sleep(1)
  clearConsole()
  delay_print("""
    Regent Aviveki smiles. "Wonderful," she says. "I'll instruct you on where to go."
    Taking a map from beside her chair, she rolls it out on the table. "This," she instructs, "is the continent of Suto Ratak. Here-" she points at a wide parcel of land- "is Elyria."
    She runs her finger along the waxed paper to a large brown spot on the map, split into four quadrants. "This is Rakunto Ke'koate'nan. It's the largest city in Suto Ratak. It's also your target destination."
    She moves her finger to a spot on the map closer to your village. "Here is a small village known as Ai'ko Le'po Koate'nan. An old friend of your mother's resides here. You will begin by traveling to this village, in the hopes that your mother's friend can offer you advice or assistance."
    She pulls a letter out of her desk and sets it in front of you. "Deliver this letter to an old woman by the name of Kurigalu. She should be willing to help you find your mother. At the very least, she'll find you someone who can aid you on your journey. You will also be given given 100 nagara scrip to begin your journey."

    The regent stands up, leaving the letter on the desk in front of you. She meets your eyes.
    "Your mother was a friend of mine," she murmurs, more to herself than you. "I hope that you can bring her back."
    She turns, and you watch her retreating back, unable to wipe the sight of Regent Aviveki's regretful, resigned expression from your mind.
    Any annoyance you felt towards her during your encounter fades.
    Kosu reaches out and picks up the letter. He handsit to you. "I believe this belongs to you."
    You take the letter and place it in your bag.
  """, indent=4)
  add_item("Letter for Kurigalu", "An important letter from the regent.")
  party_money = 100
  time.sleep(1)
  tutorial()
  inventorymenu()
  settings()
  delay_print("""
    "We should go," you tell Kosu, voice quavering slightly with a near-undetectable hint of fear.
    He nods. "If we don't leave within the hour, we won't make it to Ai'ko Le'po before nightfall."
    You rest your hand on the doorknob. Your mind wanders for a second.
  """, indent=4)
  time.sleep(0.25)
  delay_print(
    "You wonder how your mother felt when she was setting out on her journey.")
  time.sleep(1)
  clearConsole()
  delay_print(GREY_ITALIC + """
    Mother kneels down, caressing your cheek. "I'll be back soon, Esi," she whispers, smiling at you.
    "Are you scared, Mommy?" You look up at her, cheeks wet with tears.
    Mother wrings her hands. She stares up at the ceiling, watching the warm light from the lanterns flicker. "No," she finally says, a tremor in her voice. "Dai'ra, Esi. I will be strong for Elyria."
    "Yes mommy, I know you are never scared of anything."
    She stands up. "There's nothing wrong with having fears, Esi," she says, touching your cheek. "Real bravery is when you're scared, but push through anyway." She smiles, but her eyes are sad. "Can you promise to be brave for me?" You nod, looking up at her.
    "Goodbye, Mommy," you whisper, wrapping your arms around her leg. "Come back soon, okay?"
    She looks down at you as if drinking in your appearance one last time. "I will, Esi. I promise."
    
  """, indent=4)
  time.sleep(0.5)
  delay_print("""
    Amaliyah walked to the door. Hand shaking, she placed her hand on the knob... and glanced back one last time, meeting Esteri's eyes and mustering a smile.
  """, indent=4)
  time.sleep(0.5)
  clearConsole()
  delay_print("She opened the door." + RESET)
  time.sleep(1)
  clearConsole()
  delay_print("""
    You step out into the blinding sunshine, holding a hand up to shield your eyes.
    Light reflects off the snow surrounding you, casting your village in a slight eerie glow.
    "Ai'ko Le'po is to the southeast," Kosu observes, holding up the map.
    You look at him, somewhat solemn. "You know she was right, Kosu? We could die on this mission."
    Kosu grins at you. "We don't die," he says, unwavering. "After all, we're the best team in all of Elyria."
    You raise your eyebrows. "Is that so?"
    The two of you laugh and banter as you amble down the rocky foothill, traveling the same path that your mother had followed so many years earlier.
  """, indent=4)
  time.sleep(0.25)
  clearConsole()
  loading_effect()
  time.sleep(0.25)
  delay_print("""
    You slog along, grouchy, with branches snapping under your feet.
    "Are we almost there?" you ask Kosu, with an expression of consternation. "The woods don't seem to end anytimesoon."
    Kosu studies his map. "Yeah," he assures you. "We'll arrive in the village any minute now."
    Seconds later, the two of you break through the edge of the forest.
    The trees have been cleared unevenly from a patch of roughly packed land, lined with small huts that creak under the weight of the sky.
    "See?" Kosu points out. "I was right."
    You ignore him and step forward. "Something doesn't seem right."
    "Let's go look," Kosu says.
  """, indent=4)

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
    delay_print("This time, two Dronae stand guard before him.")
    cave_battle_3 = Battle([Esteri, Kosu], [Dronae.copy(), Dronae.copy()], "cave", "These ones don't even make a noise before they launches themselves at you.", "dronae")
    cave_battle_3.begin()
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
