import re

def readCommands():
    commands = []
    
    file = open("misc/commands.txt", "r")
    temp = file.readlines() 
    
    for sub in temp:
        commands.append(re.sub('\n', '', sub))
    
    file.close()

    return commands