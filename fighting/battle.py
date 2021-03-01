import util.colors as col
from util.share_functions import funcs
from util.variables import party, locations, enemies
from fighting.timer import clearTimers, resetTimer, TimeOut

class Battle:
  def __init__(self, battle_party, enemy_team, location, intro, primary_enemy_name, lose_message="Your enemies have defeated you"):
    self.battleParty = battle_party.copy()
    self.enemyTeam = enemy_team
    self.location = location
    self.intro = intro
    self.primaryEnemyName = primary_enemy_name
    self.loseMessage = lose_message

  def isFinished(self, retreated):
    for ally in list(self.battleParty):
      if ally.HP <= 0:
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
    delay_print = funcs["delay_print"]
    validate_input = funcs["validate_input"]
    clearConsole = funcs["clearConsole"]
    
    delay_print(str(self.intro))
    validate_input([], "", "Are you ready to start the battle? ", validate=False)
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
          enemy.turn(self.battleParty)
    
    var = self.isFinished(retreated)
    if (var == 1):
      delay_print("You and your team have won!")
    elif not retreated:
      delay_print("Your enemies have defeated you.")
    #Remove any running timers after function
    clearTimers()
    return var

  def turn(self, actor):
    delay_print = funcs["delay_print"]
    validate_input = funcs["validate_input"]
    getTimerMode = funcs["getTimerMode"]
  
    timerMode = getTimerMode()
    timeEnd = enemies[self.primaryEnemyName].TimeGiven + locations[self.location]["time"]
    resetTimer(timeEnd)
    
    delay_print("\nBeginning " + str(actor.Name) + "\'s turn.")
    
    if timerMode == "on":
      print("Time: 10\n")
    
    print("Your moves:\n 1. " + str(actor.Move.Name) + "\n 2. " + str(actor.Move2.Name) + "\n 3. " + str(actor.Move3.Name) + "\n 4. Retreat from battle\n")
    prompt = "Enter 1, 2, 3, or 4: "
    answer = validate_input(["1", "2", "3", "4"], "Invalid input.", prompt)
    answer = int(answer)
    
    if 1 <= answer <= 3:
      resetTimer(timeEnd)
      if answer == 1:
        move = actor.Move
      elif answer == 2:
        move = actor.Move2
      else: #answer == 3
        move = actor.Move3
      move.use(actor, self.battleParty, self.enemyTeam)
      resetTimer(timeEnd)
    elif answer == 4:
      delay_print("You have retreated!")
      return True
    return False
