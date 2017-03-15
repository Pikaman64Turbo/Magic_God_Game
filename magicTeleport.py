import time
import sys
import pickle

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
gender1 = "notin"
gender2 = "notin"
plazmaI = "Electrocution I"
testK = "Beta Knife"
playNom = "User"
woldNom = "Existance"
moralChoice1 = "Yes"
tehArea = 0

#This is used for Inventory.
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

def sayHello():
	print("hello")

def test0():
	testCheck1 = moralChoice1 = input("Absorb him? (Yes or No) ->")
	if moralChoice1 == "Yes":
		print("You have absorbed your clone, you monster!")
		timeOut(5)
		print("You have gained the {}! (not fully implemented)".format(plazmaI))
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
def moveNorth():
	global x
	global y
	newX = (x + 1)
	if newX < 0:
		print ("If I continue, I will be sucked into the void!")
		timeOut(1)
	else:
		x = newX
	print ("Location = {}, {}".format(x, y))
def moveSouth():
	global x
	global y
	newX = (x - 1)
	if newX < 0:
		print ("If I continue, I will be sucked into the void!")
		timeOut(1)
	else:
		x = newX
	print ("Location = {}, {}".format(x, y))
def moveEast():
	global x
	global y
	newY = (y + 1)
	if newY < 0:
		print ("If I continue, I will be sucked into the void!")
		timeOut(1)
	else:
		y = newY
	print ("Location = {}, {}".format(x, y))
def moveWest():
	global x
	global y
	newY = (y - 1)
	if newY < 0:
		print ("If I continue, I will be sucked into the void!")
		timeOut(1)
	else:
		y = newY
	print ("Location = {}, {}".format(x, y))
def timeOut(t):
	#time.sleep(t)
	pass

def swapGender():
	global gender
	gender = input("Are you a boy are a girl? ->")
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
		gender1 = "Dem thang."
		gender2 = "ROFLS"
		gender3 = "???"
		timeOut(3)
	else:
		print("That is not a gender, you need to see your local physician.")
		gender1 = "it"
		gender2 = "its"
		gender3 = "it"


def globalCommand(tehGame, badcommandstring):
	tehGame = tehGame.lower()
	if tehGame == "swap gender":
		swapGender()

	elif tehGame == "save game":
		pass

	elif tehGame  == "pouch":
		print(array_godPouch)

	else:
		print(badcommandstring)

class Save1(object):
	name = "default name"

    def __init__(self, woldNom, playNom, gender, gender1, gender2, gender3, Town):
        self.woldNom = woldNom
        self.playNom = playNom

with open('company_data.pkl', 'wb') as :

    company2 = pickle.load(input)
    print(company2.name) # -> spam
    print(company2.value)  # -> 42



print ("Hello, human player!")
timeOut (2)
#sayHello()
#timeOut(2)
#Swapp(testK)
#timeOut (2)
#test0()
#timeOut(2)
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
	gender1 = "Dem thang."
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
print ("Use the \"Pouch\" command to view your inventory.")
tehArea = 1
while tehArea == 1:
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
		print ("You are in your bedroom, try (examine Area) to see your immediate surroundings. Use (look South) to continue playing the game!")
	elif tehGame == "look south":
		print ("There's a window that peers out into darkness. You assume that it's a void.")
		timeOut(6)
		print ("There is a letter above the window.")
		timeOut(4)
		print ("'You can examine any noun [people, things, buildings, places] with the (read) command, even questionable items like #windows# and #people#.'")
		print ("Try (examine Area) to see your immediate surroundings.")
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
	elif tehGame == "read clone" or tehGame == "read defunct clone":
		print("Defunct {}-sama's a gamer, and it's {} entire purpose.".format(playNom))
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
		sys.exit()
	elif tehGame == "soviet russia":
		print("In Soviet Russia, Putin plays you.")
		timeOut(4)
		print("Easter Egg 'Lincoln' Found!")
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
	elif tehGame == "sleep bed":
		print("You plump down on the hard wooden surface.")
		timeOut(5)
		print("\"Wait a minute...\" You question.")
		timeOut(3)
		print("\"Wait a minute.....\"")
		timeOut(5)
		print("\"The floor is more comfortable than this!!\"")
		timeOut(6)
		print("{}'s defunct clone faceplams, \"That's why I created this chair! You were too busy creating the world that you skiped the conformaties!\"")
		timeOut(10)
		print("\"I'm not that lazy!\" You yell back at {}.".format(gender1))
		timeOut(3)
		print("\"You'd be surprised\" {} mouthsback then returns to playing Epic Teleporter Adventure.")
		timeOut(5)
		print("Easter Egg 'Patrick' found!")
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
	elif tehGame == "move east":
		if moralChoice1 == "Yes":
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
				print("You have gained the {}! (not yet implemented)".format(plazmaI))
				Swapp(plazmaI)
				moralChoice1 = "False1"
			elif Answer1 == "no":
				print("\"Nevermind\" You tell your defunct clone.")
				timeOut(4)
				print("{} looks at you with wicked drabness, \"What?!\"".format(gender1))
				timeOut(4)
				print("\"You heard me fully, and I'm feeling benevolent.\" You tell {}.".format(gender1))
				timeOut(5)
				print("{}-sama pats {} defuct clone on the head.".format(playNom, gender2))
				moralChoice1 = "False2"
			else:
				print("You just walk away from the situation, wishing that this never happened.")
		elif moralChoice1 == "False1":
			print("You stumble across an empty chair, and seize it's existance.")
			timeOut(4)
			print("\"Power... is mine!\" You laugh maniacally.")
		elif moralChoice1 == "False2":
			print("You gloss over Defunct {}, and pat {} on the head once more.".format(playNom, gender1))
			timeOut(6)
			print("\"I'm not your pet!\" Your clone barks.")
			timeOut(3)
			print("\"You'd be surprised.\" You tell {} back as you materialize bacon and throw it at him.".format(gender1))
	elif tehGame == "move north":
		print("You open the door and, finally, see what's beyond the tutorial.")
		timeOut(3)
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
		tehArea = 2
	else:
		globalCommand(tehGame, "Please, don't use such foul language.")

while tehArea == 2:
	tehGame = input("	>")
	tehGame = tehGame.lower()
	if tehGame == "look west":
		print("Dank alleyways lie in this direction.")
		print(4)
		print("\"I shouldn’t go here…\" {} thinks. \"This is the roughest part of {}.\"".format(playNom, Town))
	elif tehGame == "look east":
		print("Restaurants and fast food chains rest over here.")
		timeOut(4)
		print("{}'s stomache growls with ferocity.")
		timeOut(3)
		print("\"My resentment toward main{}-sama grows ever so slightly.\" {} grovels.".format(playNom, playNom))
		timeOut(6)
		print("\"Why can't I create food, when I can create life, clones, and a whole planet?!\"")
	elif tehGame == "look south":
		print("Your house is located here.")
		print(3)
		print("\"Hey!\" You think out loud, \"I have a plot to follow, I can’t dwindle here!\"")
		timeOut(6)
		print("…")
		timeOut(1)
		print("\"Maybe… I missed something…\" {} continues to ponder.".format(gender1))
		print(5)
		print("If you did, I’m not going to tell you.")
	elif tehGame == "look north":
		print("The outskirts of {} are seen off in the distance.".format(Town))
		timeOut(5)
		print("\"This is where I need to be!\" {} exclaims.".format(playNom))
		timeOut(4)
		print("\"I've got things to do, places to see, and adventures to be had!\"")
		timeOut(5)
		print("The common folk of {} look at you with very confused eyes.".format(Town))
	elif tehGame == "read allyways" or tehGame == "read dank allyways":
		print("The rejects of this world lie here in the depts of {}.".format(Town))
		timeOut(4)
		print("\"It'll be a cool little side story,\" {} contemplates about {} next actions.".format(playNom, gender1))
		timeOut(5)
		print("You never know what may lies beyond that, because Defunct {}-sama created this part of town.".format(playNom))
	else:
		globalCommand(tehGame, "Random passerbys of {} witness your gibberish and walk the other way.".format(Town))

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