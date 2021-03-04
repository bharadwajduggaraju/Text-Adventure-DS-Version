from util.console.input import validate_int_input

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
