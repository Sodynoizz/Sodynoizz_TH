import discord
from discord.ext.commands import command,Cog
from discord.ext import commands
class invite(Cog):
    def __init__(self,bot):
        self.bot = bot
    @Cog.listener()
    async def on_ready(self):
        print("Bot Invite is ready")

    @command(brief="Creates an invite link to the channel")
    @commands.guild_only()
    async def invite(self,ctx):
        link = await ctx.channel.create_invite(max_age=604800)
        embed = discord.Embed(description="Invite Taiyaki World Link!!!!", colour=discord.Colour.dark_purple())
        embed.add_field(name="Here is your invite link", value=link, inline=False)
        embed.set_image(
        url="https://cdn.discordapp.com/attachments/848926587226685441/858981682065834034/Taiyaki_003.jpg")
        await ctx.send(embed=embed)

    @command()
    async def invitebot(self,ctx):
        em = discord.Embed(title="Invite SodynoizzGG",
                           description="https://discord.com/oauth2/authorize?client_id=849144696433016833&permissions=8&scope=bot",
                           color=0x0314fc)
        em.set_image(
            url="https://cdn.discordapp.com/avatars/849144696433016833/b7ec7174bfa19d24b4ae927c44ca7f6e.webp?size=1024")
        em.add_field(name="Here is a link for invite SodynoizzGG discord bot",
                     value="prefix `%` !![Can change into your own prefix]")
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(invite(bot))