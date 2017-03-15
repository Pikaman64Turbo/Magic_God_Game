#inventory usage
#import magicTeleport
def sayHello():
	print("hello")
array_godPouch = [0, 1, 2, 3, 4, 5]
array_godPouch[0] = "Fist"
array_godPouch[1] = "Wooden Sword"
array_godPouch[2] = "[empty]"
array_godPouch[3] = "[empty]"
array_godPouch[4] = "[empty]"
array_godPouch[5] = "[empty]"
def Swapp(tool):
	pickUp = input("Would you like to pick it up? (y or n)")
	if pickUp == "n":
		print("You were too lethargic to pick up the item.")
	elif pickUp == "y":
		for i in range (1, 5):
			if array_godPouch[i] == "[empty]":
				array_godPouch[i] = tool
				return array_godPouch
			elif array_godPouch[i] != "[empty]":
				replaceSlot = input("{}'s' has ran out of space in {} inventory, what slot shall you replace?".format(playNom, gender2))
				array_godPouch[int(replaceSlot)] = tool
				print(array_godPouch)("")
	else:
		print("That is not an option")


#print(replace())





# def add:
# 	for i in range (1, 5):
# 		if array_godPouch[i] == "[empty]":
# 			array_godPouch[i] = ""
# 			print("{} has obtained {}".format(playNom, array_godPouch[i]))
# 		else replace






#print("I'm sorry, but your stuck with your hands.")
#array_godPouch = ["sword", "book", "rabbit", "", ""]
#array_godPouch[3] = "celery"