# Class Added By Bharadwaj Duggaraju. Contact me if there is a bug
from util.colors import * 
from util.console.input import validate_int_input
from util.console.output import delay_print, clearConsole

class Trade :
    def __init__(self, name, items):
      self.name = name  #String
      self.items = items  #List of Dicts, [{"name": "scarf", "itemsAccepted": []}]

    def trade(self, item_wanted, item_given, current_player_inventory):
      status_dict = {"status": "", "player_inventory": current_player_inventory}
      if item_wanted not in self.items:
        status_dict["status"] = "Item not found"
        return status_dict
      else:
        self.items.remove(item_wanted);
        current_player_inventory.remove(item_given)
        status_dict["status"] = "Succesfully Traded"
        status_dict["player_inventory"] = current_player_inventory
        return status_dict

        
    def beginTrade(self, playerInventory):
      clearConsole()
      delay_print(GREEN + "------ " + self.name + " ------" + GREEN)
      delay_print("Items Available:")
      counter = 1
      for i in self.items:
          delay_print(str(counter) + ". " + i["name"])
          counter += 1
      itemIndex = validate_int_input(range(1, counter), "Invalid input.", "Which item do you want to purchase? (Enter the number) ") - 1
      tradedItem = self.items[itemIndex]

      delay_print("Your Inventory:")
      acceptedInventoryIndices = [] #1-based indices
      counter = 1
      for item in playerInventory:
        if item in tradedItem["itemsAccepted"]:
          acceptedInventoryIndices.append(counter)
        delay_print(str(counter) + ". " + item)
        counter += 1
      UserTradeProp = validate_int_input(acceptedInventoryIndices, "That item is not accepted.", "Which item do you want to sell? (Enter the number) ")

      itemGiven = playerInventory[UserTradeProp-1]

      attempted_trade = self.trade(tradedItem, itemGiven, playerInventory)

      if(attempted_trade["status"] == "Item not found"):
        delay_print(RED+"Failed To Find Item")
        return attempted_trade["player_inventory"]
      else:
        delay_print(GREEN+"--Succesfully Traded---")
        clearConsole()
        return attempted_trade["player_inventory"]
