# Class Added By Bharadwaj Duggaraju. Contact me if there is a bug
from util.colors import * 
from util.console.input import validate_int_input
from util.console.output import delay_print, clearConsole

class Trade :
    def __init__(self, name, items):
      self.name = name  #String
      self.items = items  #List of Dicts, [{"name": "scarf", "itemsAccepted": []}]

    def trade(self, item_wanted, item_given):
      status_dict = {"status": ""}
      if item_wanted not in self.items:
        status_dict["status"] = "Item not found"
        return status_dict

        
    def beginTrade(self, playerInventory):
      clearConsole()
      delay_print(GREEN + "------ Welcome to the " + self.name + " Trading Post ------" + GREEN)
      delay_print("Here are the items available to trade for:")
      counter = 1
      for i in self.items:
          delay_print(str(counter) + ". " + i["name"])
          counter += 1
      itemIndex = validate_int_input(range(1, counter), "Invalid input.", "Which item do you want to trade for? (Enter the number) ") - 1
      tradedItem = self.items[itemIndex]

      delay_print("Your Inventory:")
      acceptedInventoryIndices = [] #1-based indices
      counter = 1
      for item in playerInventory:
        if item in tradedItem["itemsAccepted"]:
          acceptedInventoryIndices.append(counter)
        delay_print(str(counter) + ". " + item)
        counter += 1
      UserTradeProp = validate_int_input(acceptedInventoryIndices, "Invalid input.", "Which item do you want to trade away? (Enter the number) ")

      itemGiven = playerInventory[UserTradeProp-1]

      self.trade(tradedItem, itemGiven)

    

      



    

      
    



    



