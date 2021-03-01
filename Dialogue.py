r = open("Story.txt", "rt")
if "#" in r.readline():
	print(r.readline())

#Proposal:
#with open("Story.txt", "rt") as r: #First proposal: using with to make sure it closes even in case of later error
  #line = r.readline() #Second: Storing the line in a variable
  #if line[0] == "#": #Third: Only checking the first character
    #print(line)