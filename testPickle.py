import pickle
class PlayerData:
		def InformationSave(self, playNom, woldNom, gender):
			self.playNom = ""
			self.woldNom = ""
			self.gender = ""
		def __init__(self, playNom, woldNom, gender):
			self.playNom = playNom
			self.woldNom = woldNom
			self.gender = gender
def main():
	Jessie = PlayerData("Jessie", "Hearthbound", "notClassified")
	Kyle = PlayerData("Kyle", "Earth", "male")
	print(Jessie.playNom)
	with open('mypickle.pickle', 'wb') as f:
		pickle.dump(Jessie, f)

	with open('mypickle.pickle') as f:
		LoadedJessie = pickle.load(f)
	print(LoadedJessie.playNom)


main()