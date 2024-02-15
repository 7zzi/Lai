import csv
import discord

from discord.ext import commands

class WarnsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="warns", aliases=["warnings"])
    @commands.has_permissions(manage_messages=True)
    async def warns(self, ctx, member: discord.Member):
        with open(f'warns/{ctx.guild.id}/{member.id}.csv', 'r') as w: 
            if w == None:
                await ctx.send(f"No warnings for {member.mention}.")
            else:
                await ctx.send(w.read())