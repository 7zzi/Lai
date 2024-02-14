async def main(ctx):
    x = open(f"misc/logging.isEnabled/{ctx.guild.id}.txt", 'w')
    x.write('0')
    x.close()

    await ctx.send('logging disabled.')