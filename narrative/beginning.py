import time, sys
from util.colors import *
from util.variable.variables import inventory, add_item, set_money
from util.console.output import delay_print, clearConsole, loading_effect, Output
from util.console.input import yes_no, validate_input

def credits():
  #Approximate times in the recording given
  #~1:27
  old = Output.settings("long")
  Output.settings("long", 0.0285)
  delay_print("~~~ Credits ~~~", None, '\n', "RED_UNDERLINED")
  delay_print("Samiya Tanvi Sailer, Head Writer and Project Coordinator, Ai'ko Le'po Creator and Author")
  delay_print("Caden Ko, Head Worldbuilder and Project Coordinator")
  delay_print("Angelina Lawton, Head Composer, Pianist, and Oi'nan Developer")
  delay_print("Eesha Jain, Head Coder and Saving Specialist")
  delay_print("Joseph Eng, Head Coder")
  delay_print("Athena Shanklin, Head Oi'nan Developer and Side Quest Writer, Resident Weeb")
  delay_print("Krishna Maanasa Ramadugu, Tree Village Creator and Author and Violinist")
  delay_print("Vedaant Thuse Bal, Coding Team Member and Saving Specialist")
  delay_print("Bharadwaj Duggaraju, Coding Team Member and Saving Specialist")
  delay_print("Hiraeth Wang-Fiske, Head Character Designer and Artist")
  delay_print("Reetam Bhattacharya, Oi'nan Script Specialist")
  time.sleep(3.4)
  clearConsole()
  #~2:00
  Output.settings("long", 0.01)
  delay_print("Brought to you by An Unnamed Corporation...", end="")
  #Sum: 6.3
  time.sleep(4.2)
  clearConsole()
  time.sleep(2.1)
  #~2:13
  delay_print("The Legend of Cauliflower.", 0.01, "", "RED_ITALIC")
  time.sleep(17)
  #~2:33
  Output.settings("long", old)
  print() #Empty line
  sys.exit()
  



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