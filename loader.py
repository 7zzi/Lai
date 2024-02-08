def main(t, c):
    from os import system

    try:
        import discord
    except ImportError as e:
        print("pycord was not found, installing...")
        system("pip install py-cord")
        
        import discord

    from discord.ext import commands

    i = 0

    for str in c:
    
        i += 1
        exec(f"from {str} import {str.split('.')[-1].capitalize()}Cog")

    intent = discord.Intents.default()
    intent.members = True
    intent.message_content = True

    Lai = commands.Bot(command_prefix="'", intents = intent, activity = discord.Activity(type=discord.ActivityType.watching, name="😛 (')"))
    Lai.remove_command('help')

    for cog in [
                
                ]:

        Lai.add_cog(cog(Lai))

    Lai.run(t)