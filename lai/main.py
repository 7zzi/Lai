from os import system

try:
    from dotenv import load_dotenv
except ImportError as e:
    print("dotenv was not found, installing...")
    system("pip install python-dotenv")

from dotenv import load_dotenv
from os     import getenv
from reader import readCogs

import loader

