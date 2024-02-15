import discord

from discord.ext import commands

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="clearwarnings", aliases = ["clear"])
    @commands.has_permissions(moderate_members=True)
    async def clearwarn(self, ctx, member: discord.Member):
        with open(f'misc/warns/{member.id}.csv', 'w') as w:
            w.write("")
        await ctx.send(f"Cleared warnings for {member.mention}.")