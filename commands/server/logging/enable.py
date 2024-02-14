async def main(ctx):
    from pathlib import Path
    
    if not (Path(f"misc/logging.isEnabled/{ctx.guild.id}.txt").is_file):
        x = open(f"misc/logging.isEnabled/{ctx.guild.id}.txt", 'w')
        x.write('1')
        x.close()

        await ctx.send('logging enabled. #logs')
    else:
        x = open(f"misc/logging.isEnabled/{ctx.guild.id}.txt", 'r+')
        r = x.read()

        if (r) == '0':
            print(x.readline())
            x.truncate(0)
            x.seek(0)

            x.write('1')

            await ctx.send('logging enabled. #logs')

        if (r) == '1':
            await ctx.send('logging is already enabled! #logs')