import discord

from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "test")
    async def test(self, ctx):
        await ctx.send(f"hi {ctx.author.mention}")