import discord
from discord.ext import commands
from discord.ext.commands import Cog
import json
from utils.levelsys import update_data,add_experience,level_up
class Level(Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(brief="Check your level")
    async def level(self,ctx, member: discord.Member = None):
        if not member:
            id = ctx.message.author.id
            with open('data/users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'You are at level > {lvl}!')
        else:
            id = member.id
            with open('data/users.json', 'r') as f:
                users = json.load(f)
            lvl = users[str(id)]['level']
            await ctx.send(f'{member.mention} is on **level > {lvl}**')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        with open('data/users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, member)

        with open('data/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Level is ready')

def setup(bot):
    bot.add_cog(Level(bot))
