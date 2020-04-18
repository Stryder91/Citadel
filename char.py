#########################
## CHARACTERS POWER    ##
# >>>>>>>>><<<<<<<<<<< ##
def use_power(player, listOfPlayers):
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
		player_to_shuffle = input("Choose a player [1] | [2] to shuffle with: ")
		player_to_shuffle = int(player_to_shuffle) - 1
		if listOfPlayers[player_to_shuffle]:
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