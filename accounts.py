from util.console.input import validate_int_input
from user.userFrontend import createUser
from util.console.input import delay_print
from util.console.ouput import clearConsole
currentUser = None

def runAccount():
  createUser()

runAccount()