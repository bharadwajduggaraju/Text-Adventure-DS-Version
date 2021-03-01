class Item:
  def __init__(self, name, description, price, damageHP=0):
    self.Name = name
    self.Description = description 
    self.Price = price 
    self.DamageHP = damageHP

  def toString(self):
    if (self.Price != 0):
      return "(" + self.Price + ")" + " " + self.Name + " - " + self.Description
    return self.Name + " - " + self.Description
  
  def dealDamage(self, person):
    person.dealDamage(self.damageHP)