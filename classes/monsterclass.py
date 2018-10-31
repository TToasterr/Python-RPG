from random import randint as ri
from random import choice as ch
from newlines import *

names = ["Orc", "Goblin", "Skeleton", "Zombie", "Crazed Miner", "Crazed Minor", "Millenial"]

class Monster:
    def __init__(self, player, lvlmax, name, health, level, itemdrop):
        self.player = player
        self.name = ch(names)
        self.health = ri(5,lvlmax[self.player.level]["monsterhealth"])
        self.level = ri(1,lvlmax[self.player.level]["monsterlevel"])
        self.itemdrop = ch(lvlmax[self.player.level]["items"])

    def printStats(self):
        print(self.name)
        print("Health: %s" % self.health)
        print("Level: %s" % self.level)
