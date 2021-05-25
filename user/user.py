# The Class Used To Create and Use Operations Regarding the User
# @Server -> Python
# @Database -> MongoDB
# @Team: Bharadwaj, Vedaant, Eesha, Joseph

import time
from user.hashpassword import hash_password
from user.config.connectdb import connectDB
from util.variable.variables import party, party_money, inventory, locations, tags
from util.variable.inventory import allItems
from narrative.nodes.read_file import generate_nodes

# from narrative.nodes.node import Node

#Joseph added these:
# from util.variable.inventory import inventory_update_from_user
# from util.variable.variables import variables_update_from_user
#name_update_from_user() takes in an instance of user and will update the variables in the appropriate file from it

USERS = connectDB() # Code Split (Get User Functions)

#USER_SCHEMA (Similar to Mongoose)
# @type - dict
# @format - {
#   username: String,
#   password: String,
#   data: {...data} @as Dict: Key Values Storing User Dtat
# }

def getUserWithUsername(username):
  return USERS.find_one({"username": username})

class User:
  def __init__(self, username, password, data=None):
    self.username = username
    self.password = password
    if data == None:
      self.data = {
        "party":party,
        "party_money":party_money,
        "inventory":inventory,
        "allItems":allItems,
        "locations":locations,    
        "tags":tags,
      }
    else:
      self.data = data
    self.createdat = time.asctime()
    self.createdUser = False
		
  def login():
    pass

  def getUserData(self): #@method: get (get the user data)
    return {
      "username": self.username,
      "password": self.password,
      "data": self.data,
      "createdAt": self.createdat,
      "created": self.createdUser
    }

  def saveData(self):
    self.data = {
			"party":party,
			"party_money":party_money,
			"inventory":inventory,
			"allItems":allItems,
			"locations":locations,    
			"tags":tags,
			# "node":Node.get_curr_node()
		}

  def getDataField(self, request):
    return self.data[request]

  def getField(self, field):
    return getattr(self, field)
		
  def createUser(self): #@method post (create the user)
    if(self.createdUser == True):
      raise Exception("User Already Created")
    else:
      USERS.insert_one({
        "username": self.username,
        "password": self.password,
        "data": self.data,
        "createdat": self.createdat
      }) #Insert the User Into the DB
      self.createdUser = True

  def updateAndPersist(self,newData) :#@method post (update locals and persist)
      db_username = self.username
      db_password = self.password
      db_data = self.data
      if ("username" in newData.keys()):
        db_username = newData["username"]
      if ("password" in newData.keys()):
        db_password = newData["password"]
      if("data" in newData.keys()):
        db_data = newData["data"]

      USERS.replace_one(
      {"username": self.username, "password": self.password},
      {"username": db_username, "password": db_password, "data": db_data, "createat": self.createdat}
      )

  def deleteAccount(self): #@method delete (delete account)
    USERS.delete_one({"username": self.username, "password": self.password})
    self.username = None
    self.password = None
    self.data = None
    self.createdat = None
    self.createUser = False
	
	

#Tests

#USERS.clear()

# KOSU_HASHED_PASSWORD = hash_password("esteriismyhalfsister")

# KOSU = User("Kosu", KOSU_HASHED_PASSWORD)
# KOSU.createUser() #the initial call to create to the database
# print(KOSU.getUserData()) #get the data
# KOSU.deleteAccount() #should delete (implemted with match id'Server)

# BHARADWAJ = User("Bharadwaj", hash_password("apassword"))
# BHARADWAJ.createUser()
# BHARADWAJ.updateAndPersist({
#   "username": "Bob"
# })





