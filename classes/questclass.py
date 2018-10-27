from newlines import *

class Quest:
    def __init__(self, id, goal, item):
        self.id = id
        self.goal = goal
        self.item = item

    def printQuest(self):
        print(self.goal)
        if self.item != "":
            print(self.item)
