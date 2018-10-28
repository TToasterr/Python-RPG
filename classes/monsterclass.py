from random import randint as ri
from random import choice as ch
from newlines import *

names = ["orc", "goblin", "skeleton", "zombie", "crazed miner", "crazed minor", "millenial"]

class Monster:
    def __init__(self, player, lvlmax, name, health, level, itemdrop):
        self.player = player
        self.name = ch(names)
        self.health = ri(5,lvlmax[self.player.level]["monsterhealth"])
        self.level = ri(1,lvlmax[self.player.level]["monsterlevel"])
        self.itemdrop = ch(lvlmax[self.player.level]["items"])