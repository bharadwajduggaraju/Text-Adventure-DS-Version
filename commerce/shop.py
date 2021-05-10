# Class Added By Bharadwaj Duggaraju. Contact me if there is a bug
import sys
sys.path.append("../")
from util.console.input import *
from util.console.input import validate_int_input
from util.console.output import delay_print, clearConsole
from util.variable.inventory import allItems
from util.colors import *

class Shop:
    def __init__(self, name, items, itemsSold):
        self.name = name  #String
        self.itemsSold = itemsSold  #Llist of Dicts,
        self.items = items  #List of Dicts, [{"item": {"price": "$22", "quantity": 122}}]

        for item in items:
            allItems[item["name"]] = item

    def buy(self, name, item, quantity, playermoney):
        if (name == self.name):
            ind = 0
            finalind = -1
            for i in self.items:
                if (i["name"] == item):
                    finalind = ind
                    break
                ind += 1
            if (finalind == -1):
                return {
                    "status": "Item not found",
                    "customerMoneyLeft": playermoney
                }
            else:
                singleMoney = self.items[finalind]["price"]
                totalMoneyNeeded = singleMoney * quantity

                if (quantity > self.items[finalind]["quantity"]):
                    return {
                        "status": "Out of Stock",
                        "customerMoneyLeft": playermoney
                    }

                elif (totalMoneyNeeded > playermoney):
                    return {
                        "status":
                        "Not enough money. You need " +
                        str(totalMoneyNeeded - playermoney) +
                        " more dollars",
                        "customerMoneyLeft":
                        playermoney
                    }

                else:
                    self.items[finalind]["quantity"] -= quantity
                    self.itemsSold[finalind]["unitsSold"] += quantity
                    self.itemsSold[finalind][
                        "totalMoney"] += totalMoneyNeeded

                    return {
                        "status": "success",
                        "customerMoneyLeft": playermoney - totalMoneyNeeded
                    }

        else:
            return {
                "status": "You cannot access this store",
                "customerMoneyLeft": playermoney
            }

    def print_raw_data(self):
        print(self.items)
        print(self.itemsSold)

    def sell(self, userMoney):
        purchaseSuccessful = False
        while not purchaseSuccessful:
          itemsToBuy = validate_int_input(
              range(1, len(self.items) + 1), "Invalid input. ",
              "Which item do you want to buy (type the number)? ")
          itemCount = self.items[itemsToBuy - 1]["quantity"]
          quantityDisplay = ("" if itemCount > 1 else
                            "") + str(itemCount) + " items left"
          print("-"*10)
          quantity = abs(validate_int_input(range(0, itemCount+1), "Not that many items.", "How much of that item do you want? (" + quantityDisplay + ") "))
          #quantity = abs(int(
          #    input("How much of that item do you want? (" + quantityDisplay +
          #          ") ")))

          purchaseResults = self.buy(self.name,
                                    self.items[itemsToBuy - 1]["name"],
                                    quantity, userMoney)
          purchaseStatus = purchaseResults["status"]
          if purchaseStatus != "success":
              print(RED+"Purchase failed: " + purchaseStatus + RESET)
              print("-"*10)
          else:
              print("-"*10)
              print("Purchase successful.")
              print(GREEN+"You now have " + str(purchaseResults["customerMoneyLeft"]) + " money left.")
              purchaseSuccessful = True

    def getInfo(self, userMoney):
        clearConsole()
        delay_print(GREEN+"------ Welcome to the " + self.name + " Store ------")
        delay_print("Here are the items available:")
        counter = 1
        for i in self.items:
            delay_print(
                str(counter) + ". " + i["name"] + ": $" + str(i["price"]))

        self.sell(userMoney)

# shopItems = [{"name": "scarf", "price": 33, "quantity": 2200}]
# shopStats = [{
#     "name": "scarf",
#     "totalMoney": 0,
#     "unitsSold": 0,
#     "discount": False
# }]

# WinterShop = Shop("Arctic Circle", shopItems, shopStats)

# WinterShop.getInfo()

# buyandgetResponse = WinterShop.buy("Arctic Circle", "scarf", 22, 69)

# print(buyandgetResponse)
# WinterShop.get:
