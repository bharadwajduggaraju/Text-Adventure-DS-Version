import time, sys
from util.colors import *
from util.variables import inventory, add_item
from util.console.output import delay_print, clearConsole, loading_effect
from util.console.input import yes_no, validate_input

def adventureBeg():
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
  inventory["Money"] = 100
  time.sleep(1)
  #tutorial()
  #inventorymenu()
  #settings()
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