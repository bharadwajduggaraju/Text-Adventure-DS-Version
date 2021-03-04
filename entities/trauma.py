from util.console.output import delay_print

#List of Trauma Entities (Placeholder)
trauma_entities = ["", "Esteri", "Cressida"]
#Trauma Generator Variables
fear_name = [
  "fire", "suffocation", "brutality", "necromancy", "magic", "facing "
]
wound_name = [
  "wounded arm",
  "broken arm",
  "wounded leg",
  "broken leg",
  "bruised rib",
  "broken rib",
  "wounded eye",
  "concussion",
  "disfiguring wound",
  "infected wound",
]
trauma_name = [
  'grief', 'moral conflict', 'failure', 'cowardice', 'undeclared love for ',
  'worry for '
]
true_fear_name = [
  "fire", "suffocation", "brutality", "necromancy", "magic", "death",
  "facing "
]
true_wound_name = [
  "severed arm ",
  "severed leg ",
  "internal injuries ",
  "coma ",
  "permanent disfiguration ",
  "lingering weakness ",
]
true_trauma_name = [
  'deep concern for ', 'terrible regret', 'true failure', 'true cowardice',
  'forever undeclared love for ', 'memories of the death of ',
  "memories of the death of their lover "
]


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
