import sys
import os
import console, sound 
from random import * # Used for eightBall


# Shorthand functions 
cls = lambda: console.clear() # Clear console
peaSound = lambda: sound.play_effect('8ve:8ve-beep-timber') # Peasant's signature sound
nobSound = lambda: sound.play_effect('game:Woosh_1') # Nobleman's signature sound
roySound = lambda: sound.play_effect('game:Ding_3') # Royalty's signature sound

class Player():
	level = 0
	health = 0
	stamina = 0
	mana = 0
	xp = 0
	gp = 0
	className = ''
	
	# Classes will be set default values according to characteristics
	def classChoice(self, choice): # Initial class choice

		if choice == 1: # Peasant
			peaSound()
			self.level = 1
			self.health = 60
			self.stamina = 80
			self.mana = 0 
			self.xp = 0
			self.gp = 0
			self.className = "Peasant"
			# Total = 140
		elif choice == 2: # Nobleman
			nobSound()
			self.level = 1
			self.health = 100
			self.stamina = 50
			self.mana = 5
			self.xp = 0
			self.gp = 80
			self.className = "Nobleman"
			# Total = 155
		elif choice == 3: # Royalty
			roySound()
			self.level = 1
			self.health = 100
			self.stamina = 30
			self.mana = 15
			self.xp = 0
			self.gp = 200
			self.className = "Royalty"
			# Total = 145
		
		cls()
		
	# Use on user XP gain
	# Perhaps later make it so bosses can level up too
	def islevelUP(self, experience):

		currentXP = self.getXP() + experience # 

		if currentXP >= 100:
			sound.play_effect('arcade:Powerup_1')
			self.setLVL(1) # Base upgrade
			
			if self.className == "Peasant": 
				self.setHP(self.getHP() + 10)
				self.setStam(self.getStam() + 6)
				self.setMana(self.getMana() + 5)
				# Total = 21
				
			if self.className == "Nobleman":
				self.setHP(self.getHP() + 4)
				self.setStam(self.getStam() + 4)
				self.setMana(self.getMana() + 8)
				# Total = 16
			
			if self.className == "Royalty":
				self.setHP(self.getHP() + 2)
				self.setStam(self.getStam() + 3)
				self.setMana(self.getMana() + 10)
				# Total = 15
			
			self.xp -= 100
		
		else:
			self.setXP(currentXP)
		
			
	# Getters and setters
	def getLVL(self):
		return self.level
	def setLVL(self, value):
		self.level = value
	
	def getHP(self):
		return self.health
	def setHP(self, value):
		self.health = value
	
	def getStam(self):
		return self.stamina
	def setStam(self, value):
		self.stamina = value
	
	def getMana(self):
		return self.mana
	def setMana(self, value):
		self.mana = value
		
	def getXP(self):
		return self.xp
	def setXP(self, value):
		self.xp = value
		
	def getGP(self):
		return self.gp
	def setGP(self, value):
		self.gp = value
	
	
class RPGame():
	
	isAlive = True
	
	def startGame(self, player):
		
		# Game setup
		cls()
		sound.play_effect('game:Click_1')
		
		while self.isAlive == True:
			self.characterChoice(player)
			# Adventure time
			self.adventure(player)
			# implement timer, 1-2 seconds
	
	def characterChoice(self, player):
		secondChoice = 0
		
		while secondChoice == 0:
			cls()
			userChoice = int(input("Pick a class\n\n1. Peasant\n2. Nobleman\n3. Royalty\n0. Exit"))
			
			if userChoice == 1:
				cls()
				peaSound()

				print("Due to years of backbreaking work, Caldria's peasants are known to have a high tolerance for even the most grueling of tasks.\n\n")
				secondChoice = int(input("Is this your class?\n1. Yes, I'm a peasant\n0. No, let me check others"))
				
				if secondChoice == 1:
					player.classChoice(userChoice)
			
			if userChoice == 2:
				cls()
				nobSound()

				print("Born to a strong house with servants aplenty, the Caldrian noblemen are considered chivalrous and known to be healthy.\n\n")
				secondChoice = int(input("Is this your class?\n1. Yes, I'm a Nobleman\n0. No, let me check others"))
				
				if secondChoice == 1:
					player.classChoice(userChoice)
			
			if userChoice == 3:
				cls()
				roySound()

				print("Caldria's royalty are renown for their short temper, it's said that the magical books they looted from surrounding nations have essentially changed them.\n\n")
				secondChoice = int(input("Is this your class?\n1. Yes, I'm Royalty\n0. No, let me check others"))
				
				if secondChoice == 1:
					player.classChoice(userChoice)
					 	
			if userChoice == 0:
				self.isAlive = False
				return
							
							
	def adventure(self, player):
		
		cls()
		userChoice = 1
		
		while userChoice != 0:
			self.displayStats(player)
			userChoice = int(input('1. Explore\n2. Items\n3. Stats\n0. Exit'))
			cls()
			
			if userChoice == 1:
				print('Troll up ahead')
			elif userChoice == 2:
				print('No items collected')
			elif userChoice == 3:
				if player.getHP() >= 50:
					print("I'm okay")
				else:
					print("I could use some healing")

	
	def displayStats(self, player):
		 print(f'HP: {player.getHP()} | MP: {player.getMana()}\n')
	
	
class EightBall():
	
	def runGame(self):
		cls()
		userChoice = 1
		sound.play_effect('casino:DieShuffle3')
		
		# While user doesnt wanna leave
		while userChoice != 0:

			userChoice = int(input("Be illuminated by the EightBall\n1. Roll ball\n0. Exit"))

			cls()
			
			if userChoice == 1:
				sound.play_effect('casino:DieThrow3')
				self.rollBall()
			
	def rollBall(self):
		side = randint(0,7)

		if side == 0:
			print("Believe so")
		elif side == 1:
			print("Muddy waters")
		elif side == 2:
			print("It's dark in here")
		elif side == 3:
			print("Yes")
		elif side == 4:
			print("Don't bet on it")
		elif side == 5:
			print("Could you repeat that?")
		elif side == 6:
			print("No")
		elif side == 7:
			print("Sleep on it")
		
		print('\n')
	
def main():
	
	gameChoice = 1
	
	while gameChoice != 0:
	
		cls()
		sound.play_effect('digital:HighDown')
		print("Arcade NULL\n\nPick a game\n1. RPG -- In Progress\n2. EightBall -- TBD\n3. Load Save\n0. Exit")
		gameChoice = int(input())
		
		if gameChoice == 1:
			game = RPGame()
			player = Player()
			game.startGame(player)
			del game, player
			
		elif gameChoice == 2:
			game = EightBall()
			game.runGame()
			# implement random
			# switch random 
		
		elif gameChoice == 3:
			fileName = input("saveName: ")
			gameSave = open(fileName, "w+")
# Run program
main()
