import discord

from discord.ext import commands

class UnbanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "unban")
    @commands.has_guild_permissions(moderate_members = True)
    async def unban(self, ctx, m: discord.Member = None):
        if m == None:
            await ctx.send("You did not provide a user to unban.")
        else:
            await m.unban()
            
            await ctx.send(f"Unanned {m}.")