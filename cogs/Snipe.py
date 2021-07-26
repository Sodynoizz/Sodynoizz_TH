import discord
from discord.ext import commands
from discord.ext.commands import Cog
import asyncio
snipe_message_author = {}
snipe_message_content = {}

class snipe(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cancelled = False

    @Cog.listener()
    async def on_ready(self):
        print('Bot Snipe is ready')

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        await asyncio.sleep(60)
        del snipe_message_author[message.channel.id]
        del snipe_message_content[message.channel.id]

    @commands.command(name='snipe')
    async def snipe(self,ctx):
        channel = ctx.channel
        try:  # This piece of code is run if the bot finds anything in the dictionary
            em = discord.Embed(name=f"Last deleted message in #{channel.name}",
                               description=snipe_message_content[channel.id],color = 0xf7600f)
            em.set_footer(text=f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed=em)
        except:  # This piece of code is run if the bot doesn't find anything in the dictionary
            await ctx.send(f"There are no recently deleted messages in #{channel.name}")


def setup(bot):
    bot.add_cog(snipe(bot))