import util.colors as col
from util.console.output import delay_print, clearConsole
from util.console.input import validate_input, validate_int_input
from util.variable.instances import enemies
from util.variable.variables import party, locations
from combat.timer import clearTimers, resetTimer, TimeOut, Timer

def full_battle(battle_party, enemy_team, location, intro, primary_enemy_name, lose_message="Your enemies have defeated you!"):
  """Creates and begins a Battle instance.
  Returns the battle result"""
  battle = Battle(battle_party, enemy_team, location, intro, primary_enemy_name, lose_message)
  battle_result = battle.begin()
  return battle_result

class Battle:
  def __init__(self, battle_party, enemy_team, location, intro, primary_enemy_name, lose_message="Your enemies have defeated you."):
    self.battleParty = battle_party.copy()
    self.enemyTeam = enemy_team
    self.location = location.title()
    self.intro = intro
    self.primaryEnemyName = primary_enemy_name.lower()
    self.loseMessage = lose_message

  def isFinished(self, retreated):
    for ally in list(self.battleParty):
      if ally.HP <= 0 and ally.Adrenaline <= 0:
        ally.HP = ally.MaxHP
        self.battleParty.remove(ally)
        if ally.die():
          party.remove(ally)
    for enemy in list(self.enemyTeam):
      if enemy.HP <= 0:
        self.enemyTeam.remove(enemy)
    
    if retreated or (len(self.battleParty) == 0): #Exiting caused by return prevents need for if elif else
      return 2
    if len(self.enemyTeam) == 0:
      return 1
    return 0
  
  def begin(self): #If you have better name suggestions, go ahead and change this (and the calls in main.py)
    delay_print(str(self.intro))
    result = validate_input([], "", "Are you ready to start the battle? ", validate=False).lower()
    if result == "shaymin":
      return 2
    #Prompt may be changed
    delay_print("Ready or not, time to begin...")
    clearConsole()

    print(col.PURPLE_BOLD + "~~BATTLE START~~" + col.RESET)

    retreated = False
    while self.isFinished(retreated) == 0:
      #Reports HPs of enemies
      delay_print("\nEnemies:")
      num = 1
      for enemy in list(self.enemyTeam):
        delay_print(str(num) + ". " + enemy.Name + ": " + str(enemy.HP) + " HP")
        num += 1

      #Report HPs of party
      num = 1
      delay_print("\nParty:")
      for ally in list(self.battleParty):
        delay_print(str(num) + ". " + ally.Name + ": " + str(ally.HP) + " HP")
        for effect in ally.Effects:
          delay_print(", " + str(effect.name))
        num += 1

      #Try turns
      for ally in list(self.battleParty):
        try:
          retreated = self.turn(ally)
          clearTimers()
        except TimeOut: #Imported from timer.py
          print(col.RED_BOLD + "~Sorry, time is up.~" + col.RESET)

      #Enemy turns
      clearTimers()
      if (self.isFinished(retreated) == 0):
        for enemy in list(self.enemyTeam):
          delay_print("\n" + enemy.Name + " begins their turn.")
          enemy.turn(self.battleParty, self.enemyTeam)

    #Remove any running timers
    clearTimers()
    result = self.isFinished(retreated)
    if (result == 1):
      delay_print("You and your team have won!")
    elif not retreated:
      delay_print(self.loseMessage)
    return result

  def turn(self, actor): 
    delay_print("\nBeginning " + str(actor.Name) + "\'s turn.")

    timerOn = Timer.settings("timerMode") == "on"
    if timerOn:
      timeEnd = enemies[self.primaryEnemyName].TimeGiven + locations[self.location]["time"]
      resetTimer(timeEnd)
      print("Time:", timeEnd)
      print()
    
    print("Your moves:\n 1. " + str(actor.Move.Name) + "\n 2. " + str(actor.Move2.Name) + "\n 3. " + str(actor.Move3.Name) + "\n 4. Use item")
    answer = validate_int_input(range(1, 6), "Invalid input.", "Enter 1, 2, 3, or 4: ")
    clearTimers()
    
    if 1 <= answer <= 3:
      # Select move
      if answer == 1:
        move = actor.Move
      elif answer == 2:
        move = actor.Move2
      else: #answer == 3
        move = actor.Move3
    
      # Play moves, with combos
      scale = 1 - (1/(actor.PermStats["PhysicalGrace"]+1))
      in_time = True
      while in_time:
        resetTimer(timeEnd)
        try:
          move.use(actor, self.battleParty, self.enemyTeam)
        except TimeOut:
          in_time = False
        timeEnd *= scale
    elif answer == 4:
      pass
    elif answer == 5:
      delay_print("You have retreated!")
      return True
    return False
