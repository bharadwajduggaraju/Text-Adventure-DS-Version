#Characters (each should be a matrix with the format [name], hp, stamina, mana,  presence (impacts social), heart (impacts combat targeting and relationships), stability (impacts wound penalties, reduces trauma), grace (impacts accuracy and combos), poise (impacts armor and wound penalties), skill (impacts crits and damage), affinity (impacts spell damage or healing and # of enemies hit), control (affects spell crits and penalties of a spell failure), concentration (affects wound penalties and accuracy), [items in inventory], [traumas and permanent traits], [battle effects], tags, move, move2, move3)
#Let's go with 20 points in skills, and 30 in core stats.
#Each point in a physical skill increases HP by 2, party members start with 5HP

class Character:
  _STAT_KEYS = ["SocialPresence", "SocialHeart", "SocialStability", "PhysicalGrace", "PhysicalSkill", "PhysicalPoise", "MagicalAffinity", "MagicalControl", "MagicalConcentration"]
  def __init__(self, name, HP, MaxHP, SP, MaxSP, MP, MaxMP, SocialPresence, SocialHeart, SocialStability, PhysicalGrace, PhysicalSkill, PhysicalPoise, MagicalAffinity, MagicalControl, MagicalConcentration, Inventory, Trauma, Effects, Tags, Move, Move2, Move3, maxDeaths=3, deaths=0):
    self.Name = name
    self.Adrenaline = 0 #Bonus HP which lasts only for one battle
    self.MaxAdrenaline = 255 #Placeholder
    self.HP = HP
    self.MaxHP = MaxHP
    self.SP = SP
    self.MaxSP = MaxSP
    self.MP = MP
    self.MaxMP = MaxMP
    self.PermStats = {
      "SocialPresence": SocialPresence,
        #impacts combat targeting and social
      "SocialHeart": SocialHeart,
        #impacts relationships
      "SocialStability": SocialStability,
        #impacts wound penalties, redces trauma
      "PhysicalGrace": PhysicalGrace,
        #impacts accuracy and combos
      "PhysicalSkill": PhysicalSkill,
        #impacts armor and wound penalties
      "PhysicalPoise": PhysicalPoise,
        #impacts crits and damage
      "MagicalAffinity": MagicalAffinity,
        #impacts spell damage or healing and # of enemies hit
      "MagicalControl": MagicalControl,
        #affects spell crits and penalties of a spell failure
      "MagicalConcentration": MagicalConcentration
        #affects wound penalties and accuracy
    }
    self.AC = 0
    self.DmgReductPercent = 0
    self.Armor = []
    self.Inventory = Inventory
    self.Trauma = Trauma
    self.Effects = Effects
    self.Move = Move
    self.Move2 = Move2
    self.Move3 = Move3
    self.MaxDeaths = maxDeaths
    self.Deaths = deaths
    # self.DeathFunc = None
    self.Tags = Tags
  
  def get_stat(self, stat_name):
    return self.PermStats[stat_name]

  #No longer needed, but left in case we need it again.
  #  def copy(self):
      #copy = Character(self.name, self.HP, self.SP, self.MaxSP, self.MP, self.MaxMP, self.SocialPresence, self.SocialHeart, self.SocialStability, self.PhysicalGrace, self.PhysicalSkill, self.PhysicalPoise, self.MagicalAffinity, self.MagicalControl, self.MagicalConcentration)
  #   return copy
  
  #Applies a character's effects on them. Returns a dictionary with the new stats.
  def applyEffects(self):
    """Applies effects to self and returns a copy of self.PermStats with the applied effects."""
    newStats = self.PermStats.copy()
    newStatsKeys = Character._STAT_KEYS #Guarenteed order. Currently not changed, don't need to copy

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
    newStats = self.PermStats.copy()
    newStatsKeys = Character._STAT_KEYS
    newHP = self.HP

    for i in range(len(self.Effects)):
      effect = self.Effects[i]
      newHP -= effect.Damage
      for j in range(9):
        newStats[newStatsKeys[j]] -= effect.Reducts[j]
    return newStats
  
  def addEffect(self, effect):
    """Adds the given effect to self."""
    self.Effects.append(effect)
  def removeEffect(self, effect_name, count):
    """Removes count number of effects named effect_name. Returns the number removed."""
    num_removed = 0
    i = 0
    while i < len(self.Effects) and num_removed < count:
      if self.Effects[i].name == effect_name:
        del self.Effects[i]
        num_removed += 1
      else: #Only increment i if none were removed- deletion will move next item into index i
        i += 1
    return num_removed
  
  def checkHP(self):
    if self.HP < 0:
      self.HP = 0
    elif self.HP > self.MaxHP:
      self.HP = self.MaxHP
    if self.Adrenaline < 0:
      self.Adrenaline = 0
    elif self.Adrenaline > self.MaxAdrenaline:
      self.Adrenaline = self.MaxAdrenaline
    #die check will take place in battleFinished()

  def calc_damage(self, damage):
    dealt_damage = damage
    dealt_damage *= (100 - self.DmgReductPercent)/100
    dealt_damage = int(dealt_damage)
    return dealt_damage
  def dealDamage(self, damage):
    dealt_damage = self.calc_damage(damage)

    self.HP -= dealt_damage
    if self.HP > self.MaxHP:
      self.HP = self.MaxHP
    elif self.HP < 0:
      self.Adrenaline += self.HP #self.HP is negative
      if self.Adrenaline < 0:
        self.Adrenaline = 0
      self.HP = 0
    #The die check will take place in battleFinished()
  def heal(self, amount, HP_type=0):
    """type: 0-Adrenaline, 1-HP"""
    if HP_type == 0:
      self.Adrenaline += amount
    elif HP_type == 1:
      self.HP += amount
    else:
      raise ValueError("Unexpected value for HP_type: " + str(HP_type))
    self.checkHP()
  
  def setHP(self, health):
    self.HP = health
    self.checkHP()

  def isDead(self):
    return self.HP <= 0 and self.Adrenaline <= 0
  def isPermamentlyDead(self):
    return self.Deaths > self.MaxDeaths
  def die(self):
    self.Deaths += 1
    if self.Deaths > self.MaxDeaths:
      return True
    return False