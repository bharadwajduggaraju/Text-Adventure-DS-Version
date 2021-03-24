class Enemy:
  def __init__(self, name, maxHP, HP, timeGiven, AC, damage, effects=[]):
    self.Name = name
    self.MaxHP = maxHP
    self.HP = HP
    self.TimeGiven = timeGiven
    self.AC = AC
    self.Damage = damage
    self.Effects = effects

  def turn(self, party):
    self.applyEffects()
    target = None
    max_presence = -1
    for character in party:
      presence = character.SocialPresence
      if presence > max_presence:
        max_presence = presence
        target = character

    print(self.Name + " dealt " + str(self.Damage) + "HP damage to " + target.Name)
    target.dealDamage(self.Damage)
  
  def dealDamage(self, damage):
    self.HP -= damage
    if self.HP < 0:
      self.HP = 0
    elif self.HP > self.MaxHP:
      self.HP = self.MaxHP
    #The die check will take place in battleFinished()
  
  def setHP(self, newHP):
    self.HP = newHP
  
  #Makes a copy for individual enemies
  def copy(self):
    copy = Enemy(self.Name, self.MaxHP, self.HP, self.TimeGiven, self.AC, self.Damage)
    return copy

  #Effects fields: Name, Damage, Duration, isWounds, Reducts, TimeReduct
  def applyEffects(self):
    i = 0
    while i < len(self.Effects):
      effect = self.Effects[i]
      effect.duration -= 1
      if effect.duration == 0:
        del self.Effects[i]
        #If the effect is removed, a new effect will now be at the same index- Should not increment i
      else:
        self.HP -= effect.Damage
        self.TimeGiven -= effect.TimeReduct
        i += 1