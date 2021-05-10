#Import Libraries
import sys
import time
import os
import random
import pygame
from replit import audio

from combat.battle import Battle
from commerce.shop import Shop
from util.colors import *
from util.variables import *
from util.variables import party_money, add_party_member, add_item
from util.instances import *
from util.console.output import delay_print, loading_effect, clearConsole
from util.console.input import validate_input, validate_int_input, yes_no, tutorial, inventorymenu, settings, battle_tutorial
from commerce.trade import *
from commerce.trade import Trade
from entities.character import Character
#Making story list
story = []
with open("text/story.txt", "rt") as r:
  story = r.readlines()
#Count for story line number
count_story=0
#Character list and associated data
characters = {}
character_info = []
characters_num = 0
#Translation
clearConsole()
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
	elif "/clear" in story[count_story]:
		clearConsole()
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
			characters_num+=1
			#Add individual letters of specific line to list
			character_data = [char for char in story[count_story+count]]
			#Character data transfer to character list
			#Prep
			count_letters=0
			character_name=""
			#Checking for name to add to list variable key
			while count_letters < len(character_data) and character_data[count_letters]!=":":
				character_name+=character_data[count_letters]
				count_letters+=1
			character_info.append(character_name)
			count_letters+=1
			#Checking for stats to add to corresponding variable key
			while count_letters < len(character_data):
				#Checking for
				if character_data[count_letters] != "," and character_data[count_letters] != "\n" and character_data[count_letters] != " ":
					character_info.append(character_data[count_letters])
				count_letters+=1
			#Character list updated
			character=Character(character_info[0],  character_info[1],character_info[2], character_info[3], character_info[4], character_info[5], character_info[6], character_info[7], character_info[8], character_info[9], character_info[10], character_info[11], character_info[12], character_info[13], character_info[14], character_info[15], character_info[16], character_info[17], character_info[18], character_info[19], character_info[20], character_info[21], character_info[22])
			characters.update({characters_num:character}) 
	#Move to next line
	count_story+=1