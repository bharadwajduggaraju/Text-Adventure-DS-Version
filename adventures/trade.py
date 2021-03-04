# Class Added By Bharadwaj Duggaraju. Contact me if there is a bug

class Trade:
    def __init__(self, name, items):
      self.name = name  #String
      self.items = items  #List of Dicts, [{"name": "scarf", "itemsAccepted": []}]

    def trade(self, item_wanted, item_given): 
		# if item_wanted
      	pass
    

shopItems = [{"name": "scarf", "price": 33, "quantity": 2200}]
shopStats = [{
    "name": "scarf",
    "totalMoney": 0,
    "unitsSold": 0,
    "discount": False
}]

Trading_Post = ("Arctic Circle", shopItems, shopStats)

Trading_Post.getInfo()

buyandgetResponse = Trading_Post.buy("Arctic Circle", "scarf", 22, 69)

print(buyandgetResponse)
Trading_Post.getInfo()