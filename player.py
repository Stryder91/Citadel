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