import discord
from datetime import datetime

from discord.ext import commands
class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name = "logging")
    @commands.has_guild_permissions(manage_messages = True)
    async def logging(self, ctx, t, *, c = None):
        import commands.server.logging.disable
        import commands.server.logging.enable
        
        if t == "disable":
            await commands.server.logging.disable.main(ctx)

        if t == "enable":
            await commands.server.logging.enable.main(ctx, c)

    @commands.Cog.listener()
    async def on_message_delete(self, ma):
        e = open(f"misc/logging.isEnabled/{ma.guild.id}.txt", 'r+')
        et = e.read()

        cf = open(f"misc/logging.channel/{ma.guild.id}.txt", 'r')
        c = str(cf.read()).replace("<#", '').replace(">", '')

        logChannel = await discord.utils.get_or_fetch(ma.guild, 'channel', c, default=None)

        if (et) == '1':
            await logChannel.send(f"message deleted @ {datetime.now().strftime('%H:%M:%S UTC')}\n\ncontent: {ma.content}\nchannel: {ma.channel.mention}\nauthor: {ma.author.mention}")
        
        e.close()
        cf.close()
