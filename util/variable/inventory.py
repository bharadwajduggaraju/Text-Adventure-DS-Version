from commerce.item import Item
inventory_number = 0
allItems = {
  
}

def get_id_number():
  global inventory_number

  inventory_number += 1;
  return inventory_number - 1;

def getItem(name=None, description=None):
  for item in allItems.values():
    if (name != None and item.name == name):
      return item
    elif (description != None and item.description == description):
      return item
  return "Invalid"

#The passed in item here will be of the Item class
def addItem(item):
  if (getItem(name=item.Name) != "Invalid"):
    item.Quantity += 1
  else:
    index = get_id_number()
    allItems[index] = item

#The passed in item here will be inputs for Item class
#name, description, quatity=1, price=0, damageHP=0
def addItem(name, description, quantity=1, price=0, damageHP=0):
  output = getItem(name=name)
  if (output == "Invalid"):
    newItem = Item(name, description, quantity, price, damageHP)
    index = get_id_number()
    allItems[index] = newItem
  else:
    output.Quantity += 1
#Python rework of addItem version 1:
# def addItemInstance(item):
  # [Insert body of first addItem version]
# def addItemFromData(name, description, quantity=1, price=0, damageHP=0):
  # [Insert body of second addItem version]

# referenceItem = Item("An instance", "Use for type comparison")
# def addItem(name_or_item, description=None, quantity=1, price=0, damageHP=0): #Sadly, Python doesn't support function overloading, so this has to be one function
  # if type(name_or_item) == type(referenceItem): #Could also have a required argument specifying the mode
    # addItemInstance(name_or_item)
  # elif description == None: #Not an item, description required.
    # raise TypeError("Must specify description when name_or_item is not an Item instance")
  # else:
    # addItemFromData(name_or_item, description, quantity, price, damageHP)

#Second Python rework of addItem:
# referenceItem = Item("An instance", "Use for type comparison")
# def addItem(name_or_item, description=None, quantity=1, price=0, damageHP=0):
  # if type(name_or_item) == type(referenceItem): #Again, required argument specifying mode also works
    # item = name_or_item
    # name = item.Name
  # elif description == None: #Same as in addItem
    # raise TypeError("Must specify description when name_or_item is not an Item instance")
  # else:
    # name = name_or_item
    # item = Item(name, description, quantity, price, damageHP)
  
  # output = getItem(name) #Unless you think the order  will change, it's fine to use positional arguments
  # if output == "Invalid":
    # key = get_id_number() #It's technically a key, not an index (though the syntax is the same), by the way
    # allItem[key] = newItem
  # else:
    # output.Quantity += 1 #I'm not sure if it should be incremented by 1 or by the quantity parameter

#Delete by accessing the id number
def delete_item(id):
  if not (id in allItems.keys()):
    return "ErrorNotFound";
  allItems.get(id).Quantity -= 1
  if (allItems.get(id).Quantity <= 0):
    allItems.remove(id)

def inventory_update_from_instance(user_instance):
  global allItems
  allItems = user_instance.getData("allItems");