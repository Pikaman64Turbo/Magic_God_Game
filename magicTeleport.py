import time
import sys
import inventory
#array_areaArena = [(0,0),(0,1),(1,0),(1,1),(1,-1),(0,1),(0,2),(1,2),(2,1),(2,2),(3,1),(3,2),(4,1),(4,2),(1,-2),(0,-1),(0,-2),(3,0),(4,0),(2,-1),(2,-2),(3,-1),(3,-2),(4,-1),(4,-2)]

#AllowMov_y = true
#AllowMov_x = true
#AllowBac_y = true
#AllowBac_x = true
whileVar = 0
gender = ""
gender1 = "notin"
gender2 = "notin"
plazmaI = "Electrocution I"
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
	time.sleep(t)

replace(plazmaI)
print ("Hello, human player!")
timeOut(2)
print ("Welcome to the world of ______. This is your life now.")
timeOut(3)
woldNom = input("What world do you live in? ->")
print ("{} is filled with dangerss in every corner. Realizm has escaped, and insanity is reality.".format(woldNom))
timeOut(4)
print ("This is the world that you have created, and you solely exist to rid the evils of {}.".format(woldNom))
timeOut(5)
print ("What I'm trying to say is {} is screwed.".format(woldNom))
timeOut(4)
print ("Your 'Good Deeds' are not defined my any vocabulary of mine, only you can define it. {} is on your shoulders.".format(woldNom))
timeOut(6)
print ("As a mortal god, it is your duty [and only your duty] to do 'Good Deeds'!")
timeOut(3)
playNom = input("I'm sorry, I forgot to ask for your name, God. ->")
print ("Alright, {}-sama! The world of {} is in your hands. Do not waste your life!".format(playNom, woldNom))
timeOut(4)
print ("WAIT! I need to know something before we start.")
timeOut(2)
while gender == "":
	gender = input("Are you a boy are a girl? ->")
	if (gender == "boy"):
		gender1 = "him"
		gender2 = "his"
		gender = "none"
	elif (gender == "girl"):
		gender1 = "she"
		gender2 = "her"
	else:
		print("That is not a gender, you need to see your local physician.")
		gender1 = "it"
		gender2 = "???"

print ("You are in your bedroom, try (examine Area) to see your immediate surroundings. Use (look South) to continue playing the game!")
while True:
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
		timeOut(3)
		print ("Surprisingly, the both of you were too lazy to create an actual house.")
	elif tehGame == "look south":
		print ("There's a window that peers out into darkness. You assume that it's a void.")
		timeOut(6)
		print ("There is a letter above the window.")
		timeOut(4)
		print ("'You can examine any noun [people, things, buildings] with the (read) command, even questionable items like #windows# and #people#.'")
	elif tehGame == "read letter":
		print("It reads: {You've figured out the puzzle! You're smarter than an average peasant!}")
		timeOut(4)
		print("{Did you know that you can (look) in any primary Cardinal direction?}")
	elif tehGame == "look north":
		print("You found a door to the outdoors!") 
		timeOut(3)
		print("Why you were tooo lazy to create windows that look into said outdoors, {} may never know.".format(woldNom))
		timeOut(7)
		print("Their's a post-it note above the door.")
	elif tehGame == "read post-it note":
		print("Congratulations! You solved the puzzle.")
		timeOut(3)
		print("\"Hey, {}-sama! This is a note from your evil version: you can combine Cardinal directions with the (move) command to move!!!\"")
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
	elif tehGame == "move south":
		print("{}-sama ran South and jumped through the window, where {} were sucked into the infinite darkness.".format(playNom, gender1))
		timeOut(5)
		print("\"Me-darn it! Why is there an evil version of me?\" Were your last words.")
		timeOut(7)
		print("\"What a loser!\" The defunct clone of {} said while being glued into {} computer screen".format(woldNom, gender2))
		timeOut(5)
		print("(Death by Window) {} died by trusting the antagonist. (Hint, move North)".format(playNom))
		sys.exit()
	elif tehGame == "move West":
		print("Without looking ahead, you move West and trip over your bed.")
		timeOut(5)
		print("\"Smooth move, idiot.\" {}'s clone shouts from the opposite end of the room.".format(playNom))
		timeOut(5)
		print("You don't bother to say anything as it would add fuel from the fire.")
	elif tehGame == "read Windows":
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
	elif tehGame == "move East":
		print("You barge into your defunct clone, \"What the blazes man!\" {}'s clone shouts.".format(playNom))
		timeOut(5)
		print("\"Get back to work,\" You yell at {}, \"Or I will absorb you!\"".format(gender1))
		timeOut(6)
		print("\"Make me.\" He threatens.")
		timeOut(3)
		moralChoice1 = input("Absorb him? ->")
		moralChoice1 = moralChoice1.lower()
		if moralChoice1 == "Yes":
			print("You have absorbed your clone, you monster!")
			timeOut(5)
			print("You have gained the {}! (not yet implemented)".format(plazmaI))
			replace(plazmaI)
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
	#elif tehGame ==
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