import discord
from discord.ext import commands
from discord.ext.commands import Cog
import DiscordUtils
import os
music = DiscordUtils.Music()
queues = {}
class Music(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = True

    @commands.command()
    async def join(self,ctx):
        voicetrue = ctx.author.voice
        if voicetrue is None:
            embed1 = discord.Embed(title='You are not connect to the voice channel', color=0xf00c0c)
            return await ctx.send(embed=embed1)
        elif voicetrue is True:
            embed2 = discord.Embed(title='Already connected to a voice channel', color=0x0cd9f0)
            return await ctx.send(embed=embed2)
        await ctx.author.voice.channel.connect()
        msg = 'Joined your voice channel'
        em = discord.Embed(title="Joined the channel", color=0x0aadbf)
        await ctx.send(embed=em)

    @commands.command()
    async def leave(self,ctx):
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        if voicetrue is None:
            embed = discord.Embed(title='You are not connect to the voice channel', color=0xf00c0c)
            return await ctx.send(embed=embed)
        if mevoicetrue is None:
            embed = discord.Embed(title='You are not connect to the voice channel', color=0xf00c0c)
            return await ctx.send(embed=embed)
        await ctx.voice_client.disconnect()
        em = discord.Embed(title="Left the channel", color=0xff0505)
        await ctx.send(embed=em)

    @commands.command()
    async def play(self,ctx, *, url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            embed1 = discord.Embed(title=f'I have already playing {song.name}', color=0x0cd9f0)
            await ctx.send(embed=embed1)
        else:
            song = await player.queue(url, search=True)
            embed1 = discord.Embed(title=f'{song.name} has been added to playlist', color=0x41f00c)
            await ctx.send(embed=embed1)

    @commands.command()
    async def queue(self,ctx):
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is False:
            os.mkdir("Queue")
        DIR = os.path.abspath(os.path.realpath("Queue"))
        q_num = len(os.listdir(DIR))
        player = music.get_player(guild_id=ctx.guild.id)
        newline = '\n'
        add_queue = True
        q_num += 1
        sodynoizz = "**"
        while add_queue:
            if q_num in queues:
                q_num += 1
            else:
                add_queue = False
                queues[q_num] = q_num
        embed = discord.Embed(title=f"{f'{newline}:sound:'.join([song.name for song in player.current_queue()])}",
                              color=0x82da55)
        await ctx.send(embed=embed)

    @commands.command()
    async def pause(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        embed = discord.Embed(title=f'Paused {song.name}', color=0xf70000)
        await ctx.send(embed=embed)

    @commands.command()
    async def resume(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        embed = discord.Embed(title=f'Resumed {song.name}', color=0xf70000)
        await ctx.send(embed=embed)

    @commands.command()
    async def loop(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            embed = discord.Embed(title=f"{song.name} is looping!", color=0xf7a500)
            return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"{song.name} isn't looping!", color=0xf7a500)
            return await ctx.send(embed=embed)

    @commands.command()
    async def nowplaying(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = player.now_playing()
        embed = discord.Embed(title=f"Now playing {song.name} ", color=0x00f7de)
        await ctx.send(embed=embed)

    @commands.command()
    async def remove(self,ctx, index):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        embed = discord.Embed(title=f"'Removed {song.name} from the queue'", color=0xf70000)
        await ctx.send(embed=embed)

    @Cog.listener()
    async def on_ready(self):
        print('Bot Music is ready')

def setup(bot):
    bot.add_cog(Music(bot))