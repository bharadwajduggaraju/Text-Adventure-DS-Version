from commerce.item import Item
#Instances in util/instances.py, trauma in entities/traum.py

#Sample location
locations = {
  "Home": {
    "time": 0,
  },
  "Woods": {
    "time": 0,
  },
  "Cave": {
    "time": 0,
  }
}

party = []
party_money = 0
def get_money():
  return party_money
def set_money(new_money):
  global party_money
  party_money = new_money
def add_money(additional_money):
  global party_money
  party_money += additional_money
inventory = []

def add_party_member(party_member):
  party.append(party_member)
comparison_item = Item("Instance", "To check for type")

def add_item(name_or_item, description="", price=0, damageAmt=0):
  """Can either add values to make an item or directly pass in an Item instance"""
  #Uses global comparison_item
  if type(name_or_item) == type(comparison_item):
    item = name_or_item
  else:
    item = Item(name_or_item, description, price, damageAmt)
  inventory.append(item)
def remove_item(item_name, count=1):
  """Removes count number of items with the given name. Returns the number of items removed"""
  removed_items = 0
  i = 0
  while i < len(inventory):
    if inventory[i].Name == item_name:
      del inventory[i]
      removed_items += 1
      if removed_items == count:
        return removed_items
    else:
      i += 1 #deletion makes incrementing i unnecessary
  return removed_items

long = 0.025 #These 3 may get moved to where delay_print is defined
punc_delays = {',': 3, '(': 4, ')': 4, ';': 4, ':': 5, '.': 5, '?': 5, '!': 5}
punc_pause = True
