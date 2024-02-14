import discord
from datetime import datetime

from discord.ext import commands
class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        a = bot

    @commands.command(name = "logging")
    @commands.has_guild_permissions(manage_messages = True)
    async def logging(self, ctx, t):
        import commands.server.logging.disable
        import commands.server.logging.enable
        
        if t == "disable":
            await commands.server.logging.disable.main(ctx)

        if t == "enable":
            await commands.server.logging.enable.main(ctx)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        x = open(f"misc/logging.isEnabled/{ctx.guild.id}.txt", 'r+')
        r = x.read()

        if (r) == '1':
            await message.channel.send(f"message deleted @ {datetime.now().strftime('%H:%M:%S UTC')}\n\ncontent: {message.content}\nchannel: {message.channel}")
        x.close()
