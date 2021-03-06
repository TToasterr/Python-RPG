from newlines import *

class Player:
    def __init__(self, name, equipped, inv, health, level, xp, quest, x, y):
        self.name = name
        self.equipped = equipped
        self.inv = inv
        self.health = health
        self.level = level
        self.xp = xp
        self.quest = quest
        self.x = x
        self.y = y

    def printEquipped(self):
        print("Main: %s" % self.equipped["main"].name)
        print("Side: %s" % self.equipped["side"].name)
        print("Armor: %s" % self.equipped["armor"].name)

    def printBasics(self):
        print("Name: %s" % self.name)
        newline()
        print("Health: %s" % self.health)
        print("Level: %s" % str(int(self.level) + 1))
        print("XP: %s" % self.xp)
        newline()
        print("Main: %s" % self.equipped["main"].name)
        print("Side: %s" % self.equipped["side"].name)
        print("Armor: %s" % self.equipped["armor"].name)

        if self.quest.questing:
            newline()
            self.quest.printQuest()

    def printInv(self):
        print("Inventory: ")
        for item in self.inv:
            item.printName()

    def printStats(self):
        print("Your health: %s" % self.health)
        print("Your level: %s" % str(int(self.level) + 1))
