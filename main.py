from discord.ext import commands
import discord.utils
from discord_components import *
import asyncio
import os
from utils.change_prefix import get_prefix
from utils import keep_alive
from utils.levelsys import *
from config import keys
from utils.status import *

client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')

@client.event
async def on_guild_join(guild):
    with open('data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'bl!'

    with open('data/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_ready():
    print(f"{client.user.name} is ready.")
    client.loop.create_task(status_task())


async def status_task():
    while True:
        await client.change_presence(activity=discord.Activity(
            type=ACTIVITYTYPE[PRESENCE], name=(random.choice(globals()[PRESENCE]) + ' | %help')))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(
            type=ACTIVITYTYPE[PRESENCE], name=(random.choice(globals()[PRESENCE]) + ' | %help')))
        await asyncio.sleep(10)

@client.event
async def on_guild_remove(guild):  # when the bot is removed from the guild
    with open('data/prefixes.json', 'r') as f:  # read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))  # find the guild.id that bot was removed from

    with open('data/prefixes.json', 'w') as f:  # deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)

@client.command()
async def on_message(self,message):
    if message.author.bot == False:
        with open('data/users.json', 'r') as f:
            users = json.load(f)

            await update_data(users, message.author)
            await add_experience(users, message.author, 5)
            await level_up(users, message.author, message)
            with open('data/users.json', 'w') as f:
                json.dump(users, f, indent=4)
        await self.bot.process_commands(message)

if __name__ == '__main__':
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()
client.run(keys.token)