#Characters (each should be a matrix with the format [name], [hp, stamina, mana], [ presence (impacts combat targeting and social), heart (impacts relationships), stability (impacts wound penalties, reduces trauma)], [grace (impacts accuracy and combos), poise (impacts armor and wound penalties), skill (impacts crits and damage)], [affinity (impacts spell damage or healing and # of enemies hit), control (affects spell crits and penalties of a spell failure), concentration (affects wound penalties and accuracy)], [items in inventory], [traumas and permanent traits], [battle effects])
#Let's go with 20 points in skills, and 30 in core stats.

class Character:
  def __init__(self, name, HP, MaxHP, SP, MaxSP, MP, MaxMP, SocialPresence, SocialHeart, SocialStability, PhysicalGrace, PhysicalSkill, PhysicalPoise, MagicalAffinity, MagicalControl, MagicalConcentration, Inventory, Trauma, Effects, Tags, Move, Move2, Move3, maxDeaths=3, deaths=0):
    self.Name = name
    self.HP = HP
    self.MaxHP = MaxHP
    self.SP = SP
    self.MaxSP = MaxSP
    self.MP = MP
    self.MaxMP = MaxMP
    self.SocialPresence = SocialPresence
      #impacts combat targeting and social
    self.SocialHeart = SocialHeart
      #impacts relationships
    self.SocialStability = SocialStability
      #impacts wound penalties, reduces trauma
    self.PhysicalGrace = PhysicalGrace
      #impacts accuracy and combos
    self.PhysicalSkill = PhysicalSkill
      #impacts armor and wound penalties
    self.PhysicalPoise = PhysicalPoise
      #impacts crits and damage
    self.MagicalAffinity = MagicalAffinity
      #impacts spell damage or healing and # of enemies hit
    self.MagicalControl = MagicalControl
      #affects spell crits and penalties of a spell failure
    self.MagicalConcentration = MagicalConcentration
      #affects wound penalties and accuracy
    self.Inventory = Inventory
    self.Trauma = Trauma
      #Maybe includes permanent effects? See old comment in main.py
    self.Effects = Effects
    self.Move = Move
    self.Move2 = Move2
    self.Move3 = Move3
    self.MaxDeaths = maxDeaths
    self.Deaths = deaths
    self.Tags = Tags
  
  def get_stat(self, stat_name):
    if stat_name == "SocialPresence":
      return self.SocialPresence
    elif stat_name == "SocialHeart":
      return self.SocialHeart
    elif stat_name == "SocialStability":
      return self.SocialStability
    elif stat_name == "PhysicalGrace":
      return self.PhysicalGrace
    elif stat_name == "PhysicalSkill":
      return self.PhysicalSkill
    elif stat_name == "PhysicalPoise":
      return self.PhysicalPoise
    elif stat_name == "MagicalAffinity":
      return self.MagicalAffinity
    elif stat_name == "MagicalControl":
      return self.MagicalControl
    elif stat_name == "MagicalConcentration":
      return self.MagicalConcentration

  #No longer needed, but left in case we need it again.
  #  def copy(self):
      #copy = Character(self.name, self.HP, self.SP, self.MaxSP, self.MP, self.MaxMP, self.SocialPresence, self.SocialHeart, self.SocialStability, self.PhysicalGrace, self.PhysicalSkill, self.PhysicalPoise, self.MagicalAffinity, self.MagicalControl, self.MagicalConcentration)
  #   return copy
  
  #Applies a character's effects on them. Returns a dictionary with the new stats.
  def applyEffects(self):
    newGrace = self.PhysicalGrace
    newSkill = self.PhysicalSkill
    newPoise = self.PhysicalPoise
    newPresence = self.SocialPresence
    newHeart = self.SocialHeart
    newStability = self.SocialStability
    newAffinity = self.MagicalAffinity
    newControl = self.MagicalControl
    newConcentration = self.MagicalConcentration

    i = 0
    while i < len(self.Effects):
      effect = self.Effects[i]
      effect.duration -= 1
      if effect.duration == 0:
        del self.Effects[i]
        #If the effect is removed, a new effect will now be at the same index- Should not increment i
      else:
        self.HP -= effect.Damage
        newGrace -= effect.PhysReduct
        newSkill -= effect.PhysReduct
        newPoise -= effect.PhysReduct
        newPresence -= effect.MentReduct
        newHeart -= effect.MentReduct
        newStability -= effect.MentReduct
        newAffinity -= effect.MentReduct
        newControl -= effect.MentReduct
        newConcentration -= effect.MentReduct
        i += 1
    
    results = {
      "PhysicalGrace": newGrace, 
      "PhysicalSkill": newSkill, 
      "PhysicalPoise": newPoise, 
      "SocialPresence": newPresence, 
      "SocialHeart": newHeart, 
      "SocialStability": newStability, 
      "MagicalAffinity": newAffinity, 
      "MagicalControl": newControl, 
      "MagicalConcentration": newConcentration
    }
    return results
  
  def dealDamage(self, damage):
    self.HP -= damage
    if self.HP < 0:
      self.HP = 0
    elif self.HP > self.MaxHP:
      self.HP = self.MaxHP
    #The die check will take place in battleFinished()
  
  def setHP(self, health):
    self.HP = health

  def die(self):
    self.Deaths += 1
    if self.Deaths > self.MaxDeaths:
      return True
    return False