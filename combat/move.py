import random

from util.console.input import validate_int_input

class Move:
  def enemy_target_select(group):
    target_chances = []
    total = 0
    for entity in group:
      SPrescence = entity.getStatsWithEffects()["SocialPresence"]
      target_chances.append(SPrescence)
      total += SPrescence
    threshhold = random.randint(1, total)
    for i in range(len(target_chances)):
      if threshhold <= target_chances[i]:
        return group[i]
      else:
        threshhold -= target_chances[i]
    #basically this should make the enemy attack a character based on a chance of their socialHeart versus that of their companions
    # A higher social presence increases the range of numbers where the character gets targeted
  
  def __init__(self, Name, Damage, DamageMult, CritChance, CritMult, FailChance, FailMult, ComboTime, ComboMult, Accuracy, AccMult, Effects, EffectLevel, EffectMult, CharactersHit, HitMult, TargetType=0):
    self.Name = Name
    self.Damage = Damage
    self.DamageMult = DamageMult
    self.CritChance = CritChance
    self.CritMult = CritMult
    self.FailChance = FailChance
    self.FailMult = FailMult
    self.ComboTime = ComboTime
    self.ComboMult = ComboMult
    self.Accuracy = Accuracy
    self.AccMult = AccMult
    self.Effects = Effects
    self.EffectLevel = EffectLevel
    self.EffectMult = EffectMult
    self.CharactersHit = CharactersHit
    self.HitMult = HitMult
    self.TargetType = TargetType
  
  def use(self, actor, party, enemies, actor_is_player=True):
    """Function of using a move. party and enemies are from the perspective of actor."""
    isAttack = self.TargetType == 0
    group = enemies if isAttack else party
    activeStats = actor.applyEffects()
    if actor_is_player:
      targ_index = validate_int_input(range(1, len(group)+1), "Invalid input.", "Enter your target's number. ") - 1
      target = group[targ_index]
      move_subject = "You" #Used later in print() statements
    else:
      target = Move.enemy_target_select(group)
      move_subject = actor.Name
    if isAttack:
      attackRoll = random.randint(0, 20) + (activeStats[self.Accuracy] * self.AccMult)
      success = attackRoll > target.AC
    else:
      success = True
    
    if success:
      moveAmount = activeStats[self.Damage] * self.DamageMult
      isCrit = random.randint(0, 40) < (activeStats[self.CritChance]**2)
      if isCrit:
        moveAmount *= 2

      if isAttack:
        target.dealDamage(moveAmount)
      else:
        target.heal(-moveAmount) #self.DamageMult is negative for heals, so moveAmount must be negated back to positive
      
      if moveAmount == 0:
        print("Move ineffective!") #Change?
      elif target.HP <= 0 and moveAmount > 0:
        print(target.Name + " killed!")
      elif target.HP >= target.MaxHP and moveAmount < 0:
        print(target.Name + " fully healed! Now at " + str(target.MaxHP) + " HP.")
      else: #Target neither killed nor fully healed; Give more information
        if isCrit:
          print("Critical!", end=" ")
        elif actor_is_player: #Don't print "Success" on enemy turns
          print("Success!", end=" ")
        
        if isAttack:
          print(move_subject + " dealt " + str(moveAmount) + " damage to " + target.Name + ".")
        else:
          print(move_subject + " healed " + target.Name + " " + str(-moveAmount) + " HP.")
        if actor_is_player ^ isAttack: #If one of actor_is_player and isAttack is True
          move_target = "Ally" #If actor_is_player and move is not an attack, target is player's ally
        else:
          move_target = "Enemy"
        print(move_target + " has " + str(target.HP) + " HP remaining.")
    else:
      print(move_subject + " missed!")
