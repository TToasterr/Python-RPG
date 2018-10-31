from random import randint as ri
from random import choice as ch
from newlines import *
from useitem import useItem
from itemlist import blank_item
import sys

def fight(player, monster, lvlmax):
    #Print the player stats and monster stats, then ask what they'd like to do
    player.printStats()
    newline()
    monster.printStats()
    newline()
    inp = input("What would you like to do? \n")
    bigboi()

    #If they choose attack, choose a random number between their min damage (0) and their max (their main power)
    #and subtract it from the monsters health. If the monster is dead (at or below 0 health) then end the function and
    #say they won. If its not, get random damage between 0 and the monsters maximum (depending on the level of the player)
    #and subtract it from the players health. If the player is dead, end the program. If they arent dead, restart the function.
    if inp == "attack":
        if player.equipped["armor"] != blank_item:
            if player.equipped["armor"].bufftype == player.equipped["main"].type:
                mpdmg = lvlmax[player.level]["playerdamage"] + player.equipped["main"].power + player.equipped["armor"].buffammount
            else:
                mpdmg = lvlmax[player.level]["playerdamage"] + player.equipped["main"].power
        else:
            mpdmg = lvlmax[player.level]["playerdamage"] + player.equipped["main"].power
        pdmg = ri(0,mpdmg)
        monster.health -= pdmg

        print("You attacked the monster for %s damage." % pdmg)
        newline()

        if monster.health <= 0:
            #pick random item from lvlmax
            #pick random number of xp from lvlmax
            item = ch(lvlmax[player.level]["items"])
            xpgain = ri(0,lvlmax[player.level]["xp"])
            player.xp += xpgain
            print("You won!")
            if item != blank_item:
                print("You got a(n) %s from the monster!" % item.name)
                player.inv.append(item)
            print("You got %s xp." % xpgain)
            newline()
            return()

        mdmg = (1 + ri(0,lvlmax[player.level]["monsterdamage"])) - (ri(0,player.equipped["armor"].power))
        if mdmg < 0:
            mdmg = 0
        player.health -= mdmg

        print("You took %s damage from the monster." % mdmg)

        if player.health <= 0:
            print("You lost!")
            newline()
            sys.exit()

    #If they choose to use an item, then use the item (I just stole the code from the use item script xd)
    #Issue - It prints their equipped too
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
