def translate():
	#Txt file data transfer to list
	r = open("Story.txt", "rt")
	story=[r.readlines()]
	#Count for story line number
	count_story=0
	#Character list and associated data
	characters = []
	#Translation
	while count_story < len(story) and "/end story" not in story[count_story]:
		#Lowered text
		lower = story[count_story].lower()
		#Print translation
		if "#" == story[count_story][0]:
			if "# " not in story[count_story]:
				printable=story[count_story].replace("#","")
			else:
				printable=story[count_story].replace("# ","")
			print(printable)
		#Character data accumilation
		elif "characters:" in lower:
			#Count for lines past current line
			count=0
			#Character translation loop
			while "/end characters" not in story[count_story+count]:
				#Move to next line
				count+=1
				#Check for end of loop
				if count_story+1<len(story) and "/end characters" in story[count_story+count]:
					break
				#Add individual letters of specific line to list
				character_data = [char for char in story[count_story+count]]
				#Character data transfer to character list
				#Prep
				count_letters=0
				character_name=""
				stats=[]
				#Checking for name to add to list variable key
				while count_letters < len(character_data) and character_data[count_letters]!=":":
					character_name+=character_data[count_letters]
					count_letters+=1
				count_letters+=1
				#Checking for stats to add to corresponding variable key
				while count_letters < len(character_data):
					#Checking for
					if character_data[count_letters] != "," and character_data[count_letters] != "\n" and character_data[count_letters] != " ":
						stats.append(int(character_data[count_letters]))
					count_letters+=1
				vars()[character_name]=[character_name]
				vars()[character_name]+=stats
				#Character list updated
				characters.append(vars()[character_name])
				print(characters)
		#Move to next line
		count_story+=1