import sys
sys.path.append("C:/Users/matth/Documents/GitHub/Python-RPG/classes")
sys.path.append("C:/Users/matth/Documents/GitHub/Python-RPG/functions")

from random import randint as ri
from random import choice as ch
from itemlist import *
from newlines import *
from playerclass import Player
import inspectitem
from inspectitem import inspectItem
from giveitem import giveItem
from equipping import equipItem
from printmap import printMap
from questclass import Quest
from useitem import useItem
from monsterclass import Monster

#-----------------------------------------------------------------------

lvlmax = [
    {
        "health":20,
        "monsterlevel":2,
        "monsterhealth":15,
        "items":[minor_heal_pot, minor_heal_pot, minor_heal_pot, lesser_heal_pot, dagger, leather_armor]
    },
    {
        "health":25,
        "monsterlevel":3,
        "monsterhealth":25,
        "items":[minor_heal_pot, minor_heal_pot, lesser_heal_pot, lesser_heal_pot, dagger, dagger, leather_armor]
    }
]

#-----------------------------------------------------------------------
#Making the player

equipped = {
    "main":rusty_sword,
    "side":blank_item,
    "armor":rusty_armor
}
inv = [minor_heal_pot]
quest = Quest(False, 0, "", "")
bigboi()
name = input("What would you like your players name to be? \n")
player = Player(name, equipped, inv, 10, 1, quest, 0, 0)

#-----------------------------------------------------------------------
#The main loop
minimap = 1
bigboi()
while True:
    selection = input ("What would you like to do? \n")
    bigboi()

    if minimap == 1:
        printMap()
        newline()

    if selection == "stats":
        player.printBasics()
        newline()



    elif selection == "help":
        print("List of Commands:")
        print("stats")
        print("inv")
        print("equip item")
        print("inspect item")
        print("use item")
        print("move")
        print("toggle minimap")
        print("look around")
        newline()



    elif selection == "move":
        print("pretend you moved")
        newline()



    elif selection == "fmove":
        monster = ri(0,1)
        if monster == 1:
            monster = Monster(player, lvlmax)
            fight(player, monster)



    elif selection == "use item":
        useItem(player, lvlmax)



    elif selection == "toggle minimap":
        if minimap == 1:
            minimap = 0
        else:
            minimap == 1
        newline()



    elif selection == "look around":
        print("wow the void looks nice today")
        newline()



    elif selection == "inspect item":
        inspectItem(player)



    elif selection == "inventory" or selection == "inv":
        player.printInv()
        newline()



    elif selection == "give":
        giveItem(player)



    elif selection == "equip item":
        equipItem(player)



    else:
        print("That's not a command!")
        newline()
