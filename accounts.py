from util.console.input import validate_int_input
from user.userFrontend import createUser
from narrative.nodes.read_file import generate_nodes
from narrative.nodes.node import get_cur_node
from util.console.input import delay_print
from util.console.output import clearConsole

currentUser = None

def runAccount():
  global currentUser
  currentUser = createUser()

runAccount()