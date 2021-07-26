from discord.ext import commands
import discord
from discord.ext.commands import Cog
import json
import os
import random
from PIL import Image
class Admin(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = True
    @commands.command()
    async def changenickname(self,ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        em = discord.Embed(title=f"Nickname was changed for {member.mention}", color=0xfcba03)
        await ctx.send(embed=em)

    @commands.command(aliases=['prefix'], brief="Change prefix of SodynoizzGG bot")
    @commands.has_permissions(administrator=True)  # ensure that only administrators can use this command
    async def changeprefix(self,ctx, prefix):  # command: bl!changeprefix ...
        with open('data/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('data/prefixes.json', 'w') as f:  # writes the new prefix into the .json
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')  # confirms the prefix it's been changed to

    @commands.command(brief="Clear message")
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} Messages has been removed!', delete_after=5)

    @commands.command(pass_context=True)
    async def reload(self,ctx, *, msg):
        """Load a module."""
        await ctx.message.delete()
        try:
            if os.path.exists("custom_cogs/{}.py".format(msg)):
                self.bot.reload_extension("custom_cogs.{}".format(msg))
            elif os.path.exists("cogs/{}.py".format(msg)):
                self.bot.reload_extension("cogs.{}".format(msg))
            else:
                raise ImportError("No module named '{}'".format(msg))
        except Exception as e:
            await ctx.send('Failed to reload module: `{}.py`'.format(msg))
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('Reloaded module: `{}.py`'.format(msg))

    @commands.command(pass_context=True)
    async def unload(self,ctx, *, msg):
        """Unload a module"""
        await ctx.message.delete()
        try:
            if os.path.exists("cogs/{}.py".format(msg)):
                self.bot.unload_extension("cogs.{}".format(msg))
            elif os.path.exists("custom_cogs/{}.py".format(msg)):
                self.bot.unload_extension("custom_cogs.{}".format(msg))
            else:
                raise ImportError("No module named '{}'".format(msg))
        except Exception as e:
            await ctx.send('Failed to unload module: `{}.py`'.format(msg))
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('Unloaded module: `{}.py`'.format(msg))

    @commands.command(pass_context=True)
    async def load(self,ctx, *, msg):
        """Load a module"""
        await ctx.message.delete()
        try:
            if os.path.exists("cogs/{}.py".format(msg)):
                self.bot.load_extension("cogs.{}".format(msg))
            elif os.path.exists("custom_cogs/{}.py".format(msg)):
                self.bot.load_extension("custom_cogs.{}".format(msg))
            else:
                raise ImportError("No module named '{}'".format(msg))
        except Exception as e:
            await ctx.send('Failed to load module: `{}.py`'.format(msg))
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('Loaded module: `{}.py`'.format(msg))

    @commands.command(helpinfo='Picks a random hex color', aliases=['hex', 'colour'])
    async def color(self,ctx, inputcolor=''):
        '''
        Randomly picks a color, or displays a hex color
        '''
        if inputcolor == '':
            randgb = lambda: random.randint(0, 255)
            hexcode = '%02X%02X%02X' % (randgb(), randgb(), randgb())
            rgbcode = str(tuple(int(hexcode[i:i + 2], 16) for i in (0, 2, 4)))
            await ctx.send('`Hex: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
            heximg = Image.new("RGB", (64, 64), '#' + hexcode)
            heximg.save("color.png")
            await ctx.send(file=discord.File('color.png'))
        else:
            if inputcolor.startswith('#'):
                hexcode = inputcolor[1:]
                if len(hexcode) == 8:
                    hexcode = hexcode[:-2]
                elif len(hexcode) != 6:
                    await ctx.send('Make sure hex code is this format: `#7289DA`')
                rgbcode = str(tuple(int(hexcode[i:i + 2], 16) for i in (0, 2, 4)))
                await ctx.send('`Hex: #' + hexcode + '`\n`RGB: ' + rgbcode + '`')
                heximg = Image.new("RGB", (64, 64), '#' + hexcode)
                heximg.save("color.png")
                await ctx.send(file=discord.File('color.png'))
            else:
                await ctx.send('Make sure hex code is this format: `#7289DA`')

    @Cog.listener()
    async def on_ready(self):
        print('Bot Admin is ready')
def setup(bot):
    bot.add_cog(Admin(bot))