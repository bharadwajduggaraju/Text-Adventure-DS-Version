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
from narrative.beginning import adventureBeg, amaliyahIntro
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
  delay_print("Please select which location you would like to visit.")
  num_options = 9
  # delay_print(" 1. Chief's House")
  delay_print(" 1. Noble House")
  delay_print(" 2. Carpenter's House")
  delay_print(" 3. Cobbler's House")
  delay_print(" 4. Tailor's House")
  delay_print(" 5. Old Lady's House")
  delay_print(" 6. Apothecary")
  delay_print(" 7. Church")
  delay_print(" 8. Town Square")
  # delay_print(" 10. Servants' Quarters")
  delay_print(" 9. Dark Forest")
  if quest_completion == True:
    delay_print(" 10. Bright Forest Path")
    num_options += 1
  snowball = validate_int_input(
    range(1, num_options+1), "Invalid input",
    "Type the number of your destination here: ")  #Limited to 1 through num_options
  if snowball == 1:
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
  elif snowball == 2:
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
              Esteri.setHP(Esteri.MaxHP)
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
                delay_print("Will you introduce yourself?")
                carpenter_daughter_response = validate_input(["yes", "y", "no", "n"],"Invalid input").lower()
                if carpenter_daughter_response == "yes" or carpenter_daughter_response == "y":
                  delay_print("'I'm Esteri,' you say, proud.")
                  delay_print("'Nice to meet you, Esteri!'")
                  delay_print("The girl bows slightly. 'My name is Minu.'")
                  delay_print("Her expression becomes one of trepidation. 'Can I trust you with a secret?'")
                  carpenter_daughter_secret = validate_input(["yes", "y", "no", "n"], "Invalid input").lower()
                  if carpenter_daughter_secret == "yes" or carpenter_daughter_response == "y":
                    delay_print("'Sure.' You lean forwards, curious.")
                    delay_print("She furtively flicks her gaze to her father.")
                    delay_print("'I'm afraid that my dad is disappointed that I'm not a carpenter,' she confesses.")
                    delay_print("She looks sheepish. 'I wish I could be a good carpenter, I really do. But I enjoy taking care of animals more.'")
                    delay_print("She looks down at her lap. 'Do you think he's mad at me?'")
                    carpenter_daughter_disappointed = validate_input(["yes", "y", "no", "n"], "Invalid input").lower()
                    if carpenter_daughter_disappointed == "no" or carpenter_daughter_disappointed == "n":
                      delay_print("'I think your dad loves you for who you are,' you say gently.")
                      delay_print("You think of your mother for a second before Minu's voice snaps you out of your thoughts.")
                      delay_print("'Thank you!' Minu's face brightens. 'That makes me feel a lot more confident.'")
                      delay_print("She looks down for a second.")
                      delay_print("'It's hard to find people to talk to here...' she murmurs.")
                      time.sleep(0.5)
                      delay_print("The moment of silence passes, and Minu smiles awkwardly.")
                      time.sleep(0.5)
                      delay_print("She holds out her palm. In it is a small purple stone, pusling with blue light.")
                      delay_print("She grins. 'I'd like you to have this as thanks.'")
                      delay_print("You take the amulet and slip it into your bag. 'Thank you! I'm glad I could help.'")
                      add_item("Minu's Amulet", "An amulet containing a mysterious healing power.")
                      minu_visits += 1
                      time.sleep(1)
                      clearConsole()
                      carpenterhouse()
                    if carpenter_daughter_disappointed == "no" or carpenter_daughter_disappointed == "n":
                      delay_print("'Oh...' Minu looks concerned. 'I suppose you're right. Thank you for your time, Esteri.'")
                      delay_print("She turns away, looking disheartened. You feel momentarily bad.")
                      delay_print("Then you notice a stone next to her plate, bright red and pulsing with fiery orange streaks.")
                      delay_print("Do you take it? You're torn: it could help you on your quest, but stealing is wrong.")
                      take_minus_amulet = validate_input(["yes", "y", "n", "no"], "Invalid input").lower()
                      if take_minus_amulet == "yes" or take_minus_amulet == "y":
                        delay_print("You sneak the stone into your bag. No one notices.")
                        add_item("Minu's Amulet", "An amulet containing the power to harm others.")
                        delay_print("You decide to sneak out of the carpenter's house before anyone can catch you.")
                        stole_something = True
                        minu_visits += 1
                        time.sleep(1)
                        clearConsole()
                        village_1()
                      if take_minus_amulet == "no" or take_minus_amulet == "n":
                        delay_print("You rescind your hand and smile stiffly.")
                        minu_visits += 1
                        time.sleep(1)
                        clearConsole()
                        carpenterhouse()
                  if carpenter_daughter_secret == "no" or carpenter_daughter_secret == "n":
                    delay_print("Minu smiles softly. 'That's all right. Maybe you can come back another time to hear my secret!'")
                    time.sleep(1)
                    clearConsole()
                    carpenterhouse()
                if carpenter_daughter_response == "2":
                  delay_print("'Oh. Sorry for mistaking you for the wrong person!' She looks uncomfortable.")
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
  elif snowball == 3:
    #Cobbler's House
    VillageStore.getItems()
  elif snowball == 4:
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
          enter_tailors_house = validate_input(["yes", "y", "no", "n"], "Invalid input").lower()
          if enter_tailors_house == "yes" or enter_tailors_house == "y":
            delay_print("You glance around. The room is full of raucous, partying men, heavily drunk.")
            delay_print("Who will you talk to?")
            delay_print(" 1. Tailor")
            delay_print(" 2. Cobbler")
            delay_print(" 3. Commoner")
            delay_print(" 4. Noble Young Man")
            delay_print(" 5. Exit")
            speak_to_in_tailors_house = validate_input(["1", "2", "3", "4", "5"], "Maybe you should just leave...")
            if speak_to_in_tailors_house == "1":
              delay_print("'Hello!' The tailor greets you with laughter. 'Would you like a drink, little girl?'")
          if enter_tailors_house == "no" or enter_tailors_house == "n":
            delay_print("You decide not to enter.")
            time.sleep(1)
            clearConsole()
            village_1()
  elif snowball == 5:
    if quest_completion == False:
          clearConsole()
          print(DARK_RED + "KURIGALU'S HOUSE" + DARK_RED)
          time.sleep(0.25)
          delay_print("The door is locked!")
          time.sleep(1)
          clearConsole()
          village_1()
    elif quest_completion == True:
          clearConsole()
          print(DARK_RED + "KURIGALU'S HOUSE" + DARK_RED)
          time.sleep(0.25)
          delay_print("You nudge the door open to reveal a cozy room.")
          delay_print("The floors, made of wood coated in faded stain, are soft and splintered after decades of wear.")
          delay_print("The room is in a peculiar octagonal shape, contrary to the rectangular design of many of the other cottages.")
          delay_print("In the center, by a smoldering chimney, an old lady sits in a hard wooden chair.")
          time.sleep(1)
          clearConsole()
          delay_print("She looks up at you, eyes crinkling in a smile. 'Hello, ahalan. I am Kurigalu, the matriarch of the village. What brings you here?'")
          delay_print("What will you say?")
          delay_print(" 1. I'm looking for my mother, Amaliyah. She went missing years ago.")
          delay_print(" 2. I'm Esteri of Elyria, and I am looking for information regarding the whereabouts of my mother.")
          esteri_talk_to_kurigalu_1 = validate_input(["1", "2"], "Kurigalu waits patiently for an answer.").lower()
          time.sleep(1)
          clearConsole()
          if esteri_talk_to_kurigalu_1 == "1":
            delay_print("'Ah, yes,' Kurigalu says, nodding her head in affirmation. 'You're Amaliyah's daughter. Esteri, correct?'")
            input("")
          if esteri_talk_to_kurigalu_1 == "2":
            delay_print("'Ah, yes,' Kurigalu says, nodding her head in affirmation. 'You're Amaliyah's daughter, correct?'")
            validate_input(["y", "yes"], "Don't lie!").lower()
          delay_print("Kurigalu inclines her head. 'I heard that Amaliyah died years ago.'")
          delay_print("What will you say?")
          delay_print(" 1. We're not sure. I'm hoping to find her.")
          delay_print(" 2. I don't think she died. That's why I'm looking for her.")
          esteri_talk_to_kurigalu_2 = validate_input(["1", "2"], "Kurigalu waits patiently for an answer.").lower()
          delay_print("Kurigalu inclines her head. 'Mmm.'")
          delay_print("Will you give Kurigalu the letter?")
          esteri_talk_to_kurigalu_3 = validate_input(["y", "yes"], "You'd better give the letter to her!").lower()
          time.sleep(1)
          clearConsole()
          delay_print("Kurigalu pores over the letter. 'Interesting...' she mumbles.")
          delay_print("She looks up after a few seconds of incoherent mumbling. 'Aviveki sent you?'")
          delay_print("No longer able to contain himself, Kosu nods. 'Yes.'")
          delay_print("Kurigalu frowns. 'Aviveki and I are not on the best of terms.'")
          delay_print("You wonder what she's talking about.")
          delay_print("Behind you, Kosu shifts nervously on his feet. 'We don't necessarily like her much either,' he lies, lacking conviction.")
          delay_print("'But we don't have much of a choice. We'd like to find Chief Amaliyah and restore her to her position.'")
          time.sleep(1)
          clearConsole()
          delay_print("Kurigalu folds the letter into a small square and drops it into the fire.")
          delay_print("She gives you a long, hard look, and sighs with exhaustion.")
          delay_print("'I'm an old lady,' she tells you. 'I no longer have as much energy as I did years ago. I can't offer you much help myself.'")
          delay_print("'On the other hand,' she continues, 'Amaliyah was one of my best students...'")
          delay_print("She meets your eyes. 'And you seem to take after your mother.'")
          time.sleep(1)
          clearConsole()
          delay_print("She pulls out a piece of aged charcoal and a sheet of pulpy wood paper.")
          delay_print("After spending a few seconds scribbling frantically in Oi'nan, she folds the letter and hands it to you.")
          delay_print("'Here,' she tells you. 'Take this letter to Nagara and find a man named Hukosu. He may be able to help you.'")
          delay_print("You nod.")
          delay_print("Kosu clears his throat. 'Do we have to go to Nagara?'")
          delay_print("He sounds uncharacteristically scared.")
          delay_print("Kurigalu looks up at him, expressio suddenly sharp. 'Yes,' she says slowly. 'You must go to Nagara.'")
  elif snowball == 5:
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
  elif snowball == 8:
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
  elif snowball == 9:
    village_1_dark_forest_quest_thing()
  elif snowball == 10:
    if quest_completion == False:
      delay_print("Sorry, but you can't access this area yet. Please try again.")
      village_1()
    else:
      pass
def village_1_dark_forest_quest_thing():
  delay_print("'C'mon, Esteri, let's go!' Kosu bounds down the forest path, bouncing gleefully.")
  delay_print("His eyes glimmer in the dim light, and for a second you feel a rush of affection for your friend.")
  delay_print("His innocent expression is full of boundless joy.")
  delay_print("What do you want to say?")
  delay_print(" 1. I won't let you get ahead of me!")
  delay_print(" 2. Slowdown, Kosu. The path could get dangerous ahead.")
  statement_cave_path = validate_input(["1", "2"], "You'd better say something! He's getting away!").lower()
  if statement_cave_path == "1":
    delay_print("Kosu grins. 'You can't even catch up!'")
    delay_print("He dodges through the trees and swerves out of sight.")
    delay_print("Now regretting your rash decision, you chase after him, stumbling over tree roots and trampling the packed dirt.")
    delay_print("The path turns into a clearing ahead of you, and you dash towards the gap in the trees, hoping that Kosu is okay.")
    delay_print("As you turn the corner, Kosu comes into view. He hasn't moved.")
    delay_print("'What'd you find?' you demand.")
    delay_print("Kosu holds up his hand. 'Shhhh...' he whispers. 'Look.'")
  elif statement_cave_path == "2":
    delay_print("Kosu halts and looks back at you with mild annoyance.")
    delay_print("'You can trust me, too,' he complains.")
    delay_print("You jog up to him. 'This is a team mission,' you decree without meeting his eyes. 'It will remain a team mission.'")
    delay_print("The two of you slowly amble along the path, a slight wedge of discomfort separating you.")
    time.sleep(1)
    delay_print("After a few minutes, the path turns sharply. The two of you turn to your left and gawk at the sight that unfolds before you.")
  time.sleep(0.5)
  clearConsole()
  delay_print("The clearing is full of glowing mushrooms, shimmering in every color imaginable.")
  delay_print("Pixies flutter about, glimmering faintly and sprinkling light across the leaf-strewn earth.")
  delay_print("Vines creep up the trees, leading into the branches and climbing into darkness.")
  delay_print("What will you say?")
  delay_print(" 1. This place is beautiful!")
  delay_print(" 2. Look at the light!")
  input("")
  delay_print("Kosu turns to face you, eyes unsettled. 'You don't hear it?'")
  delay_print("The two of you fall into a dead silence. Your ears strain.")
  delay_print("A soft buzzing flows out of the silence, steady and rhythmic as the volume climbs.")
  delay_print("Kosu grabs your arm frantically. 'Something is really wrong with this place!'")
  delay_print("You drag him towards the entrance to the clearing, but you can no longer find it; in fact, the trees seem to be spinning around you, rotating at an immeasurable speed.")
  delay_print("Only one thing in the clearing remains immobile; a small rock, situated in the dead center.")
  delay_print("Do you want to pick up the rock?")
  validate_input(["y", "yes"], "'Come on, Esteri! Pick up that rock!' Kosu complains.")
  clearConsole()
  delay_print("As soon as you lift the rock, an outcropping of stalactites shoots upwards, forming the shape of a lion's muzzle.")
  delay_print("The lion's gaping maw beckons, tunneling down into the pitch-black underground.")
  delay_print("Kosu shoves past you. 'I'll go first,' he yells over the din. Before you can react, he jumps into the hole.")
  delay_print("After one more second of hesitation, you leap after him into the abyss.")
  time.sleep(1)
  clearConsole()
  delay_print("One second passes as you shoot downwards...")
  time.sleep(1)
  delay_print("... then another.")
  time.sleep(1)
  delay_print("You hear the wind whistling through your ears, and ever-so-suddenly, your eyes register the ground rushing up to meet you.")
  delay_print("There is no Kosu- only hard, spiky rock.")
  time.sleep(1)
  delay_print("You inhale and exhale, terror spiking your adrenaline, and then attempt to grab a stalactite.")
  time.sleep(1)
  delay_print("But your hands slip, and you continue to fall.")
  time.sleep(1)
  delay_print("After a brief pause, you start to scream. Agony rings in your ears as you curse your mother, your village, and Kosu for bringing this awful fate upon you.")
  time.sleep(1)
  delay_print("A gust of warm air washes over you, and suddenly you feel your body being carried backwards.")
  time.sleep(1)
  delay_print("Your light-headedness takes over as you try frantically to hold onto consciousness, but the effort is futile...")
  time.sleep(1)
  delay_print("As you shoot over a dark lake, dimly registering the tiny arms that now grip your shirt, you pass out.")
  time.sleep(1)
  clearConsole()
  loading_effect()
  delay_print("You are lying on a cold rock.")
  delay_print("You shove one arm out frantically, then retract it rapidly as you start sliding forward.")
  delay_print("The surface is as smooth and chilly as ice, yet as black as obsidian. It refuses to give you grip.")
  delay_print("Vision swimming, you struggle to stand up, pushing yourself even farther forward.")
  delay_print("At last, you succeed.")
  delay_print("The cave around you sparkles with tens of thousands of tiny pinpricks of light.")
  delay_print("It's a surreal image to behold, but it produces a considerable strain on your eyes.")
  delay_print("You only have a second to register when you see the dark silhouette that stands in front of you, buzzing with the same odd sound.")
  time.sleep(1)
  clearConsole()
  cave_battle_1 = Battle([Esteri], [Dronae.copy()], "cave", "Suddenly, it leaps out at you!", "dronae")
  cave_battle_1.begin()
  time.sleep(1)
  clearConsole()
  delay_print("You stumble away from the monster's carcass, disoriented.")
  delay_print(WHITE_ITALIC + "Esteri..." + WHITE_ITALIC)
  delay_print(WHITE + "A low rumble echoes through the cave." + WHITE)
  delay_print(WHITE_ITALIC + "Esteri... you have not proven your worth..." + WHITE_ITALIC)
  delay_print(WHITE + "You spin around, scrabbling to direct your rotation." + WHITE)
  delay_print(WHITE + "Before you can run, though, the walls reform around you. There are two openings in front of you, but they are guarded by a short, dragon-like figure." + WHITE)
  delay_print(WHITE_ITALIC + "The Dronae... will test you." + WHITE_ITALIC)
  delay_print(WHITE + "The short monster- the Dronae- buzzes." + WHITE)
  delay_print(WHITE_ITALIC + "If you can answer their questions correctly, you shall reach the end of the tunnel with no issue." + WHITE_ITALIC)
  delay_print(WHITE + "You stare down the Dronae." + WHITE)
  delay_print(WHITE_ITALIC + "But if you answer wrong... you will never be able to make it." + WHITE_ITALIC)
  delay_print(WHITE + "The wall lights glow brighter, as if to taunt you." + WHITE)
  delay_print(WHITE_ITALIC + "Oh, and one last warning: I'd suggest that you locate your friend soon- or he may be gone forever." + WHITE_ITALIC)
  delay_print(WHITE + "A low ringing hums through your ears, then a whistle of air as the voice floats away."+ WHITE)
  time.sleep(1)
  clearConsole()
  delay_print("'Well,' the Dronae buzzes, 'you're the type to bow to your superiors, aren't you?'")
  dronae_question_1 = validate_input(["y", "yes", "n", "no"], "Invalid input").lower()
  if dronae_question_1 == "y" or dronae_question_1 == "yes":
    delay_print("'Good,' the Dronae buzzes. 'You may pass... via the left, in recognition of your deference.'")
    delay_print("Will you heed its instruction, or will you choose the other path?")
    delay_print(" 1. Left")
    delay_print(" 2. Right")
    dronae_path_1 = validate_input(["1", "2"], "The Dronae is beginning to look agonized... You'd better heed its instruction...").lower()
    if dronae_path_1 == "1":
      delay_print("The Dronae looks satisfied. You turn and walk down the path to the left.")
    elif dronae_path_1 == "2":
      time.sleep(1)
      clearConsole()
      cave_battle_2 = Battle([Esteri], [Dronae.copy()], "cave", "The Dronae jumps at you in fury!", "dronae")
      cave_battle_2.begin()
      delay_print("The Dronae lies on the ground, bleeding. 'Continue...' it coughs, suddenly appearing pitiful due to the blood that saturates its muzzle. 'You have proven yourself worthy.'")
      delay_print("It fades, dissolving into the air with transience.")
  elif dronae_question_1 == "n" or dronae_question_1 == "no":
    time.sleep(1)
    clearConsole()
    cave_battle_2 = Battle([Esteri], [Dronae.copy()], "cave", "'Wrong answer!' The Dronae leaps at you, claws outstretched.", "dronae")
    cave_battle_2.begin()
    delay_print("The Dronae lies on the ground, bleeding. 'Continue...' it coughs, suddenly appearing pitiful due to the blood that saturates its muzzle. 'You have proven yourself worthy.'")
    delay_print("It fades, dissolving into the air with transience.")
    delay_print("Which way will you go?")
    delay_print(" 1. Left")
    delay_print(" 2. Right")
    dronae_path_1 = validate_input(["1", "2"], "You'd better choose quickly... Kosu is in danger...").lower()
  if dronae_path_1 == "1":
    loading_effect()
    clearConsole()
    delay_print("You stumble into another lighted cavern. This one is lined with fluorescent mushrooms like the ones you saw above. The floor is woven with roots.")
    delay_print("'Esteri!' Kosu's voice rings off the walls.")
    delay_print("Your eyes adjust, and you gasp.")
    delay_print("Your friend is ensnared in a tangle of vines, wrapping around him in an intricate pattern and constricting quickly.")
    delay_print("Yet again, a Dronae stands guard in front of the structure.")
    time.sleep(1)
    clearConsole()
    cave_battle_3 = Battle([Esteri], [Dronae.copy()], "cave", "This one doesn't even make a noise before it launches itself at you.", "dronae")
    cave_battle_3.begin()
    delay_print("When the Dronae fades this time, the vines disappear. Kosu drops to the ground with a light thud.")
    delay_print("You rush over to him.")
    delay_print("What will you say?")
    delay_print(" 1. Are you okay?")
    delay_print(" 2. Let's go!")
    validate_input(["1", "2"], "Kosu looks up at you impatiently.").lower()
    delay_print("Kosu gets up slowly and dusts himself off. 'Yeah,' he says, forcing a smile. 'Let's go!'")
    delay_print("Without waiting for further comment,you grab his wrist and pull him towards the exit to the cavern.")
    delay_print("But you are stopped by another pair of Dronae, which jump in front of you, buzzing with impertinent fury.")
    time.sleep(1)
    clearConsole()
    cave_battle_4 = Battle([Esteri, Kosu], [Dronae.copy(), Dronae.copy()], "cave", "They swipe a claw at your face in synchrony!", "dronae")
    cave_battle_4.begin()
    delay_print("When the Dronae fall, a voice echoes through the cavern.")
    time.sleep(1)
    clearConsole()
    delay_print(WHITE_ITALIC + "Esteri..." + WHITE_ITALIC)
    delay_print(WHITE + "Kosu turns frantically, searching for its source. 'What is that?!'" + WHITE)
    delay_print(WHITE_ITALIC + "You have not yet won..." + WHITE_ITALIC)
    delay_print(WHITE + "You begin to furiously walk towards the exit. Kosu follows you." + WHITE)
    delay_print(WHITE_ITALIC + "I look forward to seeing you..." + WHITE_ITALIC)
    delay_print(WHITE + "You freeze." + WHITE)
    delay_print("The voice fades away with a low whine.")
    time.sleep(1)
    clearConsole()
    delay_print("Now Kosu grabs your arm and begins to tug you along.")
    delay_print("'I don't know what that was, but we don't have time to worry about it,' he whispers, then winces. You notice that he's limping.")
    delay_print("You wrap your arm around Kosu's shoulders to help support him, and the two of you slowly stumble through the door.")
    time.sleep(1)
    clearConsole()  
    loading_effect()
    delay_print("Your hand instinctively swings up to shield your eyes as you step into the most bright room you've ever seen in your life.")
    delay_print("Light pours off the ceiling and the walls.")
    delay_print("It washes over you, and you suddenly feel energized.")
    Esteri.setHP(Esteri.MaxHP) #Sets Esteri's health to max if MaxHP is somehow more than 1000
    Kosu.setHP(Kosu.MaxHP)
    delay_print("Kosu wiggles his ankle. 'It feels normal again!'")
    time.sleep(1)
    clearConsole()
    delay_print("You look over at him, suddenly guilty.")
    delay_print("What will you say?")
    delay_print(" 1. Are you sure that you want to be doing this?")
    delay_print(" 2. I'm worried. I don't want to put you in danger.")
    kosu_talk_1_yay_woo_puppy_fish = validate_input(["1", "2"], "Kosu watches you, waiting for a comment.").lower()
    time.sleep(1)
    clearConsole()
    if kosu_talk_1_yay_woo_puppy_fish == "1":
      delay_print("Kosu grins at you. 'Of course!'")
    delay_print("He looks upwards wistfully. 'I have to come. You're like a sister to me, Esteri. I can't let you get hurt.'")
    delay_print("You laugh and stand up, brushing yourself off.")
    delay_print("What will you say?")
    delay_print(" 1. All right, enough nobleness. Let's go!")
    delay_print(" 2. Thank you, Kosu. I'm going to do my best to protect you, too.")
    validate_input(["1", "2"], "Kosu watches you, waiting for a comment.").lower()
    time.sleep(1)
    clearConsole()
    delay_print("Kosu climbs onto his feet. 'Let's go!'")
    delay_print("As he says that, a door opens in front of you, a single dark blotch in the center of the room.")
    delay_print("Are you ready to step through it?")
    validate_input(["y", "yes"], "You'd better go...")
    time.sleep(1)
    clearConsole()
  elif dronae_path_1 == "2":
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
    validate_input(["1", "2"], "Answer now! The Dronae looks agitated...").lower()
    time.sleep(1)
    clearConsole()
    delay_print("The Dronae groans. 'Of course I can't tell you that, impertinent child.'")
    delay_print("It looks over you. 'But...' It turns away, looking slightly fearful. 'Maybe I can heal you.'")
    delay_print("It climbs onto your stomach, and begins to mutter a few incantations.")
    delay_print("The Dronae's paws glow. You suddenly feel replenished.")
    Esteri.setHP(Esteri.MaxHP)
    time.sleep(1)
    clearConsole()
    delay_print("It scampers off your stomach and glares up at you as you sit up slowly, stretching your arms with new vigorousness.") 
    delay_print("'The Sentinel is not very nice,' the Dronae admits with trepidation. 'It keeps us safe, but I resent it for controlling us.'")
    delay_print("It turns to stare you in the eye. 'You seem to be a noble child... so I trust you to defeat the Sentinel and bring long-due revenge upon it.'") 
    delay_print("Now it smiles at you, mouth curling up into an eerie shape. 'But first, I would like you to send me to my family. Please prove that you were worthy of my favor!'")
    time.sleep(1)
    clearConsole()
    cave_battle_5 = Battle([Esteri], [Dronae.copy()], "cave", "The Dronae launches itself at your chest!", "dronae")
    cave_battle_5.begin()
    delay_print("You watch as the Dronae's remains fade in the wind, feeling faintly guilty.")
    delay_print("But your trepidation fades as you remember your mission and fill with resolve.")
    delay_print("Before you, mushrooms begin to sprout furiously in luminescent clumps, forming a path.")
    delay_print("Would you like to continue down the path?")
    validate_input(["y", "yes"], "You'd better go!")
    loading_effect()
    clearConsole()
    delay_print("You stumble into another lighted cavern. This one is lined with fluorescent mushrooms like the ones you saw above. The floor is woven with roots.")
    delay_print("'Esteri!' Kosu's voice rings off the walls.")
    delay_print("Your eyes adjust, and you gasp.")
    delay_print("Your friend is ensnared in a tangle of vines, wrapping around him in an intricate pattern and constricting quickly.")
    delay_print("Yet again, a Dronae stands guard in front of the structure.")
    time.sleep(1)
    clearConsole()
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
    time.sleep(1)
    clearConsole()
    cave_battle_4 = Battle([Esteri, Kosu], [Dronae.copy(), Dronae.copy()], "cave", "They swipe a claw at your face in synchrony!", "dronae")
    cave_battle_4.begin()
    delay_print("When the Dronae fall, a voice echoes through the cavern.")
    time.sleep(1)
    clearConsole()
    delay_print(WHITE_ITALIC + "Esteri..." + WHITE_ITALIC)
    delay_print(WHITE + "Kosu turns frantically, searching for its source. 'What is that?!'" + WHITE)
    delay_print(WHITE_ITALIC + "You have not yet won..." + WHITE_ITALIC)
    delay_print(WHITE + "You begin to furiously walk towards the exit. Kosu follows you." + WHITE)
    delay_print(WHITE_ITALIC + "I look forward to seeing you..." + WHITE_ITALIC)
    delay_print(WHITE + "You freeze." + WHITE)
    delay_print("The voice fades away with a low whine.")
    delay_print("You feel a light breeze rushing over you, and suddenly feel re-energized.")
    Esteri.setHP(Esteri.MaxHP)
    time.sleep(1)
    clearConsole()
    delay_print("Now Kosu grabs your arm and begins to tug you along.")
    delay_print("'I don't know what that was, but we don't have time to worry about it,' he whispers, then winces. You notice that he's limping.")
    delay_print("You wrap your arm around Kosu's shoulders to help support him, and the two of you slowly stumble to the door.")
    delay_print("Are you ready to exit?")
    validate_input(["y", "yes"], "You'd better go...")
    time.sleep(1)
    clearConsole()
  loading_effect()
  delay_print("You step into a dark cavern, akin to the first one.")
  delay_print("The ceiling twinkles like the night sky, spangled with stars.")
  delay_print("Kosu gasps in awe. 'It's beautiful!'")
  time.sleep(1)
  delay_print("A thundering footstep rings through the space.")
  delay_print("Beside you, Kosu flinches.")
  delay_print(WHITE_ITALIC + "Now..." + WHITE_ITALIC)
  delay_print(WHITE + "You ready your spear. Beside you, Kosu tenses." + WHITE)
  delay_print(WHITE_ITALIC + "...the ceremony will begin!" + WHITE_ITALIC)
  time.sleep(1)
  clearConsole()
  aiko_lepo_boss_battle = Battle([Esteri, Kosu], [Sentinel.copy()], "cave", "A massive claw swings out at your face!", "sentinel")
  aiko_lepo_boss_battle.begin()
  time.sleep(1)
  clearConsole()
  delay_print("The Sentinel falls, crashing down onto the ground forcefully and then dissolving with a final groan.")
  delay_print("A door appears in front of you. Will you enter?")
  validate_input(["y", "yes"], "You'd better go in!").lower()
  delay_print("You got the people and like got out and sh*t and now you're going to go back to the village.")
  time.sleep(1)
  village_1()
  #  quest_completion == True

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
#Shouldn't it be "if" running so that it doesn't become an infinite loop? :P
#ah yes sorry lol
if running == True:
  # amaliyahIntro()
  adventureBeg()
  # village_1()
