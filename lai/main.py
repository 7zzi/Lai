from os import system

try:
    from dotenv import load_dotenv
except ImportError as e:
    print("dotenv was not found, installing...")
    system("pip install python-dotenv")

from dotenv import load_dotenv
from os     import getenv
from reader import readCommands

import loader

# read cogs here, read token here

# call function from loader, with token & command list in arguments
# convert command list into cog list in /lai/loader.py & load those.