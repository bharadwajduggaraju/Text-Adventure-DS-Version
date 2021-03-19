class Item:
  def __init__(self, name, description, price=0, damageHP=0):
    self.Name = name
    self.Description = description 
    self.Price = price
    self.DamageHP = damageHP

  def toString(self):
    string_value = ""
    if (self.Price != 0):
      string_value += "(" + self.Price + ") "
    string_value += self.Name + " - " + self.Description
    return string_value
  
  def use(self, person):
    person.dealDamage(self.damageHP)