import random
#Characters (each should be a matrix with the format [name], [hp, stamina, mana], [ presence (impacts social), heart (impacts relationships), stability (impacts wound penalties, reduces trauma)], [grace (impacts accuracy and combos), poise (impacts armor and wound penalties), skill (impacts crits and damage)], [affinity (impacts spell damage or healing and # of enemies hit), control (affects spell crits and penalties of a spell failure), concentration (affects wound penalties and accuracy)], [items in inventory], [traumas and permanent traits], [battle effects])
class Enemy:
  _STAT_KEYS = ["SocialPresence", "SocialHeart", "SocialStability", "PhysicalGrace", "PhysicalSkill", "PhysicalPoise", "MagicalAffinity", "MagicalControl", "MagicalConcentration"]
  def __init__(self, name, maxHP, HP, timeGiven, SocialPresence, SocialHeart, SocialStability, PhysicalGrace, PhysicalSkill, PhysicalPoise, MagicalAffinity, MagicalControl, MagicalConcentration,move1, move2, move3, moveChanceDistr, effects=[],):
    self.Name = name
    self.MaxHP = maxHP
    self.HP = HP
    self.TimeGiven = timeGiven
    self.Stats = {
      "SocialPresence": SocialPresence,
      "SocialHeart": SocialHeart,
      "SocialStability": SocialStability,
      "PhysicalGrace": PhysicalGrace,
      "PhysicalSkill": PhysicalSkill,
      "PhysicalPoise": PhysicalPoise,
      "MagicalAffinity": MagicalAffinity,
      "MagicalControl": MagicalControl,
      "MagicalConcentration": MagicalConcentration
    }
    self.AC = PhysicalGrace * 2
    self.Damage = PhysicalSkill
    self.move1 = move1
    self.move2 = move2
    self.move3 = move3
    self.moves = [self.move1, self.move2, self.move3]
    scale = 100 / sum(moveChanceDistr)
    self.moveChanceDistr = []
    for i in range(3):
      self.moveChanceDistr.append(scale*moveChanceDistr[i])
    self.Effects = effects

  def turn(self, party, enemies):
    """party and enemies are from the point of view of the player"""
    self.applyEffects()
    move_roll = random.randint(1, 100)
    for i in range(3):
      if move_roll <= self.moveChanceDistr[i]:
        move = self.moves[i]
      else:
        move_roll -= self.moveChanceDistr[i]
    move.use(self, enemies, party, False)
    # target selection code moved to combat/move.py, in Move.enemy_target_select(), which is called by move.use()

  def dealDamage(self, damage):
    self.HP -= damage
    if self.HP < 0:
      self.HP = 0
    elif self.HP > self.MaxHP:
      self.HP = self.MaxHP
    #The die check will take place in battleFinished()
  def heal(self, healAmt):
    self.HP += healAmt
    if self.HP < 0:
      self.HP = 0
    elif self.HP > self.MaxHP:
      self.HP = self.MaxHP
  
  def setHP(self, newHP):
    self.HP = newHP
  
  #Makes a copy for individual enemies
  def copy(self):
    copy = Enemy(self.Name, self.MaxHP, self.HP, self.TimeGiven, self.Stats["SocialPresence"], self.Stats["SocialHeart"], self.Stats["SocialStability"], self.Stats["PhysicalGrace"], self.Stats["PhysicalSkill"], self.Stats["PhysicalPoise"], self.Stats["MagicalAffinity"], self.Stats["MagicalControl"], self.Stats["MagicalConcentration"], self.move1, self.move2, self.move3, self.moveChanceDistr.copy(), self.Effects.copy())
    return copy

  #Effects fields: Name, Damage, Duration, isWounds, Reducts, TimeReduct
  def applyEffects(self):
    """Applies effects to self and returns a copy of self.PermStats with the applied effects."""
    newStats = self.Stats.copy()
    newStatsKeys = newStats.keys()

    i = 0
    while i < len(self.Effects):
      effect = self.Effects[i]
      effect.duration -= 1
      if effect.duration == 0:
        del self.Effects[i] #If the effect is removed, a new effect will now be at the same index- Should not increment i
      elif effect.duration < 0:
        effect.duration = -1
      else:
        self.HP -= effect.Damage
        for j in range(9):
          newStats[newStatsKeys[j]] -= effect.Reducts[j]
        i += 1
    return newStats
  def getStatsWithEffects(self):
    """Only returns modified copy of stats."""
    newStats = self.Stats.copy()
    newStatsKeys = newStats.keys()
    newHP = self.HP

    for i in range(len(self.Effects)):
      effect = self.Effects[i]
      newHP -= effect.Damage
      for j in range(9):
        newStats[newStatsKeys[j]] -= effect.Reducts[j]
    return newStats
