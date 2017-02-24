#inventory usage
def sayHello():
	print("hello")
array_godPouch = [0, 1, 2, 3, 4, 5]
array_godPouch[0] = "fist"
array_godPouch[1] = "wooden sword"
array_godPouch[2] = "[empty]"
array_godPouch[3] = "[empty]"
array_godPouch[4] = "[empty]"
array_godPouch[5] = "[empty]"
def replace(tool):
	for i in range (1, 5):
		if array_godPouch[i] != "[empty]":
			replaceSlot = input("{}'s' has ran out of space in {} inventory, what slot shall you replace?".format(playNom, gender2))
			array_godPouch[int(replaceSlot)] = tool
			print(array_godPouch)("HELLLP!!!")

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