import discord

from discord.ext import commands

class KickCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "kick")
    @commands.has_guild_permissions(moderate_members = True)
    async def kick(self, ctx, m: discord.Member = None, *, r: str):
        if m == None:
            await ctx.send("You did not provide a user to kick.")
        if r == None:
            await m.message(f"You've been kicked from {ctx.guild.name}.")
            await m.kick()
            
            await ctx.send(f"Kicked {m}.")
        else:
            await m.message(f"You've been kicked from {ctx.guild.name} for {r}")
            await m.kick(reason = r)
            
            await ctx.send(f"Kicked {m} for {r}")