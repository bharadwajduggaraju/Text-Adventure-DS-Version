from functions import funcs
import random

class Move:
  def __init__(self, Name, Damage, DamageMult, CritChance, CritMult, FailChance, FailMult, ComboTime, ComboMult, Accuracy, AccMult, Effects, EffectLevel, EffectMult, Characters_Hit, HitMult, TargetType=0):
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
    self.Characters_Hit = Characters_Hit
    self.HitMult = HitMult
    self.TargetType = TargetType
  
  def use(self, actor, party, enemies):
    validate_int_input = funcs["validate_int_input"]
    isAttack = self.TargetType == 0
    if isAttack:
      group = enemies
    else:
      group = party
    activeStats = actor.applyEffects()
    targ_index = validate_int_input(range(1, len(group)+1), "Invalid input.", "Choose your target. ") - 1
    target = group[targ_index]
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

      target.dealDamage(moveAmount)
      if target.HP <= 0:
        print(target.Name + " killed!")
      elif target.HP-moveAmount > target.MaxHP:
        print("Ally fully healed! Now at " + str(target.MaxHP) + " HP.")
      else:
        if isCrit:
          print("Critical!", end=" ")
        else:
          print("Success!", end=" ")
        
        if isAttack:
          print("Dealt " + str(moveAmount) + " damage.")
          print("Enemy has " + str(target.HP) + " HP remaining.")
        else:
          print("Healed " + str(-1*moveAmount) + " HP.")
          print("Ally has " + str(target.HP) + " HP remaining.")
    else:
      print("You missed!")
