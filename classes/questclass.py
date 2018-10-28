from newlines import *

class Quest:
    def __init__(self, questing, id, goal, item):
        self.questing = questing
        self.id = id
        self.goal = goal
        self.item = item

    def printQuest(self):
        print(self.goal)
        if self.item != "":
            print(self.item)
