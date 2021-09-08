import sys
import os
import console, sound 
from random import randint # Used for eightBall


# Shorthand functions 
cls = lambda: console.clear() # Clear console
peaSound = lambda: sound.play_effect('8ve:8ve-beep-timber') # Peasant's signature sound
nobSound = lambda: sound.play_effect('game:Woosh_1') # Nobleman's signature sound
roySound = lambda: sound.play_effect('game:Ding_3') # Royalty's signature sound

class Player():
	level = 0 # Track progress
	health = 0 # Track HP
	currentHP = health
	stamina = 0 # Track energy
	mana = 0 # Track magic potential
	xp = 0 # Track level-up progress
	gp = 0 # Track gold pieces (currency)
	className = '' # Track classtype

	
	# Classes will be set default values according to characteristics
	def classChoice(self, choice): # Initial class choice

		if choice == 1: # Peasant
			peaSound()
			self.level = 1
			self.health = 60
			self.currentHP = self.health
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
			self.currentHP = self.health
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
			self.currentHP = self.health
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

		totalXP = self.getXP() + experience # Keep track of current total experience

		while totalXP >= 100:

			if self.className == "Peasant": 
				self.setHP(self.getHP() + 10)
				self.setStam(self.getStam() + 6)
				self.setMana(self.getMana() + 5)
				# Total = 21
				
			elif self.className == "Nobleman":
				self.setHP(self.getHP() + 4)
				self.setStam(self.getStam() + 4)
				self.setMana(self.getMana() + 8)
				# Total = 16
			
			elif self.className == "Royalty":
				self.setHP(self.getHP() + 2)
				self.setStam(self.getStam() + 3)
				self.setMana(self.getMana() + 10)
				# Total = 15

			sound.play_effect('arcade:Powerup_1')
			self.level += 1 # Base upgrade
			self.currentHP = self.health # Reset HP to max // Free heal
			totalXP -= 100
		
		if totalXP < 100: # Keep track of total XP
			self.setXP(totalXP)
		
			
	# Getters and setters
	def getLVL(self):
		return self.level
	def setLVL(self, value):
		self.level = value
	
	def getHP(self):
		return self.health
	def setHP(self, value):
		self.health = value

	def getCurrentHP(self):
		return self.currentHP
	def setCurrentHP(self, value):
		self.currentHP = value
	
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
	
class Enemy():
	HP = 0 # Health
	MP = 0 # Mana
	XP = 0 # Kill experience
	DMG = 0 # Damage done to player
	Type = ""

	# def __init__(self, _HP, _MP, _XP, _DMG):
	# 	self.HP = _HP
	# 	self.MP = _MP
	# 	self.XP = _XP
	# 	self.DMG = _DMG

	def randomEnemy(self, number): # Takes a number between 1-100, set enemy depending on user luck

		if number <= 10: # Strong mob, 10% chance
			self.__init__(80, 10, 50, 20)
			self.Type = "Troll"
		if number <= 50 and number > 10: # Trash mob, 40% chance
			self.__init__(20, 0, 10, 5)
			self.Type = "Goblin"
		if number <= 80 and number > 50: # Tier 2 trash mob, 30% chance
			self.__init__(30, 0, 20, 10)
			self.Type = "Orc"
		if number <= 85 and number > 80: # Free xp mob, 5% chance
			self.__init__(40, 0, 30, 0)
			self.Type = "Bear cub"
		if number <= 90 and number > 85: # Boss mob, 5% chance
			self.__init__(80, 40, 60, 30)
			self.Type = "Wizard"
		if number <= 100 and number > 90: # Medium mob, 10% chance
			self.__init__(100, 0, 40, 15)
			self.Type = "Ogre"


	
class RPGame():
	
	isAlive = True
	
	def startGame(self, player):
		
		# Game setup
		cls()
		sound.play_effect('game:Click_1')
		self.characterChoice(player)
		
		while self.isAlive == True:

			# Adventure time
			self.adventure(player)
			# implement timer, 1-2 seconds
	
	def characterChoice(self, player):
		
		while self.isAlive == True: # While user hasn't decided to exit
			cls()
			userChoice = int(input("Pick a class\n\n1. Peasant\n2. Nobleman\n3. Royalty\n0. Exit"))
			
			if userChoice == 1: # User might pick to be a peasant
				cls()
				peaSound()

				print("Due to years of backbreaking work, Caldria's peasants are known to have a high tolerance for even the most grueling of tasks.\n\n")
				classChoice = int(input("Is this your class?\n1. Yes, I'm a peasant\n0. No, let me check others"))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return

			elif userChoice == 2: # User might choose a nobleman
				cls()
				nobSound()

				print("Born to a strong house with servants aplenty, the Caldrian noblemen are considered chivalrous and known to be healthy.\n\n")
				classChoice = int(input("Is this your class?\n1. Yes, I'm a Nobleman\n0. No, let me check others"))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return
			
			elif userChoice == 3: # Perhaps user went for royalty
				cls()
				roySound()

				print("Caldria's royalty are renown for their short temper, it's said that the magical books they looted from surrounding nations have essentially changed them.\n\n")
				classChoice = int(input("Is this your class?\n1. Yes, I'm Royalty\n0. No, let me check others"))
				
				if classChoice == 1:
					player.classChoice(userChoice)
					return
					 	
			elif userChoice == 0:
				self.isAlive = False
				return
				
							
	def adventure(self, player):
		
		cls()
		
		while self.isAlive == True:
			self.displayStats(player)
			userChoice = int(input('1. Explore\n2. Inventory\n3. Stats\n0. Exit'))
			cls()
			
			if userChoice == 1: # Explore
				# In order of priority
				# Add chance for combat, traveling merchant, find treasure, dungeon, town
				# encounter = randint(1, 100) # Decides what encounter to launch
				# if encounter <= 33:
				# 	self.combat(player)
				# elif encounter > 33 and encounter < 
				self.combat(player)

			elif userChoice == 2: # Inventory
				print('No items collected')
			elif userChoice == 3: # Player stats
				if player.getHP() >= 50:
					print("I'm okay")
				else:
					print("I could use some healing")
			elif userChoice == 0: # Exit game
				self.isAlive = False

	def combat(self, player):

		combatHP = player.getCurrentHP() # Keep track of health
		combatMP = player.getMana()
		combatEnergy = player.getStam()
		randNumber = randint(1, 100) # Create random variable to assign enemy encounter
		opponent = Enemy() # Instantiate enemy variable
		opponent.randomEnemy(randNumber) # Assign random enemy
		

		while combatHP > 0 or self.isAlive == True: # While player is still in the game

			combatEnergy += 5 # Player regenerates HP

			cls()
			self.displayCombatStats(player, combatMP)
			userChoice = input(f"{opponent.Type}: You'll be a nice meal\n\n1. Slap it over the head\n2. Attempt a takedown\n3. Inventory\n0. Exit")

			if userChoice == 1:
				combatEnergy -= 10
				opponent.HP -= 10

			if userChoice == 2:
				combatEnergy -= 20
				opponent.HP -= 20
			
			if userChoice == 3:
				print("Write me!")
			
			if userChoice == 0:
				self.isAlive = False



	def displayCombatStats(self, player, mana): # Keep track of current combat stats
		print(f'{player.className}\nHP: {player.getCurrentHP()}/{player.getHP} | MP: {mana}/{player.getMana()}\n')
	
	def displayStats(self, player): # For most menus
		print(f'{player.className}\nHP: {player.getCurrentHP()}/{player.getHP} | MP: {player.getMana()}\n')
	
	def displayFullStats(self, player): # For when user wants/needs to see their total stats
		print(f'{player.className}\nHP: {player.getCurrentHP()}/{player.getHP} | MP: {player.getMana()}\nGP: {player.getGP()} | XP: {player.getXP()}\n')



class EightBall():
	
	def runGame(self):
		cls()
		userChoice = 1
		sound.play_effect('casino:DieThrow3')
		
		# While user doesnt wanna leave
		while userChoice != 0:

			userChoice = int(input("Be illuminated by the EightBall\n1. Roll ball\n0. Exit"))

			cls()
			
			if userChoice == 1:
				sound.play_effect('casino:DieShuffle3')
				self.rollBall()
			
	def rollBall(self):
		side = randint(0,7)

		if side == 0:
			print("Believe so\n")
		elif side == 1:
			print("Muddy waters\n")
		elif side == 2:
			print("It's dark in here\n")
		elif side == 3:
			print("Yes\n")
		elif side == 4:
			print("Don't bet on it\n")
		elif side == 5:
			print("Could you repeat that?\n")
		elif side == 6:
			print("No\n")
		elif side == 7:
			print("Sleep on it\n")
	
def main():
	
	isAlive = True
	
	while isAlive == True:
	
		cls()
		sound.play_effect('digital:HighDown')
		print("NULL Arcade\n\nPick a game\n1. RPG -- In Progress\n2. EightBall -- Stable\n3. Load Save -- TBD\n0. Exit")
		gameChoice = int(input())
		
		if gameChoice == 1: # Run RPG
			game = RPGame()
			player = Player()
			game.startGame(player)
			del game, player


		elif gameChoice == 2: # Run EightBall
			game = EightBall()
			game.runGame()
			del game
		
		elif gameChoice == 3: # Load/Create a save file 
			print("TBD")
			# fileName = input("saveName: ")
			# gameSave = open(fileName, "w+")

		elif gameChoice == 0:
			isAlive = False

main() # Run program
