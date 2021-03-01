from util.share_functions import funcs
validate_input = funcs["validate_input"]
validate_int_input = funcs["validate_int_input"]

class Quest:
  def __init__(self, startingStory, optionsToResults, tags, miniSideQuest):
    self.Tags = tags
    self.startingStory = startingStory
    self.optionsToResults = optionsToResults
    self.miniSideQuest = miniSideQuest

  #For mini-side-quests
  def miniSideQuest(self):
    print(self.startingStory)
    print("Here are your options: ")
    arr = []
    pos = 1
    for option in self.optionsToResults:
      arr.put(pos)
      print(pos + ": " + option)
      pos += 1
    
    answer = validate_int_input(arr, "Invalid")
    key = ""
    pos = 1

    for option in self.optionsToResults:
      if (pos == answer):
        key = option
        break
      pos += 1
    
    print(self.optionsToResults[key])

#def validate_input(accepted_list, errMessage, prompt = ""):
#  user_input = input().upper()
#  while (user_input not in accepted_list):
#    print(str(errMessage))
#    user_input = input().upper()
#  return user_input

#def validate_int_input(accepted_list, errMessage, prompt=""):
#  options = []
#  for option in accepted_list:
#    options.append(str(option))
#  answer = validate_input(options, errMessage, prompt)
#  return int(answer)