import sys
import os
import console, sound

# Clear screen
cls = lambda: console.clear()

class Player():
	level = 0
	health = 0
	stamina = 0
	mana = 0
	xp = 0
	gp = 0
	rclass = ''
	
	def classChoice(self, choice):

		if choice == 1: # Peasant
			sound.play_effect('8ve:8ve-beep-timber')
			self.level = 1
			self.health = 60
			self.stamina = 80
			self.mana = 0 
			self.xp = 0
			self.gp = 0
			self.rclass = "Peasant"
		elif choice == 2: # Nobleman
			sound.play_effect('game:Woosh_1')
			self.level = 1
			self.health = 100
			self.stamina = 50
			self.mana = 0
			self.xp = 0
			self.gp = 80
			self.rclass = "Nobleman"
		elif choice == 3: # Royalty
			sound.play_effect('game:Ding_3')
			self.level = 1
			self.health = 100
			self.stamina = 30
			self.mana = 10
			self.xp = 0
			self.gp = 0
			self.rclass = "Royalty"
		
	def levelUP(self):
		self.setLVL(1) # Base upgrade
		
		if self.rclass == "Peasant":
			setHP(10)
			setStam(6)
			setMana(5)
			# Total = 21
			
		if self.rclass == "Nobleman":
			setHP(4)
			setStam(4)
			setMana(8)
			# Total = 16
		
		if self.rclass == "Royalty":
			setHP(2)
			setStam(3)
			setMana(10)
			# Total = 15
			
		self.xp = 0 
		
			
	
	def getLVL(self):
		return self.level
	def setLVL(self, value):
		self.level += value
	
	def getHP(self):
		return self.health
	def setHP(self, value):
		self.health += value
	
	def getStam(self):
		return self.stamina
	def setStam(self, value):
		self.stamina += value
	
	def getMana(self):
		return self.mana
	def setMana(self, value):
		self.mana += value
		
	def getXP(self):
		return self.xp
	def setXP(self, value):
		self.xp += value
		
	def getGP(self):
		return self.gp
	def setGP(self, value):
		self.gp += value
	
	
	
		
class RPGame():
	
	def startGame(player):
		
		# Game setup
		sound.play_effect('game:Click_1')
		userChoice = input("Pick a class\n1. Peasant\n2. Nobleman\n3. Royalty\n0. Exit")
		userChoice = int(userChoice)
		
		if userChoice == 0:
			return

		player.classChoice(userChoice)
		cls()
		
		# Adventure time
		adventure(player)
		# implement timer, 1-2 seconds
		
	def adventure(player):
		print(f'HP: {player.getHP() | MP: {player.getMana()}}')

def main():
	
	fileName = input("saveName: ")
	gameSave = open(fileName, "w+")
	cls()
	
	gameChoice = input("Pick a game\n1. RPG -- In Progress\n2. EightBall -- TBD\n0. Exit")
	gameChoice = int(gameChoice)
	cls()
	
	if gameChoice == 1:
		game = RPGame()
		player = Player()
		RPGame.startGame(player)
		del game
		
	elif gameChoice == 2:
		return 0
		# implement random
		# switch random 
	elif gameChoice == 0:
		return 0

# Run program
main()

