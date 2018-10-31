from newlines import *
import itemlist

#Asks if they want to make a custom item. If they do, it gets the name, power, type, rarity, bufftype, and buffammount.
#If they dont want to create a new item, it asks for an item by id. It then appends the item (custom or not) to the players inventory.
def giveItem(player):
    found = 0
    corno = input("Do you want to make a custom item? \n")
    bigboi()
    if corno == "yes":
        name = input("Whats the item name? \n")
        newline()
        power = int(input("Whats the item power? \n"))
        newline()
        type = input("Whats the item type? \n")
        newline()
        rarity = input("Whats the item rarity? \n")
        newline()
        bufftype = input("Whats the item bufftype? \n")
        newline()
        buffammount = int(input("Whats the buff amount? \n"))
        bigboi()
        item = itemlist.Item(name, power, type, rarity, bufftype, buffammount)
        player.inv.append(item)
        itemlist.item_array.append(item)
    else:
        item = input("Enter the ID of the item:\n")
        if item in itemlist.item_name_array:
            for i in range(len(itemlist.item_name_array) - 1):
                if found == 1:
                    do = 'nothing'
                elif item == itemlist.item_name_array[i]:
                    item = itemlist.item_array[i]
                    player.inv.append(item)
                    found = 1
            bigboi()
            print("Added item to your inventory.")
            newline()
        else:
            bigboi()
            print("That item doesnt exist.")
            newline()
