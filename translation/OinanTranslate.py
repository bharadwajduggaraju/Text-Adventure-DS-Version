#For translating to and from Oi'nan
from translation.dictionary import OiToEng

#Converts a string form of a list to a list
def listSplit(listStr):
  """Converts a string form of a list to a list"""
  listStr = listStr[1:-1] #Removes outside parentheses
  words = listStr.split(", ")
  return words

#Extracts the next word
def popFirstWord(text):
  """Returns lowercase first word, input text without the word, the last character, and a bool specifying if the word is title format"""
  word = ""
  i = 0
  while i < len(text):
    character = text[i]
    if character == ' ' or character == '\n':
      break
    else:
      word += character
      i += 1
  text = text[i+1:]
  return word.lower(), text, character, word.title()==word

#Checks is a character is valid
def isValidCharacter(character):
  """Returns a bool specifying if the character is a lowercase letter, space, newline, or apostrophe"""
  return ('a' <= character <= 'z') or (character == ' ') or (character == '\n') or (character == "'") or (character == "*")

#For removing the punctuation
def removeExtraCharacters(text):
  """Returns a version of the input text without invalid characters (according to isValidCharacter) and the invalid characters."""
  fin = ""
  extraCharacters = ""
  for r in range(len(text)):
    if isValidCharacter(text[r].lower()):
      fin += text[r]
    else:
      extraCharacters += text[r]
  
  return fin, extraCharacters

EngToOi = {}
def addEngEntry(OiPhrase, EngText):
  """Adds the appropriate English entry with the first word of EngText as the key, the continuation of EngText as the subkey, and OiPhrase as the subvalue."""
  global EngToOi
  results = popFirstWord(EngText)
  firstWord = results[0]
  EngText = results[1]
  try:
    EngToOi[firstWord][EngText] = OiPhrase
  except KeyError: #If EngToOi[firstWord] hasn't been made
    EngToOi[firstWord] = {EngText: OiPhrase}
printDict = False

def makeEngToOi():
  #Creates a new dictionary with reversed keys and values
  OiToEngKeys = OiToEng.keys()
  for key in OiToEngKeys:
    for subKey in OiToEng[key].keys():
      EngValue = OiToEng[key][subKey]
      phrase = key
      if subKey != "":
        phrase += ' ' + subKey
      if EngValue[0] == '(': #If the value starts with a left parentheses (has multiple meanings)
        words = listSplit(EngValue)
        for EngWord in words:
          if printDict: #Testing
            print(phrase+':', EngWord)
          addEngEntry(phrase, EngWord)
      else:
        if printDict:
          print(phrase+':', EngValue)
        addEngEntry(phrase, EngValue)

def get_lang():
  lang = ""
  while lang != "oi'nan" and lang != "english" and lang != "see dict": #Last is for testing
    lang = input("Select input language: (\"Oi'nan\" or \"English\") ").lower()
    lang = removeExtraCharacters(lang)[0]
    if (lang == "o") or (lang == "oi"):
      lang = "oi'nan"
    elif (lang == "e") or (lang == "en") or (lang == "eng"):
      lang = "english"
  return lang

fromOi = False

def translate_text(text):
  #Loops through text, identifying each word and then translating
  newText = ""
  suffix = ""
  while len(text) > 0:
    word, text, character, isTitle = popFirstWord(text)
    word, extraChars = removeExtraCharacters(word)
    newWord = ""
    if fromOi:
      dictionary = OiToEng
      while len(word) >= 3 and word[-3:] == "'ne":
        newWord += "of "
        word = word[:-3]
    else:
      dictionary = EngToOi
      if word == "of":
        suffix += "'ne"
        continue
    
    try:
      phrases = dictionary[word].keys()
      for phrase in phrases:
        if (extraChars!="") and (phrase!=""):
          continue
        if text[:len(phrase)].lower() == phrase:
          newWord += dictionary[word][phrase] + suffix
          suffix = ""
          text = text[len(phrase):]
          break
    except KeyError:
      if word != "":
        newWord += str(word) + "(?)"
    
    if isTitle:
      newWord = newWord.title()
    newText += newWord + extraChars + character
  return newText
'''
madeEngToOi = False
exit = True
while not exit:
  #Language selection
  lang = get_lang()
  fromOi = (lang=="oi'nan")
  printDict = (lang=="see dict")

  if not fromOi and not madeEngToOi:
    makeEngToOi()
    madeEngToOi = True

  #Gets multi-line input from the user
  print("\nType section here (Enter an empty line to translate, and type \"exit\" to leave the program):")
  text = ""
  words = input()
  while words != "":
    text += words + '\n'
    words = input()

  if text == "exit\n":
    #break
    exit = True
    continue
  newText = translate_text(text)
  newText = newText[:-1] #Removes the last character

  print(newText)
'''