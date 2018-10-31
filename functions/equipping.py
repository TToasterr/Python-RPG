from newlines import *
import itemlist

#Equips an item. P self explanatory xd
def equipItem(player):
	realItem = ""
	finished = 0
	owo = 0

	#Print the inventory and ask what item they want to equip
	player.printInv()
	newline()
	itemName = input("What is the item youd like to equip?\n")

	#Check if the item they input is actually in their inventory
	for itemNum in range(len(player.inv)):
		if player.inv[itemNum].name == itemName:
			owo = 1
			realItem = player.inv[itemNum]
			player.inv.pop(itemNum)
	#If it idnt in their inventory, tell them they dont have the item and end the function
	if owo != 1:
		bigboi()
		print("You don't have that item!")
		newline()
		return()

	#Check every item in the game to see if the item is real (Sort of useless just because it doesnt matter if its real it only matters if its in their inventory (Hey maybe this is why you cant equip custom items))
	# for itemNum in range(len(itemlist.item_name_array) - 1):
	# 	if finished == 1:
	# 		do = "nothing"
	# 	elif itemName == itemlist.item_array[itemNum].name:
	# 		finished = 1
	# 		realItem = itemlist.item_array[itemNum]

	#If the item is armor, replace anything they have in their armor slot with the item from their inventory and then add the item from the armor slot to their inventory
	if realItem.type == "Armor":
		tempHolder = player.equipped["armor"]
		if tempHolder != "":
			player.inv.append(tempHolder)
		player.equipped["armor"] = realItem
		bigboi()
		print("You equipped armor.")
		newline()
		return()
	#If the item is a weapon, ask which slot they want it in and then do the above stuff with that slot to replace the item
	elif realItem.type in itemlist.weapons:
		bigboi()
		player.printEquipped()
		newline()
		whichSlot = input("Which slot would you like to put this in? (Main or Side)\n")
		if whichSlot == "Main":
			tempHolder = player.equipped["main"]
			if tempHolder != "":
				player.inv.append(tempHolder)
			player.equipped["main"] = realItem
		elif whichSlot == "Side":
			tempHolder = player.equipped["side"]
			if tempHolder != "":
				player.inv.append(tempHolder)
			player.equipped["side"] = realItem
		else:
			bigboi()
			print("You didnt input Main or Side.")
			newline()
			return()
		bigboi()
		print("The item was equipped!")
		newline()
		return()
	#If the item is a potion, tell them they cant equip a potion
	else:
		bigboi()
		print("You can't equip a potion!")
		newline()
		return()
