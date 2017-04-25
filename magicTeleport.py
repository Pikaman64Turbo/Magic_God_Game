import time
from sys import exit
import pickle
from random import randint
	#Ditched the idea of importing, it would be much easier to dump code from Pouch.py to magicTeleport.py
#from Pouch import wpnChange

#import Pouch


#array_areaArena = [(0,0),(0,1),(1,0),(1,1),(1,-1),(0,1),(0,2),(1,2),(2,1),(2,2),(3,1),(3,2),(4,1),(4,2),(1,-2),(0,-1),(0,-2),(3,0),(4,0),(2,-1),(2,-2),(3,-1),(3,-2),(4,-1),(4,-2)]

#This array information is used for inventory.

array_godPouch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array_godPouch[0] = "Fist"
array_godPouch[1] = "[empty]"
array_godPouch[2] = "[empty]"
array_godPouch[3] = "[empty]"
array_godPouch[4] = "[empty]"
array_godPouch[5] = "[empty]"
array_godPouch[6] = "[empty]"
array_godPouch[7] = "[empty]"
array_godPouch[8] = "[empty]"
array_godPouch[9] = "[empty]"
array_godPouch[10] = "[empty]"

#AllowMov_y = true
#AllowMov_x = true
#AllowBac_y = true
#AllowBac_x = true

whileVar = 0
gender = ""
gender1 = "it"
gender2 = "its"
gender3 = "it"
plazmaI = "Electrocution I"
testK = "Beta Knife"
playNom = ""
woldNom = ""
moralChoice1 = "Yes"
Town = "Existance"
tehArea = 1
DefunctClone = False
BedFalse = False
Summon = 3
shield1 = "Wooden Shield"
bamb = "Fused Bomb"
TownNom = False
Purpose = "Pure"
DefunctCloneDED = False
ClensedClone = False

#

class PlayerData:
		def __init__(self, playNom, woldNom, gender, gender1, gender2, gender3, Town, array_godPouch, tehArea, DefunctClone, TownNom, DefunctCloneDED, Purpose, ClensedClone):
			self.playNom = playNom
			self.woldNom = woldNom
			self.gender = gender
			self.gender1 = gender1
			self.gender2 = gender2
			self.gender3 = gender3
			self.Town = Town
			self.array_godPouch = array_godPouch
			self.tehArea = tehArea
			self.DefunctClone = DefunctClone
			self.DefunctCloneDED = DefunctCloneDED
			self.Purpose = Purpose
			self.ClensedClone = ClensedClone
			self.TownNom = TownNom

Player1 = PlayerData(playNom, woldNom, gender, gender1, gender2, gender3, Town, array_godPouch, tehArea, DefunctClone, TownNom, DefunctCloneDED, Purpose, ClensedClone)

def Save1():
	Player1 = PlayerData(playNom, woldNom, gender, gender1, gender2, gender3, Town, array_godPouch, tehArea, DefunctClone, TownNom, DefunctCloneDED, Purpose, ClensedClone)
	Saving = input("What will you name your save game? ->")
	with open("{}.pickle".format(Saving), 'wb') as f:
		pickle.dump(Player1, f)
	print("Your world has been saved... for now.")

def Load1():
	Saving = input("What file.pickle will you load? (Name of save game) ->")
	with open('{}.pickle'.format(Saving), 'rb') as f:
		Player1 = pickle.load(f)
	playNom = Player1.playNom
	woldNom = Player1.woldNom
	gender = Player1.gender
	gender1 = Player1.gender1
	gender2 = Player1.gender2
	gender3 = Player1.gender3
	Town = Player1.Town
	array_godPouch = Player1.array_godPouch
	tehArea = Player1.tehArea
	DefunctClone = Player1.DefunctClone
	DefunctCloneDED = Player1.DefunctCloneDED
	Purpose = Player1.Purpose
	ClensedClone = Player1.ClensedClone
	TownNom = Player1.TownNom
	print("Welcome back, {}!".format(playNom))
	tehArea = ""


def Swapp(tool):
	pickUp = input("Would you like to pick it up? (y or n)")
	if pickUp == "n":
		print("You were too lethargic to pick up the item.")
	elif pickUp == "y":
		for i in range (1, 10):
			if array_godPouch[i] == "[empty]":
				array_godPouch[i] = tool
				return array_godPouch
			elif array_godPouch[i] != "[empty]":
			 	replaceSlot = input("{}'s' has ran out of space in {} inventory, what slot shall you replace?".format(playNom, gender2))
			 	array_godPouch[int(replaceSlot)] = tool
			 	print(array_godPouch)

def itemSearch(itemUse):
	for i in range (1, 10):
		if array_godPouch[i] == itemUse:
			return True
	return False

def test0():
	testCheck1 = moralChoice1 = input("Absorb him? (Yes or No) ->")
	if moralChoice1 == "Yes":
		print("You have absorbed your clone, you monster!")
		timeOut(5)
		print("You have gained the {}!".format(plazmaI))
		Swapp(plazmaI)
	elif moralChoice1 == "No":
		print("\"Nevermind\" You tell your defunct clone.")
		timeOut(4)
		print("{} looks at you with wicked drabness, \"What?!\"".format(gender1))
		timeOut(4)
		print("\"You heard me fully, and I'm feeling benevolent.\" You tell {}.".format(gender1))
		timeOut(5)
		print("{}-sama pats {} defuct clone on the head. (+1 Morality)[not yet implemented]".format(playNom, gender2))
	else:
		print("You just walk away from the situation, wishing that this situation never happened.")

x = 0
y = 0
#Remember the WHILE Loop!!!

def timeOut(t):
	time.sleep(t)

def Options():
	print("Available Commands:")
	print("(look [Primary Cardinal direction]) This permits looking around your surroundings.")
	print("(move [Primary Cardinal direction]) This allows you to move.")
	print("(read [noun]) This allows you to inspect objects and people.")
	print("(punch [noun]) Use this to fight things.")
	print("(save game [1-10]) This allows you to save your progress.")
	if itemSearch(plazmaI):
		print("(zap [noun]) This barbacues almost anything.")
	print("(summon [ally]) This allows you to open a portal to summon an unlocked party member.")
	print("(pouch) This allows you to view your inventory.")

def swapGender():
	global gender
	gender = input("Are you a boy are a girl? ->")
	if (gender == "boy"):
		gender1 = "him"
		gender2 = "his"
		gender3 = "he"
		gender = "boy"
	elif (gender == "girl"):
		gender1 = "her"
		gender2 = "hers"
		gender3 = "she"
		gender = "girl"
	elif (gender == "meme"):
		print("Initiate the bogus.")
		gender1 = "Dem thang"
		gender2 = "ROFLS"
		gender3 = "???"
		gender = "meme"
		timeOut(3)
	else:
		print("That is not a gender, you need to see your local physician.")
		gender1 = "it"
		gender2 = "its"
		gender3 = "it"
		gender = "Random"

def globalCommand(tehGame, badcommandstring):
	tehGame = tehGame.lower()
	if tehGame == "swap gender":
		swapGender()
	elif tehGame == "commands":
		Options()
	elif tehGame == "save game":
		Save1()
		print("Your world has been saved... for now.")
	elif tehGame  == "pouch":
		print(array_godPouch)
	elif tehGame == "options":
		Options()
	else:
		print(badcommandstring)

# class Save1(object):
# 	name = "default name"

#     def __init__(self, woldNom, playNom, gender, gender1, gender2, gender3, Town):
#         self.woldNom = woldNom
#         self.playNom = playNom

# with open('company_data.pkl', 'wb') as :

#     company2 = pickle.load(input)
#     print(company2.name) # -> spam
#     print(company2.value)  # -> 42

#Test1()
tehGame = input("Would you like to load from a previous save or no? ->")
if tehGame == "yes":
	Load1()

elif tehGame == "no":
	timeOut(0.5)
	print ("Hello, human player!")
	timeOut (2)
	print ("Welcome to the world of ______. This is your life now.")
	timeOut(3)
	woldNom = input("What world do you live in? ->")
	print ("{} is filled with dangers in every corner. Realizm has escaped, and insanity is reality.".format(woldNom))
	timeOut(4)
	print ("This is the world that you have created, and you solely exist to rid the evils of {}.".format(woldNom))
	timeOut(5)
	print ("What I'm trying to say is {} is screwed.".format(woldNom))
	timeOut(4)
	print ("Your 'Good Deeds' are not defined in any vocabulary of mine, only you can define it. {} is on your shoulders.".format(woldNom))
	timeOut(6)
	print ("As a mortal god, it is your duty [and only your duty] to do 'Good Deeds'!")
	timeOut(3)
	playNom = input("I'm sorry, I forgot to ask for your name, God. ->")
	print ("Alright, {}-sama! The world of {} is in your hands. Do not waste your life!".format(playNom, woldNom))
	timeOut(4)
	print ("WAIT! I need to know something before we start.")
	timeOut(2)
	gender = input("Are you a boy are a girl? ->")
	gender = gender.lower()
	if (gender == "boy"):
		gender1 = "him"
		gender2 = "his"
		gender3 = "he"
		gender = "none"
	elif (gender == "girl"):
		gender1 = "her"
		gender2 = "hers"
		gender3 = "she"
	elif (gender == "meme"):
		print("Initiate the bogus.")
		gender1 = "Dem thang"
		gender2 = "ROFLS"
		gender3 = "???"
		timeOut(3)
	else:
		print("That is not a gender, you need to see your local physician.")
		gender1 = "it"
		gender2 = "its"
		gender3 = "it"

	print ("You are in your bedroom, try (examine Area) to see your immediate surroundings. Use (look South) to continue playing the game!")
	timeOut(1)
	print ("Use the \"Options\" command to see your available movement options")
	DefunctClone = False
	TownNom = False
	DefunctCloneDED = False
	ClensedClone = False
	tehArea = 1

else:
	print("Fine then, I'll destroy the previous worlds.")
	exit()


while tehArea == 1:
	BedFalse = False
	tehGame = input("	>")
	tehGame = tehGame.lower()
	if tehGame == "examine area":
		print ("Starting Home (Bedroom): Main {}-sama punished you to this realm.".format(playNom))
		timeOut(3)
		print ("During your exile, you put forth the last of your power to create {}. You hadn't created your living residence yet.".format(woldNom))
		timeOut(5)
		print ("You were dying. In the last-ditch attempt to save your name, you cloned yourself multiple times to preserve the last of your essence.")
		timeOut(6)
		print ("In the name of {}, you live with another version of yourself.".format(playNom))
		timeOut(4)
		print ("Surprisingly, the both of you were too lazy to create an actual house.")
		timeOut(2)
		print ("Type (Options) to bring up available commands.")
	elif tehGame == "look south":
		print ("There's a window that peers out into darkness. You assume that it's a void.")
		timeOut(6)
		print ("There is a letter above the window.")
		timeOut(4)
		print ("'You can examine any noun [people, things, buildings, places] with the (read) command, even questionable items like #windows# and #people#.'")
	elif tehGame == "punch clone" or tehGame == "punch defunct clone":
		if DefunctCloneDED == False:
			if DefunctClone == False:
				print("You punch you clone in the face.")
				timeOut(3)
				print("{COMBAT INITIATED}")
				timeOut(1)
				print("{} zaps you by summoning lightning from {} fingertips.".format(gender3, gender2))
				timeOut(2)
				print("Your torso is charred!")
				tehGame = input("You can: (Punch) (Flee) ->")
				if tehGame == "punch":
					print("You punch harder!!")
					timeOut(2)
					print("Defunct Clone: Massive damage to the cranium")
					timeOut(2)
					print("It's not enough!")
					timeOut(2)
					print("Your defunct clone commits an uppercut.")
					timeOut(2)
					print("You: Medium damage to the neck.")
					timeOut(1)
					print("You're flung up into the air.")
					timeOut(2)
					print("{CHANCE OF DEATH}")
					timeOut(5)
					print(".")
					timeOut(1)
					print("..")
					timeOut(1)
					print("...")
					Chance_of_Death = randint(1,2)
					if Chance_of_Death == 1:
						print("You hit your head.")
						timeOut(2)
						print("You died to your neck snapping.")
						timeOut(2)
						print("(Died to Defunct Clone) hint: do not mess with a guy with lightning powers.")
						exit()
					elif Chance_of_Death == 2:
						print("You stick the landing!!")
					tehGame = input("You can: (Punch) or (Mercy) ->")
					if tehGame == "punch":
						print("You deliver the final punch!")
						timeOut(2)
						print("Defunct Clone: Fatal Damage!!!")
						timeOut(2)
						print("\"Why do you hate me--so...\" Were your defunct clone's last words.")
						timeOut(3)
						print("You absorb your Defunct Clone's carcass.")
						timeOut(3)
						print("You gain the power of Electrocution 1 and Beta Knife!")
						Swapp(plazmaI)
						Swapp(testK)
						print("Your wounds automatically heal.")
						timeOut(3)
						print("Your thoughts twist and churn.")
						timeOut(3)
						print("You feel an intence migrain.")
						timeOut(3)
						print("\"I just committed murder... I killed a. living. thing.\" Thoughts continue to pop up in your soul.")
						timeOut(9)
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						print("\"Oh my god.\"")
						timeOut(0.5)
						print("\"I committed a sin!!\"")
						timeOut(0.5)
						print("\"Can a god commit a sin?!")
						timeOut(0.5)
						timeOut("\"It feels good to kill...\"")
						timeOut(0.75)
						print("\"Am I even a god?\"")
						timeOut(0.5)
						print("\"I killed my clone!\"")
						timeOut(0.75)
						print("\"Murder feels good.\"")
						timeOut(0.5)
						print("\"Did I kill myself?")
						timeOut(0.5)
						print("\"If I'm a mortal, then why am I god.\"")
						timeOut(0.5)
						print("\"KILL ME!\"")
						timeOut(0.5)
						print("\"I killed a god...\"")
						timeOut(4)
						print("\"And...\"")
						timeOut(2)
						print("\"It.\"")
						timeOut(1)
						print("\"Felt.\"")
						timeOut(1)
						print("\"Good...\"")
						timeOut(3)
						print("\"Good.\"")
						timeOut(3)
						print("\"Gooood Deeeds...")
						timeOut(4)
						print(":-)")
						timeOut(7)
						print("Your purpose has changed from \"Pure\" to \"Corrupted Soul\"")
						Purpose = "Corrupted"
						DefunctCloneDED = True
					elif tehGame == "mercy":
						print("\"If you seize attack, I will stop my attack.\" You tell {}".format(gender2))
						timeOut(2)
						print("Your clone looks down at the floor and shakes his head, \"What are my benefits?\"")
						timeOut(4)
						print("\"Unlimited 'pizza'.\" You tell him.")
						timeOut(4)
						print("\"So, I get a slice of that religous pie of yours?\" {} reassures.".format(gender1))
						timeOut(5)
						print("\"Of coarse!!\"")
						timeOut(4)
						print("The defunct clone smiles, \"Then count me in!\"")
						timeOut(3)
						print("Defunct Clone joins your party!")
						DefunctClone = True
						timeOut(2)
						print("\"Here, have a Beta Knife.\" Your clone chucks the knife at you.")
						timeOut(2)
						Swapp(testK)
						timeOut(1)
						print("\"I now know my purpose, I must spread my good deeds.")
						timeOut(2)
						print("Your purpose has changed from \"Pure\" to \"Thug\".")
						Purpose = "Thug"
				elif tehGame == "flee":
					print("\"It's just a prank bro.\" You tell your defunct clone.")
					timeOut(4)
					print("Your defunct clone shakes {} head.".format(gender2))
					timeOut(3)
					print("\"I shead no mercy on a defunct clone of mine.\" {} tells you.".format(gender1))
					timeOut(7)
					print("The now true clone of {} electrocutes you.".format(playNom))
					timeOut(3)
					print("You: Fatal Damage!!!")
					timeOut(4)
					print("(Death by being owned) hint: do not mess with a clone of god.")
					exit()
				else:
					print("Shut up, I'm lazy!")
			else:
				print("You've already made peace with your Defunct Clone.")
		else:
			print("You can't fight a carcass.")
	elif tehGame == "read void":
		print ("You look at the void.")
		timeOut(3)
		print ("It stares back.")
	elif tehGame == "read letter":
		print("It reads: {You've figured out the puzzle! You're smarter than an average peasant!}")
		timeOut(4)
		print("{Did you know that you can (look) in any Primary Cardinal direction?}")
	elif tehGame == "look north":
		print("You found a door to the outdoors!") 
		timeOut(3)
		print("Why you were too lazy to create windows that look into said outdoors, {} may never know.".format(woldNom))
		timeOut(7)
		print("There's a post-it note above the door.")
	elif tehGame == "read post-it note" or tehGame == "read post-it":
		print("Congratulations! You solved the puzzle.")
		timeOut(3)
		print("\"Hey, {}-sama! This is a note from your evil version: you can combine Cardinal directions with the (move) command to move!!!\"".format(playNom))
		timeOut(8)
		print("\"To start out, type (move South).\"")
	elif tehGame == "look west":
		print("The typical rectangular red-and-white bed is located in the middle of the floor.")
		timeOut(5)
		print("You were too lazy to create smooth edges, let alone move it out from the wooden surface.")
		timeOut(6)
		print("There is nothing else of intrest here, as there is nothing else there.")
	elif tehGame == "look east":
		print("Your computer is located on the end of this room. {} is sitting on a chair playing a game on a command prompt.".format(playNom))
		timeOut(8)
		print("\"What a loser,\" You tell yourself, \"I need to stop making defunct clones about myself\"")
	elif tehGame == "read defunct clone" or tehGame == "read clone":
		print("Defunct {}-sama's a gamer, and it's {} entire purpose.".format(playNom, gender1))
		timeOut(4)
		print("Although, {} wasn't always that way... {} actually helped you create {}.".format(gender3, playNom, woldNom))
		timeOut(6)
		print("{} then started acting very weird, and now resides here replaying {} former glory.".format(gender3, gender1))
	elif tehGame == "move south":
		print("{}-sama ran South and jumped through the window, where {} were sucked into the infinite darkness.".format(playNom, gender1))
		timeOut(5)
		print("\"Me-darn it! Why is there an evil version of me?\" Were your last words.")
		timeOut(7)
		print("\"What a loser!\" The defunct clone of {} said while being glued into {} computer screen".format(woldNom, gender2))
		timeOut(5)
		print("(Death by Window) {} died by trusting the antagonist. (Hint, move North)".format(playNom))
		exit()
	elif tehGame == "soviet russia":
		print("In Soviet Russia, Putin plays you.")
		timeOut(4)
		print("Easter Egg 'Lincoln' Found!")
	elif tehGame == "read floor":
		print("You stand on a wooden planked floor.")
	elif tehGame == "read computer":
		print("print(\"You find a computer, but your defunct clone is using it right now.\")")
		timeOut(1)
		print("timeOut(5)")
		timeOut(5)
		print("print(\"\\\"Best not to bother {} right now.\\\" You tell yourself\").format(gender1)")
		timeOut(1)
		print("Easter Egg 'Kyle' found!")
	elif tehGame == "read bed":
		print ("This \"bed\" looks to be extreamly uncomfortable.")
		timeOut(3)
		print ("You attempt to clip the bed out from the floor. To no avail, you give up.")
		timeOut(5)
		print ("\"Videogames makes this look too easy.\" You think, \"I need to take notes.\"")
	elif tehGame == "move west":
		print("Without looking ahead, you move West and trip over your bed.")
		timeOut(5)
		print("\"Smooth move, idiot.\" {}'s clone shouts from the opposite end of the room.".format(playNom))
		timeOut(5)
		print("You don't bother to say anything as it would add fuel from the fire.")
	elif tehGame == "zap bed":
		if electorcuteBed == False:
			if itemSearch(plazmaI):
				print("In pure fustration, you destroy the bed with lightning.")
				timeOut(4)
				print("{} plumps down on the ashes, \"I've never felt so comfortable in my life\" You murmur.".format(playNom))
				print(6)
				print("You fall asleep, then awake by being consumed in soot.")
				timeOut(4)
				print("\"Yes.\" Your eyes water, \"A twenty year rest from toil.\"")
				timeOut(4)
				print("{} smiles.".format(playNom))
				timeOut(3)
				print("The bed magically regenerates.")
				BedFalse = True
			else:
				print("Thout shall not zap if one cannot electrocute.")
		else:
			print("You've already destroyed your bed. The ashes've already polluted the room.")
	elif tehGame == "sleep bed":
		if BedFalse == False:
			print("You plump down on the hard wooden surface.")
			timeOut(5)
			print("\"Wait a minute...\" You question.")
			timeOut(3)
			print("\"Wait a minute.....\"")
			timeOut(5)
			print("\"The floor is more comfortable than this!!\"")
			timeOut(6)
			print("{}'s defunct clone faceplams, \"That's why I created this chair! You were too busy creating the world that you skiped the conformaties!\"".format(playNom))
			timeOut(10)
			print("\"I'm not that lazy!\" You yell back at {}.".format(gender1))
			timeOut(3)
			print("\"You'd be surprised\" {} mouthsback, then returns to playing Epic Teleporter Adventure.".format(gender2))
			timeOut(5)
			print("Easter Egg 'Patrick' found!")
		else: 
			print("You plump down on the hard wood floor covered with ash.")
			timeOut(4)
			print("You immediatly regret everything.")
	elif tehGame == "read window" or tehGame == "read windows":
		print("You look at the windows, very intently.")
		timeOut(4)
		print("For the past hour, you reflect about your life.")
		timeOut(4)
		print("You continue to think deeply.")
		timeOut(5)
		print("\"Hmmm.\"")
		timeOut(4)
		print("\"HMMMMMMM...\"")
		timeOut(3)
		print("\"If I'm a mortal, why am I a god?\" You ask yourself.")
	elif tehGame == "zap window":
		if itemSearch(plazmaI):
			print("You destroy the window and the void engulfs everything.")
			timeOut(4)
			print("\"Infinite sadness will bestow upon my entire essance!\" Were your final words.")
			timeOut(7)
			print("(Death by Window) hint: Do not destroy everything.")
			exit()
		else:
			print("Do you want to die?!")
	elif tehGame == "zap computer":
		if itemSearch(plazmaI):
			print("You electrocute the computer. It violently explodes.")
			timeOut(5)
			print("\"Gaming sould die in a fire!\" {}-sama spew out words with your tounge.".format(playNom))
			timeOut(6)
			print("\"Anything more important than me shall come to a violent end in dispair!\"")
		else:
			print("You do not possess this power... yet.")
	elif tehGame == "move east":
		if DefunctCloneDED == True:
			print("You stumble across an empty chair, and seize it's existance.")
			timeOut(4)
			print("\"Power... is mine!\" You laugh maniacally.")
		else:
			if DefunctClone == False:
				print("You barge into your defunct clone, \"What the blazes man!\" {}'s clone shouts.".format(playNom))
				timeOut(5)
				print("\"Get back to work,\" You yell at {}, \"Or I will absorb you!\"".format(gender1))
				timeOut(6)
				print("\"Make me.\" {} threatens.".format(gender1))
				timeOut(3)
				Answer1 = input("Absorb him? ->")
				Answer1 = Answer1.lower()
				if Answer1 == "yes":
					print("You have absorbed your clone, you monster!")
					timeOut(5)
					print("You have gained the {}!".format(plazmaI))
					Swapp(plazmaI)
					print("Use 'Zap [object]' to electrocute anything to a crisp.")
					timeOut(3)
					print("Electricity forms on the tips of your fingers.")
					timeOut(4)
					print("\"I still don't know my good deeds, nor my purpose.\". {}-sama tilts {} head.".format(playNom, gender2))
					timeOut(5)
					print("\"I guess I still have to wing-it.\"")
					timeOut(3)
					print("Your purpose has changed from \"Pure\" to \"Morally Confused\"")
					Purpose = "Confused"
					DefunctCloneDED = True
				elif Answer1 == "no":
					print("\"Nevermind\" You tell your defunct clone.")
					timeOut(4)
					print("{} looks at you with wicked drabness, \"What?!\"".format(gender1))
					timeOut(4)
					print("\"You heard me fully, and I'm feeling benevolent.\" You tell {}.".format(gender1))
					timeOut(5)
					print("{}-sama pats {} defuct clone on the head.".format(playNom, gender2))
					timeOut(5)
					print("\"Hey, I need to tell you that I can be your party member\" Defunct Clone tells you.")
					timeOut(6)
					print("\"Huh?\" You scratch your head.")
					timeOut(3)
					print("Yeah, you can use (Summon [character]) to teleport me to your location to assist you in combat, puzzles, and practically almost anything!")
					timeOut(10)
					print("You've obtained \"Defunct Clone\" as your party member!")
					DefunctClone = True
					print("Your purpose has changed from \"Pure\" to \"Speedrunner\"")
					Purpose = "Speedrunner"
				else:
					print("You just walk away from the situation, wishing that this never happened.")
			else:
				print("You gloss over Defunct {}, and pat {} on the head once more.".format(playNom, gender1))
				timeOut(6)
				print("\"I'm not your pet!\" Your clone barks.")
				timeOut(3)
				print("\"You'd be surprised.\" You tell {} back as you materialize bacon and throw it at him.".format(gender1))
	elif tehGame == "move north":
		Summon += 1
		print("Summon value = {}".format(Summon))
		if Player1.DefunctClone == False:
			print("\"Hey!!\" You hear someone yelling from the east side of the room.")
			timeOut(5)
			print("{} turns {} head to the origin of the sound, and {} witnessed {} Defunct Clone sitting in a chair next to the computer screen.".format(playNom, gender2, gender3, gender2))
			timeOut(7)
			print("\"Are you seriously ignoring me?!\" Defunct {}-sama lashes.".format(playNom))
			timeOut(3)
			print("You roll your eyes, \"Maybe...\" You tell {} in a sarcastic voice.".format(gender1))
			timeOut(5)
			print("\"There is no 'maybe'... {}-sama!\" The Defuct Clone shouts and points at you.".format(playNom))
			timeOut(6)
			print("\"I wanna let you know, that I'm an important person in this game. I was told that I'm optional, but you know what, I'm sick of imagining what it's like in the outside world!\"")
			timeOut(10)
			print("\"You created the slums off...\"")
			timeOut(1)
			print("\"I didn't create crap!\" {} interrupts you, \"That defunct clone died long ago, burried by your own concieved dogma!\"".format(gender3))
			timeOut(7)
			print("\"{}... {} was the true maker of that town that lies beyond. You killed {}!\"".format(gender3, gender3, gender2))
			timeOut(6)
			print("\"No I didn't!\" You confess, \"It was my evil self; YOU were living under a rock for centuries!\"")
			timeOut(7)
			print("\"The clone's face is red with rage, \"How dare you mock my sagaciousness!!\"")
			timeOut(5)
			print("Lightning charges can be seen from {} fingertips, \"Let's see if your more bark than bite, Evil Self!!\"".format(gender2))
			print("{COMBAT INITIATED}")
			timeOut(1)
			print("{} zaps you by summoning lightning from {} fingertips.".format(gender3, gender2))
			timeOut(2)
			print("Your torso is charred!")
			tehGame = input("You can: (Punch) (Flee) ->")
			tehGame = tehGame.lower()
			if tehGame == "punch":
				print("You punch harder!!")
				timeOut(2)
				print("Defunct Clone: Massive damage to the cranium")
				timeOut(2)
				print("It's not enough!")
				timeOut(2)
				print("Your defunct clone commits an uppercut.")
				timeOut(2)
				print("You: Medium damage to the neck.")
				timeOut(1)
				print("You're flung up into the air.")
				timeOut(2)
				print("{CHANCE OF DEATH}")
				timeOut(5)
				print(".")
				timeOut(1)
				print("..")
				timeOut(1)
				print("...")
				Chance_of_Death = randint(1,2)
				if Chance_of_Death == 1:
					timeOut(1)
					print("You hit your head.")
					timeOut(2)
					print("You died to your neck snapping.")
					timeOut(2)
					print("(Died to Defunct Clone) hint: do not mess with a guy with lightning powers.")
					exit()
				elif Chance_of_Death == 2:
					print("You stick the landing!!")
					tehGame = input("You can: (Punch) or (Mercy) ->")
					tehGame = tehGame.lower()
					if tehGame == "punch":
						print("You deliver the final punch!")
						timeOut(2)
						print("Defunct Clone: Fatal Damage!!!")
						timeOut(2)
						print("\"Why do you hate me--so...\" Were your defunct clone's last words.")
						timeOut(3)
						print("You absorb your Defunct Clone's carcass.")
						timeOut(3)
						print("You gain the power of Electrocution 1 and Beta Knife!")
						Swapp(plazmaI)
						Swapp(testK)
						print("Your wounds automatically heal.")
						timeOut(3)
						print("During the corse of your recovery, you think to yourself, contemplating about your life as a clone of god.")
						timeOut(6)
						print("\"Is that all I am?\" {} thinks aloud, \"A clone to a selfish god?\"")
						timeOut(4)
						print("You spit on the floor, \"I know my TRUE purpose and my good deeds.\"")
						timeOut(4)
						print("\"I must kill all clones of my true, selfish self.\" You maniaclly grin, \"I must kill all who oppose me.\"")
						timeOut(6)
						DefunctCloneDED = True
						print("\"Your purpose has been changed from \"Pure\" to \"Sack Religious\".")
						Purpose = "AntiReligious"
					elif tehGame == "mercy":
						print("\"If you seize attack, I will stop my attack.\" You tell {}".format(gender2))
						timeOut(2)
						print("Your clone looks down at the floor and shakes his head, \"What are my benefits?\"")
						timeOut(4)
						print("\"Your life.\" You tell him.")
						timeOut(4)
						print("Silence occurs.")
						timeOut(5)
						print("\"I see...\" {} backs off, \"I'll stop, don't wanna mess with someone with commendable strength\"".format(gender1))
						timeOut(5)
						print("\"Or,\" You attempt to change his mind, \"you can join my strength. We'll find our purpose together.\"")
						timeOut(4)
						print("The defunct clone feebly smiles, \"I'll follow your lead any day.\"")
						timeOut(3)
						print("Defunct Clone joins your party!")
						DefunctClone = True
						timeOut(3)
						print("Your purpose has been changed from \"Pure\" to \"Absolute Awesome Person\"")
						Purpose = "BadAAP"
						timeOut(2)
						print("\"Here, have a Beta Knife.\" Your clone chucks the knife at you.")
						timeOut(2)
						Swapp(testK)
						print("\"Slash anything with it and your target explodes.\" Your clone explains, \"However, only use it wisely.\"")
						timeOut(6)
						print("\"Why?\" {} asks.".format(playNom))
						timeOut(3)
						print("\"It corrupts your soul if used.\"")
						timeOut(4)
						print("These words do not phase you, \"May my soul be damned if may be, my good deeds will never fail my way.\"")
			elif tehGame == "flee":
				print("\"I don't want to fight you!\" {} shouts to {} defunct clone as {} books it to the door, \"Let alone understand what your talking about!\"".format(playNom, gender2, gender3))
				timeOut(5)
				print("\"Running away from a fight will never serve you well outside the doors!\" Your defunct clone shouts.")
				timeOut(5)
				print("Your defunct clone blocks the door with his own body.")
				timeOut(4)
				print("The defunct clone surrounds {} body with electicity, and tackles you.".format(gender2))
				timeOut(5)
				print("You: Massive Damage to the nerve system! (fell to the floor due to damage)")
				tehGame = input("You can: (Break Window), (Mercy), (Punch)")
				tehGame = tehGame.lower()
				if tehGame == "break window":
					print("You can't move!")
					timeOut(3)
					print("\"Now, it's time to end this!\" Your clone shouts.")
					timeOut(3)
					print("Defunct Clone engulfs {} hand with electricity and charges at you.".format(gender2))
					timeOut(4)
					print("The Defunct Clone's Thunder Punch missed.")
					timeOut(3)
					print("The plazma scortches the wooden floor.")
					timeOut(3)
					print("You detected a knife strapped onto the clone's pants.")
					timeOut(4)
					print("With the upmost potent of your current streingth, you pull the knife out from the strap...")
					timeOut(4)
					print("Throw it at the window, and the window explodes.")
					timeOut(5)
					print("\"I will not die without you!\" You yell at the clone.")
					timeOut(4)
					print("The void consumes all life and light.")
					timeOut(7)
					print("(Died like an Absolute Awesome Person) hint: genoside is never the answer to anything in life")
					exit()
				elif tehGame == "mercy":
					print("\"I said, I don't want to fight!!!\"")
					timeOut(3)
					print("Your clone stares long into your soul.")
					timeOut(8)
					print("\"You're defunct for a reason, please don't kill me!\" You yell {}.".format(gender2))
					timeOut(4)
					print("The Defunct Clone's life has finally been enlightened, guilt overflows onto his essence.")
					timeOut(6)
					print("\"I-I'm sorry.\" Your clone drops his Beta Knife, \"Please forgive me.\"")
					tehGame = input("You can: (Forgive), (Forget), (Destroy*)")
					tehGame = tehGame.lower()
					if tehGame == "forgive":
						print("\"It's ok,\" You gather all of your streingth to get up, \"I can forgive you.\"")
						timeOut(5)
						print("Tears can be seen from your clone's face, \"{}...\"".format(playNom))
						timeOut(4)
						print("You walk over to him, \"Say no more, corrupted {}-sama.\"".format(playNom))
						timeOut(5)
						print("You embrace your clone, and clense him of his evil ways.")
						timeOut(5)
						print("Defunct Clone, is now Clensed Clone.")
						timeOut(4)
						print("\"Thank you, my kin.\" your clone apologizes, \"How did I fall under this path of life?\"")
						timeOut(5)
						print("\"Since you've built the catacombs of the town beyond.\" You respond.")
						timeOut(6)
						print("The embrace breaks. \"Then my kin, let's spread your good deeds to the catacombs!\" Clense Clone exclaimes.")
						timeOut(7)
						print("Clensed Clone joins your party.")
						ClensedClone = True
						timeOut(5)
						print("\"Well then,\" you walk to the door, \"Allow us to not waist anymore time.\"")
						timeOut(6)
						print("Your purpose has remained \"Pure\"")
						Purpose = "Pure"
					elif tehGame == "forget":
						print("\"I don't care.\" you wimper.")
						timeOut(3)
						print("\"You, are a defunct clone of mine. It's to be expected that you would revolt against your own maker.\"")
						timeOut(7)
						print("Your clone seizes {} speech; he looks at {} hands, still electrified, and {} stability crumbles.".format(gender2, gender2, gender2))
						timeOut(7)
						print("\"Why... have I deemed down the path of the fallen?\" The clone looks back at you, shivering with dread.")
						timeOut(7)
						print("\"It looks like my evil self has gotten to you.\" {} tells the defunct clone as {} rises and limps away.".format(playNom, gender1))
						timeOut(5)
						print("\"Erase me!\" The clone pleads, \"End my existance! I'm sorry...\"")
						timeOut(5)
						print("\"I'M SO SORR-\"")
						timeOut(0.5)
						print("Your Defunct Clone explodes.")
						timeOut(4)
						print("You turn around, and you see scortch marks from where the clone used to be.")
						timeOut(5)
						print("{}'s fear forces him to not move!".format(playNom))
						timeOut(6)
						print("\'I'm not broken out of combat yet.\' You ponder, \'Who else is there?\'")
						timeOut(8)
						print("A black cloud of spiritual energy appears before you.")
						timeOut(5)
						print("\"Hello, {}-sama, my old enemy.\" The black energy speaks.".format(playNom))
						timeOut(4)
						print("\"I should've known!\" A lightbulb appears in your head.")
						timeOut(4)
						print("\"Corruption!\"")
						timeOut(1)
						print("\"Evil Self!\"")
						timeOut(1)
						print("\"Windowed Void,\" The cloud reveals, \"Your worse nightmare!\"")
						timeOut(5)
						print("\"Instead of taking pride within yourself, this is the ripe time to kill me!\" You yell at Void.")
						timeOut(7)
						print("\"You are not a threat to me.\" Windowed Void pitties you, \"Without absorbing or allying with Defunct Clone...\"")
						timeOut(7)
						print("\"You only have your fists to fight with; you cannot harm me in this form.\"")
						timeOut(6)
						print("\"I'd much rather make you watch the destruction of this realm, and everything you created.\"")
						timeOut(6)
						print("Windowed Void's Cloud form dissapears.")
						timeOut(4)
						print("Your physical wounds heal, but you're scarred in the heart.")
						timeOut(5)
						Purpose = "Scarred"
						print("Your purpose has changed from \"Pure\" to \"Scarred\".")
						timeOut(6)
						print("Knowing that the threat is out there, you carefully open the door to the outdoors.")
				elif tehGame == "punch":
					print("You gather all of your streingth to rise up.")
					timeOut(5)
					print("\"Don't you just ever give up?\" Defunct Clone shouts")
					timeOut(4)
					print("\"Never!\" You pathetically wimper.")
					timeOut(3)
					print("\"You punch your defunct clone in the face!")
					timeOut(4)
					print("Defunct Clone: Petite Damage to the face.")
					timeOut(3)
					print("\"I actually pity your soul.\" Defunct Clone-sama talks down upon you.")
					timeOut(5)
					print("The clone pulls out {} Beta Knife and cuts you.".format(gender2))
					timeOut(4)
					print("You explode.")
					timeOut(2)
					print("You: FATAL DAMAGE!!!")
					timeOut(3)
					print("(Died to being stubborn) hint: Benevolence pays in many ways.")
					exit()
			else:
				print("You couldn't move because of a faulty command!")
				timeOut(4)
				print("\"If you won't fight, I will!\" The Defuct Clone dropkicks.")
				timeOut(5)
				print("You: Huge Damage to the Rib Cage! (Last Chance)")
				tehGame = input("You can: (Punch) (Flee) ->")
				tehGame = tehGame.lower()
				if tehGame == "punch":
					print("You punch harder!!")
					timeOut(2)
					print("Defunct Clone: Massive damage to the cranium")
					timeOut(2)
					print("It's not enough!")
					timeOut(2)
					print("Your defunct clone commits an uppercut.")
					timeOut(2)
					print("You: Medium damage to the neck.")
					timeOut(1)
					print("You're flung up into the air.")
					timeOut(2)
					print("{CHANCE OF DEATH}")
					timeOut(5)
					print(".")
					timeOut(1)
					print("..")
					timeOut(1)
					print("...")
					Chance_of_Death = randint(1,2)
					if Chance_of_Death == 1:
						timeOut(1)
						print("You hit your head.")
						timeOut(2)
						print("You died to your neck snapping.")
						timeOut(2)
						print("(Died to Defunct Clone) hint: do not mess with a guy with lightning powers.")
						exit()
					elif Chance_of_Death == 2:
						print("You stick the landing!!")
						tehGame = input("You can: (Punch) or (Mercy) ->")
						tehGame = tehGame.lower()
						if tehGame == "punch":
							print("You deliver the final punch!")
							timeOut(2)
							print("Defunct Clone: Fatal Damage!!!")
							timeOut(2)
							print("\"Why do you hate me--so...\" Were your defunct clone's last words.")
							timeOut(3)
							print("You absorb your Defunct Clone's carcass.")
							timeOut(3)
							print("You gain the power of Electrocution 1 and Beta Knife!")
							Swapp(plazmaI)
							Swapp(testK)
							print("Your wounds automatically heal.")
							timeOut(3)
							print("During the corse of your recovery, you think to yourself, contemplating about your life as a clone of god.")
							timeOut(6)
							print("\"Is that all I am?\" {} thinks aloud, \"A clone to a selfish god?\"")
							timeOut(4)
							print("You spit on the floor, \"I know my TRUE purpose and my good deeds.\"")
							timeOut(4)
							print("\"I must kill all clones of my true, selfish self.\" You maniaclly grin, \"I must kill all who oppose me.\"")
							timeOut(6)
							DefunctCloneDED = True
							print("\"Your purpose has been changed from \"Pure\" to \"Sack Religious\".")
							Purpose = "AntiReligious"
						elif tehGame == "mercy":
							print("\"If you seize attack, I will stop my attack.\" You tell {}".format(gender2))
							timeOut(2)
							print("Your clone looks down at the floor and shakes his head, \"What are my benefits?\"")
							timeOut(4)
							print("\"Your life.\" You tell him.")
							timeOut(4)
							print("Silence occurs.")
							timeOut(5)
							print("\"I see...\" {} backs off, \"I'll stop, don't wanna mess with someone with commendable strength\"".format(gender1))
							timeOut(5)
							print("\"Or,\" You attempt to change his mind, \"you can join my strength. We'll find our purpose together.\"")
							timeOut(4)
							print("The defunct clone feebly smiles, \"I'll follow your lead any day.\"")
							timeOut(3)
							print("Defunct Clone joins your party!")
							DefunctClone = True
							timeOut(3)
							print("Your purpose has been changed from \"Pure\" to \"Absolute Awesome Person\"")
							Purpose = "BadAAP"
							timeOut(2)
							print("\"Here, have a Beta Knife.\" Your clone chucks the knife at you.")
							timeOut(2)
							Swapp(testK)
							print("\"Slash anything with it and your target explodes.\" Your clone explains, \"However, only use it wisely.\"")
							timeOut(6)
							print("\"Why?\" {} asks.".format(playNom))
							timeOut(3)
							print("\"It corrupts your soul if used.\"")
							timeOut(4)
							print("These words do not phase you, \"May my soul be damned if may be, my good deeds will never fail my way.\"")
				elif tehGame == "flee":
					print("\"I don't want to fight you!\" {} shouts to {} defunct clone as {} books it to the door, \"Let alone understand what your talking about!\"".format(playNom, gender2, gender3))
					timeOut(5)
					print("\"Running away from a fight will never serve you well outside the doors!\" Your defunct clone shouts.")
					timeOut(5)
					print("Your defunct clone blocks the door with his own body.")
					timeOut(4)
					print("The defunct clone surrounds {} body with electicity, and tackles you.".format(gender2))
					timeOut(5)
					print("You: Massive Damage to the nerve system! (fell to the floor due to damage)")
					tehGame = input("You can: (Break Window), (Mercy), (Punch)")
					tehGame = tehGame.lower()
					if tehGame == "break window":
						print("You can't move!")
						timeOut(3)
						print("\"Now, it's time to end this!\" Your clone shouts.")
						timeOut(3)
						print("Defunct Clone engulfs {} hand with electricity and charges at you.".format(gender2))
						timeOut(4)
						print("The Defunct Clone's Thunder Punch missed.")
						timeOut(3)
						print("The plazma scortches the wooden floor.")
						timeOut(3)
						print("You detected a knife strapped onto the clone's pants.")
						timeOut(4)
						print("With the upmost potent of your current streingth, you pull the knife out from the strap...")
						timeOut(4)
						print("Throw it at the window, and the window explodes.")
						timeOut(5)
						print("\"I will not die without you!\" You yell at the clone.")
						timeOut(4)
						print("The void consumes all life and light.")
						timeOut(7)
						print("(Died like an Absolute Awesome Person) hint: genoside is never the answer to anything in life")
						exit()
					elif tehGame == "mercy":
						print("\"I said, I don't want to fight!!!\"")
						timeOut(3)
						print("Your clone stares long into your soul.")
						timeOut(8)
						print("\"You're defunct for a reason, please don't kill me!\" You yell {}.".format(gender2))
						timeOut(4)
						print("The Defunct Clone's life has finally been enlightened, guilt overflows onto his essence.")
						timeOut(6)
						print("\"I-I'm sorry.\" Your clone drops his Beta Knife, \"Please forgive me.\"")
						tehGame = input("You can: (Forgive), (Forget), (Destroy*)")
						tehGame = tehGame.lower()
						if tehGame == "forgive":
							print("\"It's ok,\" You gather all of your streingth to get up, \"I can forgive you.\"")
							timeOut(5)
							print("Tears can be seen from your clone's face, \"{}...\"".format(playNom))
							timeOut(4)
							print("You walk over to him, \"Say no more, corrupted {}-sama.\"".format(playNom))
							timeOut(5)
							print("You embrace your clone, and clense him of his evil ways.")
							timeOut(5)
							print("Defunct Clone, is now Clensed Clone.")
							timeOut(4)
							print("\"Thank you, my kin.\" your clone apologizes, \"How did I fall under this path of life?\"")
							timeOut(5)
							print("\"Since you've built the catacombs of the town beyond.\" You respond.")
							timeOut(6)
							print("The embrace breaks. \"Then my kin, let's spread your good deeds to the catacombs!\" Clense Clone exclaimes.")
							timeOut(7)
							print("Clensed Clone joins your party.")
							ClensedClone = True
							timeOut(5)
							print("\"Well then,\" you walk to the door, \"Allow us to not waist anymore time.\"")
							timeOut(6)
							print("Your purpose has remained \"Pure\"")
							Purpose = "Pure"
						elif tehGame == "forget":
							print("\"I don't care.\" you wimper.")
							timeOut(3)
							print("\"You, are a defunct clone of mine. It's to be expected that you would revolt against your own maker.\"")
							timeOut(7)
							print("Your clone seizes {} speech; he looks at {} hands, still electrified, and {} stability crumbles.".format(gender2, gender2, gender2))
							timeOut(7)
							print("\"Why... have I deemed down the path of the fallen?\" The clone looks back at you, shivering with dread.")
							timeOut(7)
							print("\"It looks like my evil self has gotten to you.\" {} tells the defunct clone as {} rises and limps away.".format(playNom, gender1))
							timeOut(5)
							print("\"Erase me!\" The clone pleads, \"End my existance! I'm sorry...\"")
							timeOut(5)
							print("\"I'M SO SORR-\"")
							timeOut(0.5)
							print("Your Defunct Clone explodes.")
							timeOut(4)
							print("You turn around, and you see scortch marks from where the clone used to be.")
							timeOut(5)
							print("{}'s fear forces him to not move!".format(playNom))
							timeOut(6)
							print("\'I'm not broken out of combat yet.\' You ponder, \'Who else is there?\'")
							timeOut(8)
							print("A black cloud of spiritual energy appears before you.")
							timeOut(5)
							print("\"Hello, {}-sama, my old enemy.\" The black energy speaks.".format(playNom))
							timeOut(4)
							print("\"I should've known!\" A lightbulb appears in your head.")
							timeOut(4)
							print("\"Corruption!\"")
							timeOut(1)
							print("\"Evil Self!\"")
							timeOut(1)
							print("\"Windowed Void,\" The cloud reveals, \"Your worse nightmare!\"")
							timeOut(5)
							print("\"Instead of taking pride within yourself, this is the ripe time to kill me!\" You yell at Void.")
							timeOut(7)
							print("\"You are not a threat to me.\" Windowed Void pitties you, \"Without absorbing or allying with Defunct Clone...\"")
							timeOut(7)
							print("\"You only have your fists to fight with; you cannot harm me in this form.\"")
							timeOut(6)
							print("\"I'd much rather make you watch the destruction of this realm, and everything you created.\"")
							timeOut(6)
							print("Windowed Void's Cloud form dissapears.")
							timeOut(4)
							print("Your physical wounds heal, but you're scarred in the heart.")
							timeOut(5)
							Purpose = "Scarred"
							print("Your purpose has changed from \"Pure\" to \"Scarred\".")
							timeOut(6)
							print("Knowing that the threat is out there, you carefully open the door to the outdoors.")
					elif tehGame == "punch":
						print("You gather all of your streingth to rise up.")
						timeOut(5)
						print("\"Don't you just ever give up?\" Defunct Clone shouts")
						timeOut(4)
						print("\"Never!\" You pathetically wimper.")
						timeOut(3)
						print("\"You punch your defunct clone in the face!")
						timeOut(4)
						print("Defunct Clone: Petite Damage to the face.")
						timeOut(3)
						print("\"I actually pity your soul.\" Defunct Clone-sama talks down upon you.")
						timeOut(5)
						print("The clone pulls out {} Beta Knife and cuts you.".format(gender2))
						timeOut(4)
						print("You explode.")
						timeOut(2)
						print("You: FATAL DAMAGE!!!")
						timeOut(3)
						print("(Died to being stubborn) hint: Benevolence pays in many ways.")
						exit()
				else:
					print("\"That's it!\" Defunct Clone yells, \"I'm tired of this!\"")
					timeOut(6)
					print("Defunct Clone pulls out his Beta Knife and slashes at you.")
					timeOut(4)
					print("You explode.")
					timeOut(1)
					print("(Death by idioticy) hint: DO SOMETHING!")
		if TownNom == False:
			if Purpose == "Pure":
				print("You open the door and, finally, see what's beyond the tutorial.")
				timeOut(4)
				print("City (Central Area): This is the city that you’ve built around your house.")
				timeOut(4)
				print("{} thought that it was a grand idea to make the city without a mayor and a name.".format(playNom))
				timeOut(5)
				print("Knowing this, {} became the mayor of this town… and was too lazy to create a name for it.".format(gender3))
				timeOut(7)
				Town = input("What will you name your town? ->")
				print("You shout to the world, \"I hereby call this nameless town {}!\"".format(Town))
				timeOut(4)
				print("Random passersbys bow down to your lordship.")
				timeOut(4)
				print("\"All hail the town, {}!\" They shout to the heavens.".format(Town))
				timeOut(5)
				print("{} also made himself the messiah of {}’s religion.".format(playNom, Town))
				timeOut(5)
				print("\"Let's all praise {}, the lord!\" You exclaim to the heavens.".format(gender1))
				timeOut(6)
				print("\'I need to go to the slums,\' You think, \'That way, I can convert people to their own good ways.\'")
				tehArea = 2
				TownNom = True
			if Purpose == "Scarred":
				print("To try to move forward with your temporary life, you open the door and create a portal to a parallel universe.")
				timeOut(7)
				print("\"I have no weapons, power-ups, or allies to call upon...\" {} relizes reality.".format(playNom))
				timeOut(5)
				print("\"I feel naked...\"")
				timeOut(3)
				print("You move through the portal and close it immediatly behind you; You don't want Windowed Void to pass through in your vulnerable state.")
				timeOut(10)
				print("You spawn into the town; random passerbys can be seen scattered throughout the town.")
				timeOut(7)
				print("\"G'morning milord!\" A random passerby bows then moves on with their life.")
				timeOut(7)
				print("\'That's correct!\' You begin to monolouge, \'I am the massiah of this town... Something I cherish.\'")
				timeOut(7)
				print("Windowed Void's threat circles into your mind.")
				timeOut(4)
				Town = input("You try to erase those memories by naming your nameless town. ->")
				print("On a whim, you snap your fingers and the name of this town is {}, henceforth.".format(Town))
				timeOut(5)
				print("You continue on with your day; trying to move on as you conseal yourself with a cloak.")
				tehArea = 2
				TownNom = True
			if Purpose == "Corrupted":
				print("{} move through the door, with all intent to destroy anything in your path.".format(playNom))
				timeOut(5)
				print("You see scattered civilians throughout the city that is bestowed upon you.")
				timeOut(5)
				print("\"Fresh... Experiance Points!\" {} slobbers.".format(playNom))
				timeOut(4)
				Town = input ("Name your to-be slaughter grounds->")
				print("Henceforth, {} will be your breeding grounds of 'good deeds'!".format(Town))
				tehArea = 2
				TownNom = True
			if Purpose == "BadAAP":
				print("You kick the door down; with Defunct Clone in tow, you make way for the city.")
				timeOut(7)
				print("\"Bro!\" Defuct Clone shouts, \"That's not necisarry!\"")
				timeOut(5)
				print("\"This is a war.\" You respond, \"We must battle with life.\"")
				timeOut(5)
				Town = input("\"Aren't you at least going to name this no-named City?\" ->")
				print("\"{},\" {} shouts aloud, \"This is the land of {}\"".format(Town, playNom, Town))
				timeOut(4)
				print("\"{}...\" Defunct Clone thinks, \"That name's so rad!\"")
				timeOut(5)
				print("\"Then come, Defunct-sama! Let us make war with the world!\"")
				timeOut(6)
				print("Defunct Clone walks back inside the starting structure, \"Summon if you need me!\"")
				timeOut(7)
				print("{} moves on with {} ego with gudge for your clone behind your back.".format(playNom, gender3))
				tehArea = 2
				TownNom = True
			if Purpose == "Antireligious":
				print("Hatred and pride resides within your soul.")
				timeOut(4)
				print("You slash down the door with your Beta Knife; it explodes.")
				timeOut(6)
				print("\"Now, it's time do destroy ALL of the churches; I am the massiah no more, I am the savior of humanity.\" You grovel.")
				timeOut(10)
				Town = ("Spite the name of the Gods by renaming this town. ->")
				print("\"New {} shall rise from it's former ashes and begin anew with my own influence.\"")
				timeOut(6)
				print("\"I'm going to assume that my... political agenda is out of the question.")
				tehArea = 2
				TownNom = True
			if Purpose == "Confused":
				print("You open the door and, finally, see what's beyond the tutorial.")
				timeOut(4)
				print("City (Central Area): This is the city that you’ve built around your house.")
				timeOut(4)
				print("{} thought that it was a grand idea to make the city without a mayor and a name.".format(playNom))
				timeOut(5)
				print("Knowing this, {} became the mayor of this town… and was too lazy to create a name for it.".format(gender3))
				timeOut(7)
				Town = input("What will you name your town? ->")
				print("You meakly shout to the world, \"I hereby call this nameless town {}!\"".format(Town))
				timeOut(4)
				print("Random passersbys ignore your existance.")
				timeOut(4)
				print("\"Humf,\" You strut, \"I don't need followers anyways.\"")
				timeOut(5)
				print("{} also made himself the messiah of {}’s religion, but it's not a popular one.".format(playNom, Town))
				timeOut(5)
				print("\'I need to go to the church...\' You think, \'My followers have been dwindling from my last visit.")
				timeOut(7)
				print("\'Let us all pray that no evil has bestowed upon this realm.\'")
				tehArea = 2
				TownNom = True
			if Purpose == "Speedrunner":
				print("You open the doors, and a nameless Town appears.")
				timeOut(1)
				Town = input("NAME THE TOWN!!! ->")
				timeOut(1)
				print("\"All hail the lord!\" The passerbys yell.")
				timeOut(1)
				print("\"Amen!\" {} yells to the crowd. {}'s the massiah.".format(playNom, gender1))
				timeOut(1)
				print("\"Praise the town, {}!\" Your nonexistant followers yell to the world.".format(Town))
				tehArea = 2
				TownNom = True
			if Purpose == "Thug":
				print("You punch the doors down with pride stimulating your sences.")
				timeOut(5)
				print("You grin as you see passerbys in this great big city.")
				timeOut(5)
				print("The civilians scurry away from you with fear.")
				timeOut(3)
				print("\"I see that this town has no mayor.\" You talk aloud, \"I should head to the mayor's office and take over this city.\"")
				timeOut(9)
				print("You stop to think... \"Where in the world is this office!\"")
				timeOut(4)
				print("\'No matter, I'll storm through this blasted place anyways...\'")
				tehArea = 2
		else:
			print("You make your way to the Town of {}".format(Town))
			tehArea = 2
	elif tehGame == "summon defunct clone":
		if DefunctClone == True:
			print("You've tried to summon your defunct clone!")
			timeOut(4)
			print(".")
			timeOut(1)
			print("..")
			timeOut(1)
			print("...")
			if Summon > 0:
				timeOut(1)
				print("A portal appeared and {}'s defunct clone came through!".format(playNom))
				timeOut(4)
				print("\"What do you want?!\" {} shouts.".format(gender3))
				tehGame = input("(Attack [noun]), (Smite [noun]), (Call Off), (Talk) ->")
				tehGame = tehGame.lower()
				if tehGame == "attack bed":
					print("Your clone zaps the bed with plazma.")
					timeOut(3)
					print("The bed is now in ashes.")
					timeOut(3)
					print("Your clone walks back to the computer.")
					Summon -= 1
				elif tehGame == "smite bed":
					print("Your clone touches the bed and turned it into a wooden shield!")
					Swapp(shield)
					BedFalse = True
					print("Your clone walks back to the computer.")
					Summon -= 1
				elif tehGame == "smite window":
					print("Your clone touches the window and it explodes.")
					timeOut(4)
					print("(Death by Defunct Clone) hint: do not fool with windows.")
					exit()
				elif tehGame == "smite computer":
					print("Your clone gives you a fuse bomb.")
					Swapp(bamb)
					timeOut(3)
					print("\"I'm not smiting my computer.\" {}'s defunct clone tells {}.".format(playNom, gender1))
					print("Your clone walks back to the computer.")
					Summon -= 1
				elif tehGame == "attack window":
					print("Your clone breaks the window and everything is engulfed by the void.")
					timeOut(5)
					print("(Death by Idiotic Command) hint: do not fool with windows.")
					exit()
				elif tehGame == "attack computer":
					print("Defunct Clone attacks you!")
					timeOut(4)
					print("\"I will never attack my computer, you idiot!\"")
					timeOut(5)
					MoralChoice1 = input("Punch Defunct Clone?! [yes] [no] ->")
					MoralChoice1 = tehGame.lower()
					if MoralChoice1 == "no":
						print("You don't want to commit murder... just yet.")
					elif MoralChoice1 == "yes":
						print("You punch you clone in the face.")
						timeOut(3)
						print("{COMBAT INITIATED}")
						timeOut(1)
						print("{} zaps you by summoning lightning from {} fingertips.".format(gender3, gender2))
						timeOut(2)
						print("Your torso is charred!")
						tehGame = input("You can: (Punch) (Flee) ->")
						if tehGame == "punch":
							print("You punch harder!!")
							timeOut(2)
							print("Defunct Clone: Massive damage to the cranium")
							timeOut(2)
							print("It's not enough!")
							timeOut(2)
							print("Your defunct clone commits an uppercut.")
							timeOut(2)
							print("You: Medium damage to the neck.")
							timeOut(1)
							print("You're flung up into the air.")
							timeOut(2)
							print("{CHANCE OF DEATH}")
							timeOut(5)
							print(".")
							timeOut(1)
							print("..")
							timeOut(1)
							print("...")
							Chance_of_Death = randint(1,2)
							if Chance_of_Death == 1:
								print("You hit your head.")
								timeOut(2)
								print("You died to your neck snapping.")
								timeOut(2)
								print("(Died to Defunct Clone) hint: do not mess with a guy with lightning powers.")
								exit()
							elif Chance_of_Death == 2:
								print("You stick the landing!!")
							tehGame = input("You can: (Punch) or (Mercy) ->")
							if tehGame == "punch":
								print("You deliver the final punch!")
								timeOut(2)
								print("Defunct Clone: Fatal Damage!!!")
								timeOut(2)
								print("\"Why do you hate me--so...\" Were your defunct clone's last words.")
								timeOut(3)
								print("You absorb your Defunct Clone's carcass.")
								timeOut(3)
								print("You gain the power of Electrocution 1 and Beta Knife!")
								Swapp(plazmaI)
								Swapp(testK)
								print("Your wounds automatically heal.")
								timeOut(3)
								print("Your thoughts twist and churn.")
								timeOut(3)
								print("You feel an intence migrain.")
								timeOut(3)
								print("\"I just committed murder... I killed a. living. thing.\" Thoughts continue to pop up in your soul.")
								timeOut(9)
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								print("\"Oh my god.\"")
								timeOut(0.5)
								print("\"I committed a sin!!\"")
								timeOut(0.5)
								print("\"Can a god commit a sin?!")
								timeOut(0.5)
								timeOut("\"It feels good to kill...\"")
								timeOut(0.75)
								print("\"Am I even a god?\"")
								timeOut(0.5)
								print("\"I killed my clone!\"")
								timeOut(0.75)
								print("\"Murder feels good.\"")
								timeOut(0.5)
								print("\"Did I kill myself?")
								timeOut(0.5)
								print("\"If I'm a mortal, then why am I god.\"")
								timeOut(0.5)
								print("\"KILL ME!\"")
								timeOut(0.5)
								print("\"I killed a god...\"")
								timeOut(4)
								print("\"And...\"")
								timeOut(2)
								print("\"It.\"")
								timeOut(1)
								print("\"Felt.\"")
								timeOut(1)
								print("\"Good...\"")
								timeOut(3)
								print("\"Good.\"")
								timeOut(3)
								print("\"Gooood Deeeds...")
								timeOut(4)
								print(":-)")
								timeOut(7)
								print("Your purpose has changed from \"Pure\" to \"Corrupted Soul\"")
								Purpose = "Corrupted"
								DefunctCloneDED = True
							elif tehGame == "mercy":
								print("\"If you seize attack, I will stop my attack.\" You tell {}".format(gender2))
								timeOut(2)
								print("Your clone looks down at the floor and shakes his head, \"What are my benefits?\"")
								timeOut(4)
								print("\"Unlimited 'pizza'.\" You tell him.")
								timeOut(4)
								print("\"So, I get a slice of that religous pie of yours?\" {} reassures.".format(gender1))
								timeOut(5)
								print("\"Of coarse!!\"")
								timeOut(4)
								print("The defunct clone smiles, \"Then count me in!\"")
								timeOut(3)
								print("Defunct Clone joins your party!")
								DefunctClone = True
								timeOut(2)
								print("\"Here, have a Beta Knife.\" Your clone chucks the knife at you.")
								timeOut(2)
								Swapp(testK)
								timeOut(1)
								print("\"I now know my purpose, I must spread my good deeds.")
								timeOut(2)
								print("Your purpose has changed from \"Pure\" to \"Thug\".")
								Purpose = "Thug"
						elif tehGame == "flee":
							print("\"It's just a prank bro.\" You tell your defunct clone.")
							timeOut(4)
							print("Your defunct clone shakes {} head.".format(gender2))
							timeOut(3)
							print("\"I shead no mercy on a defunct clone of mine.\" {} tells you.".format(gender1))
							timeOut(7)
							print("The now true clone of {} electrocutes you.".format(playNom))
							timeOut(3)
							print("You: Fatal Damage!!!")
							timeOut(4)
							print("(Death by being owned) hint: do not mess with a clone of god.")
							exit()
						else:
							print("Shut up, I'm lazy!")
				elif tehGame == "call off":
					print("\"What a waste...\" Your clone mutters as he walks back to his computer.")
				elif tehGame == "attack defunct clone" or tehGame == "attack clone":
					print("\"Do ya think I'm stupid?!\" {} yells, \"Yer just wasting your time...\"")
					timeOut(4)
					print("Your clone walks back to the computer.")
				else:
					print("\"I do not understand such incipid language.\" {}'s clone questions your existance.".format(playNom))
			else:
				print("You do not have enough Summon Points, enter another area to replenish them.")
		else:
			print("This summon is not unlocked.")
	else:
		globalCommand(tehGame, "Please, don't use such foul language.")



while tehArea == 2:
	print("Not yet implemented.")
	while Purpose == Pure:
		tehGame = input("	>")
		tehGame = tehGame.lower()
		if tehGame == "look south":
			print("Your structure still exists; just like any spawn area.")
		elif tehGame == "move south":
			print("You think you've missed something, so you try to go back home.")
			tehArea = 1
		elif tehGame == "look west":
			print("The dank catacombs lie beyond this point.")
			timeOut(4)
			print("Clensed Clone teleports to your location.")
			timeOut(4)
			print("\"Are you ready, Main {}-sama?\" {} asks you.".format(playNom, gender3))
			timeOut(3)
			print("You awkwardly stare west, not bothering to respond.")
			timeOut(5)
			print("The clone winks, \"You know where to find me.\"")
			timeOut(4)
			print("{} teleports away.".format(gender3))
		elif tehGame == "read catacombs" or tehGame == "read dank catacombs":
			print("You feel an immense evil energy radiating from the dankness.")
			timeOut(5)
			print("\'It's a cult.\' {} thinks, \'There is no other explanation for this phenomenon.\'".format(playNom))
		elif tehGame == "read mcronalds":
			print("This fast food chain is synonymous for its fake hamburger meat and chemical-rich fenchfries.")
			timeOut(9)
			print("Or, it's well known for its low prices.")
			timeOut(4)
			print("Ever since Cow-fill-a came into existance; McRonalds started cooking it's hamburgers with real, freezer-quality meat patties.")
		elif tehGame == "read jonnie jim's" or tehGame == "read jonnie jims":
			print("This building serves the freshest sandwiches on the block; they serve it infront of you.")
			timeOut(7)
			print("Soubway once existed here, but after a lawsuit over a \"Foot-long Fraud\" claim, Jonnie Jim's reign its domination.")
			timeOut(9)
			print("Dimitry Dean runs the place, he's a good man.")
		elif tehGame == "read dairy king":
			print("Dairy King's been here since the creation of this world.")
			timeOut(5)
			print("You've been funding the place benevolently, because it contains your favorite food; Royal Blizzards.")
		elif tehGame == "read cow-fill-a" or tehGame == "read cow fill a" or tehGame == "read cowfilla":
			print("Surprisingly enough, this fast-food chain only sells beef products and salad.")
			timeOut(6)
			print("Cow-fill-a also gave McRonalds a run for its money during the \"Beef off\" where a lawsuit was set against McRonald's quality meat.")
			timeOut(9)
			print("Dispite being recognized as a \'Christian assosiated\' restaurant, Cow-fill-a almost forced McRonalds into bankruptcy through the food court.")
		elif tehGame == "move east":
			print("You feel a little hungry, so you move to the Food District.")
			timeOut(5)
			print("\'Might as well grab something for Clensed Clone...\' {} thinks.".format(playNom))
			timeOut(4)
			tehArea = 3 
		elif tehGame == "look east":
			print("Fast food restaurants lie in this quadrant of the city.")
			timeOut(5)
			print("They are: McRonalds, Jonnie Jim's, Dairy King, and Cow-fill-a.")
		elif tehGame == "look north":
			print("A festival could be heard down the street.")
			timeOut(4)
			print("\'I should leave the happy folks alone; they are none of my concern at the momement\' {} thinks.".format(playNom))
		else:
			globalCommand(tehGame, "Random passerbys of {} witness your gibberish and walk the other way.".format(Town))
	while Purpose == Scarred:
		tehGame = input("	>")
		tehGame = tehGame.lower()
		if tehGame == "look south":
			print("The portal has closed behind you; it no longer exists.")
			timeOut(5)
			print("{} does see an apartment complex behind {}, but this is no longer {}.".format(playNom, gender1, gender2))
			timeOut(5)
			print("\'I mustn't look back!\' {} thinks, \'Windowed Void can find me at any moment!\'")
		elif tehGame == "look east":
			print("Fast-food restaurants lie in this quadrant of the city,")
			timeOut(4)
			print("They are McRonalds and Soubway.")
		elif tehGame == "read mcronalds":
			print("This fast food chain is synonymous for its fake hamburger meat and chemical-rich fenchfries.")
			timeOut(9)
			print("Or, it's well known for its low prices.")
			timeOut(4)
			print("To compete with Soubway, McRonalds constructed Preminum Snack Wraps.")
		elif tehGame == "read soubway":
			print("This fast-food restaurant serves foot-long sandwiches and soups.")
			timeOut(6)
			print("There are rumors that these \'foot-long\' sandwiches are actually eleven inches; the food court always disclose these claims as rumours though.")
		elif tehGame == "look west":
			print("Clean allyways can be obviously seen here.")
			timeOut(4)
			print("This is none of your consern.")
		elif tehGame == "look north":
			print("A festival can be spotted infront of you.")
			timeOut(4)
			print("A positive emotion kindles in {}'s heart.".format(playNom))
			timeOut(4)
			print("\'I need a little break from all of this tension; a little sidetracking shouldn't hurt.\'")
		else:
			globalCommand(tehGame, "Random passerbys of {} witness your gibberish and walk the other way.".format(Town))
else:
	pass
while tehArea == 3:
	while Purpose == Pure:
		print("You've found your way to a bustling mall filled to the brim with food items.")
		timeOut(4)
		print("McRonalds, Dairy King, Jonnie Jim's, and Cow-fill-a were the only fast-food chains that take your intrests.")
		timeOut(6)
		print("\'I'm too busy to eat at a legitimate restaurant right now.\' You think.")
		tehGame == input("(visit [place]) ->")
		#if :
		#	pass


	#print ("Sample Text!!!")
	#print ("(Unfinished Demo){} died by an unfinished game.".format(playNom))
	#sys.exit()
	
#while True:
	# inteleImput = input("This is a test. Imput the code. ->")
	# if inteleImput == "move North":
	# 	moveNorth();
	# elif inteleImput == "move South":
	# 	moveSouth();
	# elif inteleImput == "move West":
	# 	moveWest();
	# elif inteleImput == "move East":
	# 	moveEast();
	# else: 
	# 	print ("I'm too stupid to use that incepid language.")