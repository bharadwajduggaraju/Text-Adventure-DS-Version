import time, sys
from util.colors import *
from util.variable.variables import inventory, add_item, set_money
from util.console.output import delay_print, clearConsole, loading_effect
from util.console.input import yes_no, validate_input

def amaliyahIntro():
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
  clearConsole()

#   #Comments
#   '''
#   delay_print(WHITE + "You are facing a pack of fifteen kirin." + WHITE)
#   delay_print("You must defeat them without letting the timer run out after every move.")
#   delay_print("But be careful! They will fight back after every attack you make, so you have to choose your moves carefully.")
#   delay_print("You will choose between four attack options and the option to dodge the next attack. You may also access your inventory.")
#   delay_print("Dodging is useful when you need more time to think or want to learn what your opponent's attacks are.")
#   delay_print("But otherwise, you should select from your move menu or utilize an item from your inventory.")
#   delay_print("You'll learn more about your inventory later. For now, let's fight the Kirin using one of your four attacks.")
#   '''

#   #delay_print("Your four attacks are:")
#   #delay_print("1. Sword Slash")
#   #delay_print("2. Earthbreaking Stone Spires")
#   #delay_print("3. Divine Sword Triple ")
#   #delay_print("4. Basic Self-Healing")
#   ##NOTE: please don't have divine sword triple or earthbreaking stone spires
#   #Change ^ above in the Amaliyah character

#   time.sleep(3)
#   clearConsole()

def adventureBeg():
  delay_print("""
    The voice of the chaplain rings out in sonorous tones across the hall. "Esteri. Today, you are come of age, and eligible to ascend the throne. As it has been for the many centuries..."
    The chaplain drones on as you kneel on the flagstones, watching the play of candlelight on the polished rock. Slowly, the chaplain's voice drones to a close.
    "In the absence of the Chieftess Amaliyah, and with no kinswomen to anoint you, I hereby pronounce you a noble citizen of the Confederacy of Elyria." You rise, turning to face the assembled servants and courtiers with a graceful curtsy as the first rays of sunrise burst over the highest peak.
    Beneath you, the capital unfolds in the light, with its stone causeways swooping over the lake and from the mountains. You remain there as the hall slowly empties, despite the cold.
    A servant approaches, carrying a small bowl and a missive.
    "Lady Esteri, this missive from Regent Avivaki. She requests your presence."
    You nod, scanning the parchment. "I will be there."
    The servant nods and smiles. "The regent will be happy to see you."
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
    "Please, sit down. We have much to discuss, young one." Village Regent Aviveki meets your eyes with a solmen expression.
    Will you sit?""", indent=4)
  sit_with_regent_aviveki = validate_input(["yes", "y", "n", "no"], "You had better decide!").lower()
  if sit_with_regent_aviveki == "yes" or sit_with_regent_aviveki == "y":
    delay_print("Eager to gain knowledge on your mother, you quickly take a seat and listen.")
  elif sit_with_regent_aviveki == "no" or sit_with_regent_aviveki == "n":
    delay_print(""" 
    "I don't want to sit down," you say, crossing your arms. 
    Aviveki frowns. "I do not request cooperation," she says, voice taking on an edge. "Sit down, please."
    You sit. 
    """, indent=4)
  time.sleep(1)
  delay_print("""  
    Aviveki stares at you, gaze cold. "We have reasons to believe that your mother, Chieftess Amaliyah, may in fact be alive."
    Your heart rate speeds up. Years ago, when you were young, your mother had been sent on a quest to find new land for the people of Elyria. A few years into her quest, she disappeared and never returned. The village leaders seemed convinced that she was dead- Aviveki had been in power for ten years- but you didn't agree. 
    "As her descendant, the day has come for you to finally take on the responsibility of searching for her." Aviveki's mouth turns down a little as she says this, slightly derisive. 
    Silently, you pump your fist under the table, full of confidence. Finding your mother had been your goal for years. You leaned forwards a little in anticipation.
    "As the true future Chieftess of Elyria, and my successor, you must embark on this quest to find your mother and complete her mission. Can we trust you to complete this task with honor?" Aviveki's expression was borderline disinterested.
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
    "Wonderful." The village head tries to smile, mouth stretching upwards into a sort of grimace. "I knew that our people could count on you, Esteri."
    "Of course." You smile internally with pride. 
    "You'll require a naviagator for your journey, so I've select one of our skilled navigators-in-training to assist you."
    Aviveki frowns. "But he appears to be a bit late..."
  """, indent=4)
  delay_print()
  time.sleep(2)
  clearConsole()
  delay_print("""
    The door bursts open and a young man with an unruly mop of brown hair bursts in.
    The new arrival wipes sweat off of his brow, glancing up at the village head with a sheepish expression.
    The village head glares down at him in indignation. "You're late."

    Your eyes widen as you recognize the boy.
    Will you greet him?
  """, indent=4)
  kosu_is_here_yay = validate_input(["yes", "no", "y", "n"], "You have to decide fast! It's getting awkward!").lower()
  if kosu_is_here_yay == "yes" or kosu_is_here_yay == "y":
    delay_print("""
      "Kosu!" You jump out of your chair, grinning, and hug your best friend. "How are you? How did your trip to the Southern Villages go?"
      "Hey, Esteri!" Kosu grins. "It's been a few months, hasn't it? Nice to see you! I'm doing great. The trip went well. I assume you are too, seeing as you're finally going-"
    """, indent=4)
  if kosu_is_here_yay == "no" or kosu_is_here_yay == "n":
    delay_print("""
      You force yourself to study the table, unwilling to jeopardize your chance to search for your mother by tarnishing Aviveki's trust. 
      The boy, unwilling to take a hint, taps your shoulder. "Hey, Esteri! How are you? It's been a few months since I last saw you!"
      You make eye contact with Aviveki for a second- she appears disdainful- and look up at Kosu, suddenly guilty for trying to ignore your best friend. "Hi, Kosu!" You stand up and give him a hug. "I'm doing great. How was your trip to the Southern Villages?"
      Kosu smiles. "The trip went great."
      Aviveki clears her throat and you look back at her, remembering her presence. 
      "Thank you, Regent Aviveki!" Kosu says, grinning widely. "Esteri is thrilled to-"
    """, indent=6)
  time.sleep(0.25)
  option = yes_no(
    False, "You need to decide quickly...",
    "Do you interrupt Kosu in order to preserve your dignity? ").lower()

  if option == "y" or option == "yes":
    delay_print("""
      You shoot Kosu a warning glance and he quiets, remorseful. Then you turn to face the village regent.
      Her expression is haughty. "You're wasting time."
      Do you apologize?
    """, indent=6)

    option = validate_input(["yes", "no", "y", "n"], "Decide now! She's the chief!").lower()
    if option == "yes" or option == "y":
      delay_print("""
        "I apologize, Regent Aviveki," you say, and awkwardly curtsy, simmering internally with fury. Kosu bows his head, sheepish.
        "You're forgiven," the village leader says with an air of superiority. "But don't forget your manners in the future."
        You bite your tongue to hold back further remarks.
      """, indent=8)
    elif option == "2":
      delay_print("""
        "Kosu and I deserve to enjoy our reunion," you say, glaring. 
        The village leader sniffs in indignation. "I am a very busy woman. Please enjoy your reunion when you are no longer in my presence."
        You bite your tongue to hold back further remarks.
      """, indent=8)
    delay_print(
      "Kosu speaks up, a twinge of guilt in his voice. 'Is there anything else that we need to know before leaving?'"
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
    Kosu shakes his head in indignation. "We aren't quitters," he says, voice spiking with an undertone of determination. "Esteri and I will be fine."
    Will you agree with him?
  """, indent=4)
  option_whee_yay_cookie_snowballcake = validate_input(["yes", "y", "no", "n"], "You have to decide! The village regent looks impatient!").lower()
  if option_whee_yay_cookie_snowballcake == "yes" or option_whee_yay_cookie_snowballcake == "y":
    delay_print("""
      "Kosu's right," you say, grinning with confidence. Adrenaline courses through your veins. "We'll be fine."
    """)
  if option_whee_yay_cookie_snowballcake == "no" or option_whee_yay_cookie_snowballcake == "n":
    delay_print("""
      You nod noncommitally. In reality you are confident in your abilities to carry out the task before you; but Aviveki already seems to believe that you are naive, and you don't wish to cement her opinion.
      """, indent=6)
  time.sleep(1)
  clearConsole()
  delay_print("""
    Regent Aviveki smiles, eyes still cold. "Wonderful," she says. "I'll instruct you on where to go."
    Taking a map from beside her chair, she rolls it out on the table. "Here-" she points at a wide parcel of land- "is Elyria. This is our home."
    She moves her finger to a small spot on the map near your domain. "Here is a small village known as Ai'ko Le'po Koate'nan. An old friend of your mother's resides here. You will begin by traveling to this village, in the hopes that your mother's friend can offer you advice or assistance."

    She pulls a letter out of her desk and sets it in front of you. "Deliver this letter to an old woman by the name of Kurigalu. She should be willing to help you find your mother. At the very least, she'll find you someone who can aid you on your journey. You will also be given given 100 nagara scrip to begin your journey."
    She tosses a pouch of coins onto the desk.

    The regent stands up, leaving the letter and money on the desk in front of you. She meets your eyes.
    "Your mother was a friend of mine," she murmurs, more to herself than you. "I hope that you can bring her back."
    She turns, and you watch her retreating back, unable to wipe the sight of Regent Aviveki's regretful, resigned expression from your mind.
    Any annoyance you felt towards her during your encounter fades.
    Kosu reaches out and picks up the letter. He hands it to you. "I believe this belongs to you."
    You take the letter and place it in your bag along with the coins.
  """, indent=4)
  add_item("Letter for Kurigalu", "An important letter from the regent.")
  set_money(100)
  time.sleep(1)
  #tutorial()
  #inventorymenu()
  #settings()
  delay_print("""
    "We should go," you tell Kosu.
    He nods. "If we don't leave within the hour, we won't make it to Ai'ko Le'po before nightfall."
    The two of you amble to the exit, and you rest your hand on the doorknob. Your mind wanders for a second.
  """, indent=4)
  time.sleep(1)
  delay_print(
    "You wonder how your mother felt when she was setting out on her journey.")
  time.sleep(1)
  clearConsole()
  delay_print(GREY_ITALIC + """
    Mother kneels down, caressing your cheek. "I'll be back soon, Esi," she whispers, smiling at you.
    "Are you scared, Mommy?" You look up at her, cheeks wet with tears.
    Mother wrings her hands. She stares up at the ceiling, watching the warm light from the lanterns flicker. "No," she finally says, a tremor in her voice. "Dai'ra, Esi. I will be strong for Elyria."
    "Yes, mommy, I know you are never scared of anything." You wipe your eyes furiously, determined to look brave like your mother.
    She stands up. "There's nothing wrong with having fears, Esi," she says, touching your cheek. "Real bravery is when you're scared, but push through anyway." She smiles, but her eyes are sad. "Can you promise to be brave for me?" You nod, looking up at her with resolution in your eyes.
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
    You look at him, somewhat solemn. "You know she was right, Kosu? We could die on this mission." For the first time, your confidence wavers a little.
    Kosu grins at you. "We don't die," he says reassuringly, seeming to sense your fears. "After all, we're the best team in all of Elyria."
    You raise your eyebrows. "Is that so?" You swallow your misgivings and smile. You've been preparing for this journey for your entire life; you're ready.
    The two of you laugh and banter as you amble down the rocky foothill, traveling the same path that your mother had followed so many years earlier.
  """, indent=4)
  time.sleep(0.25)
  clearConsole()
  loading_effect()
  time.sleep(0.25)
  delay_print("""
    You slog along, grouchy, with branches snapping under your feet. Fog hangs thickly in the air around you.
    Do you express impatience?
  """, indent=4)
  fog_forest_complainer_oof = validate_input(["yes", "y", "no", "n"], "You continue to trudge through the forest.").lower()
  if fog_forest_complainer_oof == "yes" or fog_forest_complainer_oof == "y":
    delay_print("""
      "Are we almost there?" you ask Kosu with an expression of consternation. "The woods don't seem to end anytime soon."
      Kosu studies his map. "Yeah," he assures you. "We'll arrive in the village any minute now."
    """, indent=6)
  if fog_forest_complainer_oof == "no" or fog_forest_complainer_oof == "n":
    delay_print("""
      You bite your tongue, deciding to hold back any complaint after you glance at Kosu, who's laser-focused on his map. He stumbles over a root and you grab his arm.
      "Thanks," he says, grinning at you.
    """, indent=6)
  delay_print("""
    Seconds later, the two of you break through the edge of the forest.
    The trees have been cleared unevenly from a patch of roughly packed land, lined with small huts that creak under the weight of the sky.
    "Here we are!" Kosu grins. "Let's go look for Kurigalu."
    The two of you stroll slowly through the town. It's silent: oddly so. 
    "There's no one here," Kosu observes. He looks nervous.
  """, indent=4)
