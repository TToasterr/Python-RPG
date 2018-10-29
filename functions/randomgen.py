#Quality art
# ─██ ██ ██ ██ ██ ██ ██ ─ ██ ██ ██ ── ── ── ── ── ██ ██ ██ ─ ██ ██ ██ ██ ██ ██ ██ ─
# ─██ ░░ ░░ ░░ ░░ ░░ ██ ─ ██ ░░ ██ ── ── ── ── ── ██ ░░ ██ ─ ██ ░░ ░░ ░░ ░░ ░░ ██ ─
# ─██ ░░ ██ ██ ██ ░░ ██ ─ ██ ░░ ██ ── ── ── ── ── ██ ░░ ██ ─ ██ ░░ ██ ██ ██ ░░ ██ ─
# ─██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ── ── ── ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ─
# ─██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ██ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ─
# ─██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ─
# ─██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ─
# ─██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ── ██ ░░ ██ ─ ██ ░░ ██ ── ██ ░░ ██ ─
# ─██ ░░ ██ ██ ██ ░░ ██ ─ ██ ░░ ██ ██ ██ ░░ ██ ██ ██ ░░ ██ ─ ██ ░░ ██ ██ ██ ░░ ██ ─
# ─██ ░░ ░░ ░░ ░░ ░░ ██ ─ ██ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ██ ─ ██ ░░ ░░ ░░ ░░ ░░ ██ ─
# ─██ ██ ██ ██ ██ ██ ██ ─ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ─ ██ ██ ██ ██ ██ ██ ██ ─
# ─── ── ── ── ── ── ── ─ ── ── ── ── ── ── ── ── ── ── ── ─ ── ── ── ── ── ── ── ─

#Okay now for the code
from random import randint as ri

def makeSeedMap():
    global seedmap
    #Creates the blank map and sets the cursor to it
    seedmap = [[0 for y in range(5)] for x in range(5)]
    x = 2
    y = 2

    #Fills the map with random numbers along a path
    #These numbers will be turned into chunks later
    for i in range(25):
        try:
            #If cursor hits the edge, go to center (i have to do this cuz python is the large homo)
            if x >= 26 or y >= 26:
                x = 2
                y = 2
            seedmap[y][x] = i+1
        except:
            #If cursor hits edge, go to center
            x = 2
            y = 2
        #Cursor goes in a direction
        num = ri(1,4)
        if num == 1:
            x += 1
        elif num == 2:
            x -= 1
        elif num == 3:
            y += 1
        elif num == 4:
            y -= 1
        else:
            #This should never happen
            print("ya goofed the seedmap congrats")

#Self explanitory
def printSeedMap():
    for y in range(len(seedmap)):
        for x in range(len(seedmap)):
            if seedmap[x][y] <= 9:
                print("0", end='')
            print(seedmap[x][y], end=' ')
        print()
