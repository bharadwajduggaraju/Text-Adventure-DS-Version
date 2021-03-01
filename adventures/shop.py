##Class Added By Bharadwaj Duggaraju. Contact me if there is a bug

class Shop:
    def __init__(self, name, items, itemsSold):
        self.name = name  #String
        self.itemsSold = itemsSold  #Llist of Dicts,
        self.items = items  #List of Dicts, [{"item": {"price": "$22", "quantity": 122}}]

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
                return {"status": "Item not found", "customerMoneyLeft": playermoney}
            else:
                singleMoney = self.items[finalind]["price"]
                totalMoneyNeeded = singleMoney * quantity
                if (totalMoneyNeeded > playermoney):
                    return {"status": "Not enough money. You need" + str(totalMoneyNeeded-playermoney) + " more dollars", "customerMoneyLeft": playermoney}

                else:
                    if (quantity > self.items[finalind]["quantity"]):
                        return {"status": "Out of Stock", "customerMoneyLeft": playermoney}

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
            return "You cannot access this store"

    def getInfo(self):
        print("------ Welcome to the " + self.name + " Store ------")
        print("Here are the items available:")
        counter = 1
        for i in self.items:
            print(str(counter) + ". " + i["name"] + ": $" + str(i["price"]))


shopItems = [{"name": "scarf", "price": 33, "quantity": 2200}]
shopStats = [{
    "name": "scarf",
    "totalMoney": 0,
    "unitsSold": 0,
    "discount": False
}]

WinterShop = Shop("Arctic Circle", shopItems, shopStats)

WinterShop.getInfo()

buyandgetResponse = WinterShop.buy("Arctic Circle", "scarf", 22, 69)

print(buyandgetResponse)
WinterShop.getInfo()