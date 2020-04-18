from enum import Enum
from random import randint


# Citadel game
# Five colors: green (merchant), red (captain), yellow (king), blue (priest) et purple (wonder) 
# End game conditions 5 (or 7) neighboor in kingdom
# Then we count points.

buildingsDict = {
	"Tavern": "green", 
	"Tower": "red", 
	"Market": "green", 
	"Church": "blue", 
	"Palace": "yellow", 
	"Wall": "red", 
}
characters = ["Assassin","Thief","Wizard","King","Merchant","Architect","Priest","Captain"]
buildings = ["Tavern", "Tower", "Market", "Church", "Palace", "Wall", "Cathedral", "Barrack", "Castle", "Magic Tower", "Bewitched Dunjeon"]

class Player:
	def __init__(self, player, deck, role, money = 10, kingdom = [], alive = True, raidable = True):
		self.player = player
		self.deck = deck
		self.role = role
		self.money = money
		self.kingdom = kingdom
		self.alive = alive
		self.raidable = raidable
	
	def collect_money(self, addMoney):
		self.money += addMoney
		print("You collect income. +2 money")
		print(self.__repr__())
	
	def build_kingdom(self):
		pick = input("Pick one from : " + str(self.deck) + "\n")
		if int(self.deck.index(pick)) >= 0:
			self.kingdom.append(pick)
			self.deck.pop(self.deck.index(pick))
			print("You are building a new " + str(pick) + " into your kingdom.")
			print(self.__repr__())

	def pick_card_from_draw(self, addBuilding):
		self.deck.append(addBuilding)

	def to_die(self):
		self.alive = False

	def unraidable(self):
		self.raidable = False
		print("You are protected from captain's raid.")
		print(self.__repr__())

	def get_income_from_buildings(self, buildingsDict, color):
		for n in self.kingdom:
			for (bld, c) in buildingsDict.items():
				if n == bld and c == color:
					self.money += 1
		print("You are receiving money from your kingdom.")
		print(self.__repr__())

	def __repr__(self):
		return {
			'player':self.player, 
			'deck' : self.deck,
			'role':self.role, 
			'money':self.money, 
			'kingdom':self.kingdom,
			'alive':self.alive, 
			'raidable':self.raidable
		}

class Building:
	def __init__(self, buildingName, color, wonder):
		self.buildingName = buildingName
		self.color = color
		self.wonder = wonder

class Character:
	def __init__(self, role, color):
		self.role = role
		self.color = color

# for (character, color) in charactersDict.items():
# 	character = Character(character, color)
# 	print (character.__dict__)

def choose_player(choice):
	indexChar = characters.index(choice)
	characters.pop(indexChar)
	return choice
	
def create_deck(buildings):
	player_deck = []
	for b in range(4):
		player_deck.append(buildings[randint(0, (len(buildings) -1) )])
	return player_deck


def prepare_hand(buildings, nbCard=2):
	hand = []
	for i in range(nbCard):
		hand.append(buildings[randint(0, (len(buildings) -1) )])
	print("The hand : "+ str(hand))
	return hand

# def get_income_from_buildings(player, buildingsDict, color):
# 	for n in player.kingdom:
# 		for (bld, c) in buildingsDict.items():
# 			if n == bld and c == color:
# 				print("Adding 1 to player's money")
# 				player.money += 1


#########################
## CHARACTERS POWER    ##
# >>>>>>>>><<<<<<<<<<< ##
def use_power(player):
	if player.role == "Assassin":
		character_to_kill = input("Choose a character to kill: ")
		for i in listOfPlayers:
			if i.role == character_to_kill:
				i.to_die()
				print(character_to_kill + " is now dead. \n")
				print(i.__dict__)
		
	if player.role == "Thief":
		character_to_steal = input("Choose a character to steal: ")
		for i in listOfPlayers:
			if i.role == character_to_steal:
				player.money += i.money
				i.money = 0
				print("Stolen - "+ str(i.__dict__) + "\n")

		print("P1 - "+ str(player.__dict__) + "\n")

	if player.role == "Wizard":
		player_to_shuffle = input("Choose a player to shuffle with: ")
		player_to_shuffle = int(player_to_shuffle) - 1
		intermediate_deck = listOfPlayers[player_to_shuffle].deck
		listOfPlayers[player_to_shuffle].deck = player.deck
		player.deck = intermediate_deck
		print("P1 - "+ str(player.__dict__) + "\n")
		print("P2 - "+ str(listOfPlayers[player_to_shuffle].__dict__) + "\n")

	if player.role == "King":
		player.get_income_from_buildings(buildingsDict, "yellow")
		print(str(player.role)+"'s playing.")
		print (player.__dict__)
		pass

	if player.role == "Merchant":
		player.money += 1
		player.get_income_from_buildings(buildingsDict, "green")
		print (player.__dict__)

	if player.role == "Architect":
		print(str(player.role)+"'s playing.")
		buildOrDraw = input("BUILD (3) or DRAW (4) \n")
		if (buildOrDraw == "BUILD"):
			for i in range(3):
				toBuild = input("Choose what to build : " + str(player.deck) + " and 0 for quit. \n")
				if (toBuild == "0"):
					print(player.__dict__) 
					break
				elif player.deck.index(toBuild) >= 0:
					player.kingdom.append(toBuild)
					player.deck.pop(player.deck.index(toBuild))
				print(player.__dict__) 
		if (buildOrDraw == "DRAW"):
			hand_to_choose = prepare_hand(buildings, 4)
			pick_one = input("Choose one building : \n")
			if hand_to_choose.index(pick_one) >=0:
				player.deck.append(pick_one)
			
			print(player.__dict__)
	if player.role == "Priest":
		print(str(player.role)+"'s playing.")
		player.unraidable()
		player.get_income_from_buildings(buildingsDict, "blue")

	if player.role == "Captain":
		print(str(player.role)+"'s playing.")
		player.get_income_from_buildings(buildingsDict, "red")
		pass

# def build_neighboor(player):
# 	pick = input("Pick one from : " + str(player.deck) + "\n")
# 	print("You pick : " + str(pick))
# 	if int(player.deck.index(pick)) >= 0:
# 		player.build_kingdom(pick)
# 		return player


#########################
##      PLAY TURN      ##
# >>>>>>>>><<<<<<<<<<< ##
def play_turn(player):
	# 3 actions: 'collect', 'build' or 'use_power'
	action = input('Choose an action between COLLECT, BUILD or POWER as ' + player.role +'\n')
	if (action == "COLLECT"):
		# 'coins' or 'cards'
		drawOrCoins = input('Prefer +2 coins or draw 2 cards \n')
		if (drawOrCoins == 'COINS'):
			player.collect_money(2)
		if (drawOrCoins == 'CARDS'):
			choices = prepare_hand(buildings)
			player_choice = input('Choose a building \n')
			print(choices.index(player_choice))
			if int(choices.index(player_choice)) >= 0:
				player.pick_card_from_draw(player_choice)
				print(player.__dict__)
			else: 
				print('Buildings does not exist.')

	if (action == "BUILD"):
		player.build_kingdom()
	if (action == "POWER"):
		use_power(player)

print('             ')

######  Init ######
listOfPlayers = []

rolePlayer1 = input("Choose character player 1: \n")
player1 = Player(1, create_deck(buildings), choose_player(rolePlayer1))
listOfPlayers.append(player1)
print(player1.__dict__) 

rolePlayer2 = input("Choose character player 2:\n")
player2 = Player(2, create_deck(buildings), choose_player(rolePlayer2))
listOfPlayers.append(player2)
print(player2.__dict__)

### ALL Players

fullKingdom = False

while (fullKingdom != True):
	round = 0
	# One round
	for i in listOfPlayers:
		if (i.alive) :
			play_turn(i)
			round += 1
			print(round)
			if (len(i.kingdom) > 5):
				fullKingdom = True
				print("End Game!")

print('\n')


# Assassin = Character("Assassin", "grey")
# Thief = Character("Thief", "grey")
# Wizard = Character("Wizard", "grey")
# King = Character("King", "yellow")
# Merchant = Character("Merchant", "green")
# Architect = Character("Architect", "grey")
# Priest = Character("Priest", "blue")
# Captain = Character("Captain", "red")