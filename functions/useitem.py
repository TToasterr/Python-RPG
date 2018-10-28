from newlines import *
from convertitem import *

weapons = ["Melee", "Ranged", "Magic"]

def useItem(player):
    bigboi()
    player.printEquipped()
    newline()
    player.printInv()
    newline()
    which = input("What item do you want to use? \n")

    item = convertItem(which)

    bigboi()
    if item[0] != 0:
        finished = 0
        item = item[1]

        if item.type in weapons:
            if item == player.equipped["main"] or item == player.equipped["side"]:
                if item.type == "Melee":
                    dmgType = "swing at"

                elif item.type == "Ranged":
                    dmgType = "shoot"

                elif item.type == "Magic":
                    dmgType = "curse"

                print("You %s the air and do %s damage." % (dmgType, item.power))
                newline()

            else:
                print("You cant use that item. You dont have it equipped.")
                newline()

        elif item.type == "Potion":
            for itm in range(len(player.inv)):
                if finished == 1:
                    do = "nothing"

                elif player.inv[itm].name == item.name:
                    player.inv.pop(itm)
                    finished = 1

            if finished != 1:
                print("You dont have that item.")
                newline()
                return()

            player.health += item.power
            print("You healed for %s health." % item.power)
            newline()

        else:
            print("You cant use armor. Its only for defense.")
            newline()

    else:
        print("You dont have that item.")
        newline()
