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
from random import randint as ri

def makeSeedMap():
    global seedmap
    seedmap = [[0 for y in range(5)] for x in range(5)]
    x = 2
    y = 2

    for i in range(25):
        try:
            if x >= 26 or y >= 26:
                x = 2
                y = 2
            seedmap[y][x] = i+1
        except:
            x = 2
            y = 2
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
            print(num)

def printSeedMap():
    for y in range(len(seedmap)):
        for x in range(len(seedmap)):
            if seedmap[x][y] <= 9:
                print("0", end='')
            print(seedmap[x][y], end=' ')
        print()
