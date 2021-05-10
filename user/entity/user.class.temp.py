# def createUser():
#   print("Welcome! Type the number of the option you want: ")
#   print("1. Log in with an existing account")
#   print("2. Create a new account")
#   print("3. Exit")

#   answer = validate_int_input([1, 2], "Please enter 1 or 2", "")
#   if (answer == 1):
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")

#     if (contains(username) and db[username] == hash_password(password)):
#       print("Successfully logged in!")
#       #Do log in stuff here
#     else:
#       print("Invalid username or password.")
#       time.sleep(1)
#       createUser()
#   elif answer == 3:
#     sys.exit(0)
#   else:
#     username = input("Enter your username: ")
#     if (contains(username)):
#       print("Username already exists.")
#       time.sleep(1)
#       createUser()
#     else:
#       password = hash_password(input("Enter your password"))
#       #Other information here will probably include location, inventory, etc.
#       user = User({"password": password}, username)
#       user.createUser()

