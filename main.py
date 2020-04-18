from random import randint
from char import use_power
from player import Player
from building import Building

'''
Read README.md to discover and understand the game!
'''

#### A CORRIGER : choix des persos, prix batiments

buildings = ["Tavern", "Tower", "Market", "Church", "Palace", "Wall", "Cathedral", "Barrack", "Castle", "Magic Tower", "Bewitched Dunjeon"]

buildingsDict = {
	"Tavern": "green", 
	"Tower": "red", 
	"Market": "green", 
	"Church": "blue", 
	"Palace": "yellow", 
	"Wall": "red", 
}

class Character:
	def __init__(self, role, color):
		self.role = role
		self.color = color

# for (character, color) in charactersDict.items():
# 	character = Character(character, color)
# 	print (character.__dict__)
characters = ["Assassin","Thief","Wizard","King","Merchant","Architect","Priest","Captain"]
def choose_character(choice):
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

# def build_district(player):
# 	pick = input("Pick one from : " + str(player.deck) + "\n")
# 	print("You pick : " + str(pick))
# 	if int(player.deck.index(pick)) >= 0:
# 		player.build_kingdom(pick)
# 		return player


######  Init ######
listOfPlayers = []

rolePlayer1 = input("Choose character player 1: \n")
player1 = Player(1, create_deck(buildings), choose_character(rolePlayer1))
listOfPlayers.append(player1)
print(player1.__dict__) 

rolePlayer2 = input("Choose character player 2:\n")
player2 = Player(2, create_deck(buildings), choose_character(rolePlayer2))
listOfPlayers.append(player2)
print(player2.__dict__)

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
		use_power(player, listOfPlayers)

print('             ')



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