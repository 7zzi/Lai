import discord

from discord.ext import commands

class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "mute")
    @commands.has_guild_permissions(moderate_members = True)
    async def mute(self, ctx, m: discord.Member, t, *, r: str):
        if m == None:
            await ctx.send("You did not provide a user to mute.")
        if t == None:
            await ctx.send("You haven't specified a mute duration.")
        if r == None:
            await m.send(f"You've been muted in {ctx.guild.name} for {r}, expires in {t}.")
            
            await ctx.send(f"Mute {m}.")
        else:
            await m.send(f"You've been banned from {ctx.guild.name} for {r}")
            await m.ban(reason = r)
            
            await ctx.send(f"Muted {m} for {r}")