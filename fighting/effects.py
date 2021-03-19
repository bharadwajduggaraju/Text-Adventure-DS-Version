class Effect:
  def __init__(self, name, damage, duration, wounds, reduct_list=[0]*9, delay=0):
    self.Name = name
    self.Damage = damage
    self.Duration = duration
    self.isWounds = wounds
    self.Reducts = reduct_list
    if len(self.Reducts) < 9:
      self.Reducts += [0]*(9-len(self.Reducts))
    self.TimeReduct = delay
  
  #Instead of adding an effect type to a character's Effects list, add the instance returned by this. (Prevents modifying the effect type instace of Effect)
  def effectTypeInstance(self):
    effectTypeInstance = Effect(self.Name, self.Damage, self.Duration, self.isWounds, self.Reducts, self.TimeReduct)
    return effectTypeInstance
