from random import randint as ri
from random import choice as ch
from newlines import *
from useitem import useItem
import sys

def fight(player, monster, lvlmax):
    player.printStats()
    newline()
    monster.printStats()
    newline()
    inp = input("What would you like to do? \n")
    bigboi()

    if inp == "attack":
        mpdmg = lvlmax[player.level]["playerdamage"] + player.equipped["main"].power
        pdmg = ri(0,mpdmg)
        monster.health -= pdmg

        print("You attacked the monster for %s damage." % pdmg)
        newline()

        if monster.health <= 0:
            print("You won!")
            newline()
            return()

        mdmg = 1 + ri(0,lvlmax[player.level]["monsterdamage"])
        player.health -= mdmg

        print("You took %s damage from the monster." % mdmg)

        if player.health <= 0:
            print("You lost!")
            newline()
            sys.exit()

    elif inp == "use item":
        useItem(player, lvlmax)
        mdmg = 1 + ri(0,lvlmax[player.level]["monsterdamage"])
        player.health -= mdmg

        print("You took %s damage from the monster." % mdmg)

        if player.health <= 0:
            print("You lost!")
            newline()
            sys.exit()

    newline()
    fight(player, monster, lvlmax)
