#Use this file to simulate importing files from main

# from user.user import getDB

# getDB()

# import util.variable.inventory as inventory

# from narrative.nodes.read_file import generate_nodes
from narrative.nodes.hub import is_valid_float

if __name__ == "__main__":
  # inventory.addItem("Test", "A test")
  # sections = test("narrative/test.txt")
  # print(sections)
  # node_dict, variables = generate_nodes("narrative/test2.txt")
  # node_dict["main"].traverse(variables)

  for test_str in ("0", "5", "+0", "-5", "50", "-05.", "+50.1"):
    print("{0:8}{1}".format(test_str, is_valid_float(test_str)))
