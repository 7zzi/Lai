from os import system
from reader import readCommands


try:
    import discord
except ImportError as e:
    print("pycord was not found, installing...")
    system("python3 -m pip install py-cord")
        
    import discord

from discord.ext import commands


# read cogs here, read token here
# loader.main(TOKEN, commands)
# call function from loader, with token & command list in arguments
# convert command list into cog list in /lai/loader.py & load those.

file = open("token.txt", "r")

for str in readCommands():
    exec(f"from {str} import {str.split('.')[-1].capitalize()}Cog")

intent = discord.Intents.default()
intent.members = True
intent.message_content = True

Lai = commands.Bot(command_prefix="'", intents = intent, activity = discord.Activity(type=discord.ActivityType.watching, name="u 😜😜"))
Lai.remove_command('help')

for cog in [
    TestCog,
    BanCog,
    UnbanCog,
    MuteCog,
    KickCog,
    MainCog,
    BaseCog,
    AddCog,
    RemoveCog,
    CloseCog,
    WarnCog,
    WarnsCog,
    ClearCog,
    ]:
    print(cog)
    Lai.add_cog(cog(Lai))

Lai.run(file.read())
file.close()