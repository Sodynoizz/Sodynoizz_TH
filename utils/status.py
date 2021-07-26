import discord
import random
LISTENING = ['to music']
PLAYING = ['with sodynoizz']
WATCHING = ['sodynoizz']
STREAMING = ['sodynoizz_TH']
ACTIVITYTYPE = {'LISTENING': discord.ActivityType.listening,
                'PLAYING': discord.ActivityType.playing,
                'WATCHING': discord.ActivityType.watching,
                'STREAMING': discord.ActivityType.streaming}
PRESENCELISTS = ['LISTENING', 'PLAYING', 'WATCHING', 'STREAMING']
PRESENCE = random.choice(PRESENCELISTS)