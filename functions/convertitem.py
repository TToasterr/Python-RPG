import itemlist

#This basically just takes an item by name and returns that same item but as a class
def convertItem(itemName):
    finished = 0
    realItem = ""
    for itemNum in range(len(itemlist.item_name_array)):
        if finished == 1:
            do = "nothing"
        elif itemName == itemlist.item_array[itemNum].name:
            finished = 1
            realItem = itemlist.item_array[itemNum]
    return(finished, realItem)
