inventory_number = 0
def get_id_number():
  global inventory_number

  inventory_number += 1;
  return inventory_number - 1;

allItems = {
  
}

'''
SYNTAX:
index = get_id_number()
allItems[index] = Item
'''