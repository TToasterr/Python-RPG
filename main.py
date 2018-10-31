import sys
sys.path.append("C:/Users/matth/Documents/GitHub/Python-RPG/classes")
sys.path.append("C:/Users/matth/Documents/GitHub/Python-RPG/functions")

from random import randint as ri
from random import choice as ch
from itemlist import *
from newlines import *
from playerclass import Player
from inspectitem import inspectItem
from giveitem import giveItem
from equipping import equipItem
from printmap import printMap
from questclass import Quest
from useitem import useItem
from monsterclass import Monster
from fight import fight
from randomgen import makeSeedMap
from randomgen import printSeedMap

#-----------------------------------------------------------------------

lvlmax = [
    {
        "health":20,
        "playerdamage":5,
        "monsterlevel":2,
        "monsterhealth":15,
        "monsterdamage":3,
        "xp":10,
        "maxxp":20,
        "items":[minor_heal_pot, minor_heal_pot, minor_heal_pot, lesser_heal_pot, dagger, leather_armor, blank_item, blank_item, blank_item]
    },
    {
        "health":25,
        "playerdamage":7,
        "monsterlevel":3,
        "monsterhealth":25,
        "monsterdamage":5,
        "xp":20,
        "maxxp":40,
        "items":[minor_heal_pot, minor_heal_pot, lesser_heal_pot, lesser_heal_pot, dagger, dagger, leather_armor, blank_item, blank_item]
    },
    {
        "health":30,
        "playerdamage":10,
        "monsterlevel":4,
        "monsterhealth":40,
        "monsterdamage":7,
        "xp":30,
        "maxxp":60,
        "items":[minor_heal_pot, lesser_heal_pot, lesser_heal_pot, heal_pot, dagger, shortbow, leather_armor, blank_item]
    },
    {
        "health":40,
        "playerdamage":15,
        "monsterlevel":5,
        "monsterhealth":50,
        "monsterdamage":10,
        "xp":50,
        "maxxp":100,
        "items":[lesser_heal_pot, lesser_heal_pot, heal_pot, heal_pot, shortsword, shortbow, leather_armor]
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
player = Player(name, equipped, inv, 10, 0, 0, quest, 0, 0)

#-----------------------------------------------------------------------
#The main loop
minimap = 0
bigboi()
while True:
    if player.xp >= lvlmax[player.level]["maxxp"]:
        player.xp = 0
        player.level += 1

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
            monster = Monster(player, lvlmax, "", "", "", "")
            fight(player, monster, lvlmax)



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

    elif selection == "seedmap":
        seedmap = makeSeedMap()
        printSeedMap()


    else:
        print("That's not a command!")
        newline()
