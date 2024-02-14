import discord

from discord.ext import commands
class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "logging")
    async def logging(self, ctx, t):
        import commands.server.logging.disable
        import commands.server.logging.enable
        
        if t == "disable":
            await commands.server.logging.disable.main(ctx)

        if t == "enable":
            await commands.server.logging.enable.main(ctx)