class Effect:
  def __init__(self, name, damage, duration, wounds, phys=0, ment=0, delay=0):
    self.Name = name
    self.Damage = damage
    self.Duration = duration
    self.isWounds = wounds
    self.PhysReduct = phys
    self.MentReduct = ment
    self.TimeReduct = delay
  
  #Instead of adding an effect type to a character's Effects list, add the instance returned by this. (Prevents modifying the effect type instace of Effect)
  def effectTypeInstance(self):
    effectTypeInstance = Effect(self.Name, self.Damage, self.Duration, self.isWounds, self.phys, self.ment)
    return effectTypeInstance
