import discord
from datetime import datetime

from discord.ext import commands
class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        a = bot

    @commands.command(name = "logging")
    async def logging(self, ctx, t):
        import commands.server.logging.disable
        import commands.server.logging.enable
        
        if t == "disable":
            await commands.server.logging.disable.main(ctx)

        if t == "enable":
            await commands.server.logging.enable.main(ctx)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        await message.channel.send(f"message deleted @ {datetime.now().strftime('%H:%M:%S UTC')}\n\ncontent: {message.content}\nchannel: {message.channel}")