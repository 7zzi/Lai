import re

def readCogs():
    cogs = []
    
    file = open("misc/cogs.txt", "r")
    temp = file.readlines() 
    
    for sub in temp:
        cogs.append(re.sub('\n', '', sub))
    
    file.close()

    return cogs