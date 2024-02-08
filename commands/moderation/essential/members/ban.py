import discord

from discord.ext import commands

class BanCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "ban")
    @commands.has_guild_permissions(moderate_members = True)
    async def ban(self, ctx, m: discord.Member = None, *, r: str):
        if m == None:
            await ctx.send("You did not provide a user to ban.")
        if r == None:
            await m.message(f"You've been banned from {ctx.guild.name}.")
            await m.ban()
            
            await ctx.send(f"Banned {m}.")
        else:
            await m.message(f"You've been banned from {ctx.guild.name} for {r}")
            await m.ban(reason = r)
            
            await ctx.send(f"Banned {m} for {r}")