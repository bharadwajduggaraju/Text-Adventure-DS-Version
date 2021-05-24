from util.console.input import validate_int_input
from user.hashpassword import hash_password
import time, sys
from user.user import User
from user.config.connectdb import connectDB

currentUser = None #NEED TO BE MOVED LATER - ONLY PLACED HERE FOR TEMPORARY

def getUserWithUsername(username):
  return connectDB().find_one({"username": username})

def createUser():
  print("Welcome! Type the number of the option you want: ")
  print("1. Log in with an existing account")
  print("2. Create a new account")
  print("3. Exit")

  answer = validate_int_input([1, 2], "Please enter 1 or 2", "")
  
  if (answer == 1):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user = getUserWithUsername(username)

    if (user != None and user["password"] == hash_password(password)):
      print("Successfully logged in!")
      currentUser = user
    else:
      print("Invalid username or password.")
      time.sleep(1)
      createUser()
  elif answer == 3:
    sys.exit(0)
  else:
    username = input("Enter your username: ")
    if (getUserWithUsername(username) != None):
      print("Username already exists.")
      time.sleep(1)
      createUser()
    else:
      password = hash_password(input("Enter your password"))
      #Other information here will probably include location, inventory, etc.
      user = User({"password": password}, username)
      currentUser = user