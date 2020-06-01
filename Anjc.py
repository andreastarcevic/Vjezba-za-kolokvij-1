import random
from AnjcError import AnjcError

#Autor : Petar Garmaz

class Anjc():
	def __init__(self):
		self.playerTotalScore = 0
		self.botTotalScore = 0

	def TitleCard(self):
		print("===========================================================================")
		print("================================= A N J C =================================")
		print("===========================================================================\n")

	def MainMenu(self):
		print("[1] Igraj Anjc")
		print("[x] Izlaz\n")

		return input("Šta želite raditi? ")

	def CardPullingMenu(self):
		print("[1] Izvuci novu kartu")
		print("[x] Stani\n")

		return input("Šta želite raditi? ")

	def PlayerPullCard(self):
		Cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Dečko", "Dama", "Kralj", "Kec"]
		
		pulledCard = random.choice(Cards)

		cardScore = 0

		if(pulledCard == "2"):
			cardScore = 2
		elif (pulledCard == "3"):
			cardScore = 3
		elif (pulledCard == "4"):
			cardScore = 4
		elif (pulledCard == "5"):
			cardScore = 5
		elif (pulledCard == "6"):
			cardScore = 6
		elif (pulledCard == "7"):
			cardScore = 7
		elif (pulledCard == "8"):
			cardScore = 8
		elif (pulledCard == "9"):
			cardScore = 9
		elif (pulledCard == "10"):
			cardScore = 10
		elif (pulledCard == "Dečko"):
			cardScore = 10
		elif (pulledCard == "Dama"):
			cardScore = 10
		elif (pulledCard == "Kralj"):
			cardScore = 10
		elif (pulledCard == "Kec"):
			cardScore = 1
		
		self.playerTotalScore += cardScore

		return pulledCard
	
	def BotPullCard(self):
		Cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Dečko", "Dama", "Kralj", "Kec"]
		
		pulledCard = random.choice(Cards)

		cardScore = 0

		if(pulledCard == "2"):
			cardScore = 2
		elif (pulledCard == "3"):
			cardScore = 3
		elif (pulledCard == "4"):
			cardScore = 4
		elif (pulledCard == "5"):
			cardScore = 5
		elif (pulledCard == "6"):
			cardScore = 6
		elif (pulledCard == "7"):
			cardScore = 7
		elif (pulledCard == "8"):
			cardScore = 8
		elif (pulledCard == "9"):
			cardScore = 9
		elif (pulledCard == "10"):
			cardScore = 10
		elif (pulledCard == "Dečko"):
			cardScore = 10
		elif (pulledCard == "Dama"):
			cardScore = 10
		elif (pulledCard == "Kralj"):
			cardScore = 10
		elif (pulledCard == "Kec"):
			cardScore = 1
		
		self.botTotalScore += cardScore

		return pulledCard

	def Play(self):
		choice = ""
		pullCard = ""

		self.botTotalScore = 0
		self.playerTotalScore = 0
		
		while(choice != "x"):
			self.TitleCard()
			choice = self.MainMenu()
			print("=" * 75)

			if(choice != "x"):
				if(self.playerTotalScore <= 21 and self.playerTotalScore <= 21):
					pullCard = self.CardPullingMenu()

				while(pullCard != "x"):
					if(pullCard == "1"):
						if(self.playerTotalScore <= 21 and self.playerTotalScore <= 21):
							print("Vi ste izvukli: {}".format(self.PlayerPullCard()))
							print("Bot je izvukao: {}".format(self.BotPullCard()))
							print("=" * 75)
							print("Vi imate {} bodova".format(self.playerTotalScore))
							print("Bot ima {} bodova".format(self.botTotalScore))
							print("=" * 75)
							pullCard = self.CardPullingMenu()
							print("=" * 75)			

						elif(self.playerTotalScore > 21):
							print("Bot je pobijedio!\n")
							self.Play()

						elif(self.botTotalScore > 21):
							print("Vi ste pobijedili!\n")
							self.Play()

					elif(pullCard == "x"):
						if(self.playerTotalScore > self.botTotalScore):
							print("Vi ste pobijedili!\n")
							self.Play()

						elif(self.playerTotalScore < self.botTotalScore):
							print("Bot je pobijedio!\n")
							self.Play()

						else:
							print("Neriješeno\n")
							self.Play()

					else:
						raise AnjcError(102)
				

			elif(choice == "x"):
				print("Doviđenja!")
			else:
				raise AnjcError(101)

if __name__ == "__main__":
	Anjc().Play()