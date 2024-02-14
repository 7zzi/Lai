import discord

from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "logging enable")
    async def enable(self, ctx):
        ctx.send("in progress, ignore.")