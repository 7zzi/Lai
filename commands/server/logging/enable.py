async def main(ctx, c):
    from pathlib import Path
    if (Path(f"misc/logging.isEnabled/{ctx.guild.id}.txt").is_file()) == False:
        x = open(f"misc/logging.isEnabled/{ctx.guild.id}.txt", 'w')
        x.write('1')
        x.close()

        v = open(f"misc/logging.channel/{ctx.guild.id}.txt", 'w')
        v.write(c)
        v.close()

        await ctx.send('logging enabled.')
    else:
        x = open(f"misc/logging.isEnabled/{ctx.guild.id}.txt", 'r+')
        r = x.read()



        if (r) == '0':
            x.truncate(0)
            x.seek(0)
            x.write('1')

            v = open(f"misc/logging.channel/{ctx.guild.id}.txt", 'w')
            v.write(c)
            v.close()

            await ctx.send('logging enabled.')

        if (r) == '1':
            await ctx.send('logging is already enabled! #logs')

        x.close()