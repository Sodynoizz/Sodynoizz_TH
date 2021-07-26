import discord
from discord.ext import commands
from discord.ext.commands import Cog
class Helping(Cog):
    def __init__(self,bot):
        self.bot = bot
        self.cancelled = False

    @Cog.listener()
    async def on_ready(self):
        print('Bot Help is ready')

    @commands.group()
    async def help(self,ctx):
        em = discord.Embed(title=".:. 📌 🧩  `Welcome to My Help Menu`  🧩📌 .:.",
                           description="Use `%help` followed by a command name to get more additional information on a command. For example: `%help sodynoizz`.",
                           color=0x9b05ff)
        em.add_field(name="⚙️ : Moderation(10)",
                     value="`ban`,`unban`,`kick`,`tempban`,`createchannel`,`createrole`,`deleterole`,`giverole`,`moverole`,`warn`")
        em.add_field(name="😄 : Fun(12)",
                     value="`coinflip`,`dice`,`gif`,`image`,`kill`,`meme`,`rps`,`slots`,`sodynoizz`,`tictactoe`,`place`,`wanted`")
        em.add_field(name=":scroll: : General(18)",
                     value="`animal`,`ask`,`calculator`,`covid`,`define`,`dm`,`echo`,`eightball`,`emoji`,`hello`,`nsfw`,`quote`,`remind`,`status`,`translate`,`weather`,`whois`,`wikipedia`")
        em.add_field(name="👑 : Admin(10)",
                     value="`changenickname`,`changeprefix`,`clear`,`color`,`load`,`reload`,`snipe`,`unload`,`invite`,`invitebot`")
        em.add_field(name=":cyclone: : Info(6)", value="`avatar`,`help`,`level`,`members`,`ping`")
        em.add_field(name="🎵 : Music(9)",
                     value="`join`,`leave`,`loop`,`nowplaying`,`pause`,`play`,`queue`,`remove`,`resume`")
        em.add_field(name="📈 : Economy(6)", value="`balance`,`beg`,`deposit`,`give`,`rob`,`withdraw`")
        await ctx.send(embed=em)


    @help.command(aliases=["Moderation"])
    async def moderation(self,ctx):
        em = discord.Embed(title="⚙️ : Moderation ",
                           descripion="`ban`,`unban`,`kick`,`tempban`,`createchannel`,`createrole`,`deleterole`,`giverole`,`moverole`",
                           color=0xff6600)
        em.add_field(name="**Moderation Categories**", value="Example : `%help ban`,`%help unban`,`%help tempban`",
                     inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def ban(self,ctx):
        em = discord.Embed(title="Ban", description="Ban a member from the guild || แบนสมาชิกในดิสคอร์ด",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%ban <member> [reason]")
        await ctx.send(embed=em)

    @help.command()
    async def unban(self,ctx):
        em = discord.Embed(title="Unban", description="Unban a member from the guild || ปลดแบนสมาชิกในดิสคอร์ด",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%unban <member id>")
        await ctx.send(embed=em)

    @help.command()
    async def kick(self,ctx):
        em = discord.Embed(title="Kick", description="Kick a member from the guild || เตะสมาชิกในดิสคอร์ด",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%kick <member> [reason]")
        await ctx.send(embed=em)

    @help.command()
    async def tempban(self,ctx):
        em = discord.Embed(title="Tempban",
                           description="Ban a member from the guild for time || แบนสมาชิกในดิสคอร์ดเป็นระยะเวลา..",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%tempban <member> [duration]")
        await ctx.send(embed=em)

    @help.command()
    async def createchannel(self,ctx):
        em = discord.Embed(title="Tempban",
                           description="Create a channel on your server || สร้างช่องสำหรับ text channel",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%createchannel <channel name>")
        await ctx.send(embed=em)

    @help.command()
    async def createrole(self,ctx):
        em = discord.Embed(title="Createrole", description="Create a role in your server || สร้างยศในดิสคอร์ดคุณ",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%createrole <role name>")
        await ctx.send(embed=em)

    @help.command()
    async def deleterole(self,ctx):
        em = discord.Embed(title="Deleterole", description="Delete a role in your server || ลบยศในดิสคอร์ดคุณ",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%deleterole <role id>")
        await ctx.send(embed=em)

    @help.command()
    async def giverole(self,ctx):
        em = discord.Embed(title="Giverole", description="Give a role to someone || มอบยศให้ member", color=0xff6600)
        em.add_field(name="**Syntax**", value="%deleterole <role id>")
        await ctx.send(embed=em)

    @help.command()
    async def moverole(self,ctx):
        em = discord.Embed(title="Moverole", description="Order your role || เรียงลำดับความสำคัญของยศในดิสคอร์ดคุณ",
                           color=0xff6600)
        em.add_field(name="**Syntax**", value="%deleterole <role id>")
        await ctx.send(embed=em)

    @help.command(aliases=["fun"])
    async def Fun(self,ctx):
        em = discord.Embed(title="😄 : Fun",
                           descripion="`coinflip`,`dice`,`gif`,`image`,`kill`,`meme`,`rps`,`slots`,`sodynoizz`,`tictactoe`,`wanted`",
                           color=0x03fcf0)
        em.add_field(name="**Fun Categories**", value="Example : `%help coinflip`,`%help dice`,`%help gif`",
                     inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def coinflip(self,ctx):
        em = discord.Embed(title="Coinflip", description="Head or Tails? || เสี่ยงทายว่าหัวหรือก้อย", color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%coinflip <heads or tails?> [amount]")
        await ctx.send(embed=em)

    @help.command()
    async def dice(self,ctx):
        em = discord.Embed(title="Dice", description="Dice 1-6  || เสี่ยงทายว่าลูกเต๋า", color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%dice <1-6>")
        await ctx.send(embed=em)

    @help.command()
    async def gif(self,ctx):
        em = discord.Embed(title="GIF", description="GIF COMMAND || สุ่ม gif", color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%gif")
        await ctx.send(embed=em)

    @help.command()
    async def image(self,ctx):
        em = discord.Embed(title="Image", description="Image command || หารูปภาพที่ต้องการ", color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%image <picture do you want>")
        await ctx.send(embed=em)

    @help.command()
    async def kill(self,ctx):
        em = discord.Embed(title="Kill", description="Kill command like minecraft|| ฆ่า @mention", color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%kill <member>")
        await ctx.send(embed=em)

    @help.command()
    async def meme(self,ctx):
        em = discord.Embed(title="Meme", description="Random meme command|| สุ่มมีม", color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%meme")
        await ctx.send(embed=em)

    @help.command()
    async def rps(self,ctx):
        em = discord.Embed(title="Rock Paper Scissors", description="Rock Paper Scissors|| ค้อน กรรไกร กระดาษ",
                           color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%rps <rock paper scissors> [amount]")
        await ctx.send(embed=em)

    @help.command()
    async def slots(self,ctx):
        em = discord.Embed(title="Slots", description="Slot machine || สลอต แมชชีน", color=0x03fcf0)
        em.add_field(name="**Syntax**", value="%slots <bet>")
        await ctx.send(embed=em)

    @help.command()
    async def sodynoizz(self,ctx):
        em = discord.Embed(title="Sodynoizz", description="Handsome command || หล่อเท่", color=0x03fcf0)
        em.add_field(name='**Syntax**', value="%sodynoizz")
        await ctx.send(embed=em)

    @help.command()
    async def tictactoe(self,ctx):
        em = discord.Embed(title="Tictactoe", description="OX game || เกม OX", color=0x03fcf0)
        em.add_field(name='**Syntax**', value="%tictactoe <@member1> <@member2>")
        await ctx.send(embed=em)

    @help.command()
    async def wanted(self,ctx):
        em = discord.Embed(title="Wanted", description="Wanted meme || Wanted มีม", color=0x03fcf0)
        em.add_field(name='**Syntax**', value="%wanted <@member>")
        await ctx.send(embed=em)

    @help.command(aliases=["General"])
    async def general(self,ctx):
        em = discord.Embed(title=":scroll: : General",
                           descripion="`ask`,`calculator`,`covid`,`define`,`dm`,`echo`,`eightball`,`emoji`,`hello`,`nsfw`,`place`,`remind`,`status`,`translate`,`weather`,`whois`,`wikipedia`",
                           color=0x4432a8)
        em.add_field(name="**General Categories**", value="Example : `%help OwO`,`%help ask`,`%help calculator`",
                     inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def echo(self,ctx):
        em = discord.Embed(title="Echo", description="Repeat command || คำสั่งซ้ำคำที่พิมพ์", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%echo <message>")
        await ctx.send(embed=em)

    @help.command()
    async def animal(self,ctx):
        em = discord.Embed(title="Animal", description="Animal Search || ค้นหารูปสัตว์")
        em.add_field(name="**Animal Available**", value="dog,cat,panda,fox,bird,koala")
        em.add_field(name="**Syntax**", value="%animal <animal>")
        await ctx.send(embed=em)

    @help.command()
    async def ask(self,ctx):
        em = discord.Embed(title="Ask", description="Ask what do you want  || ถามสิ่งที่มีสาระด้วย wolfram alpha",
                           color=0x4432a8)
        em.add_field(name='**Syntax**', value="%OwO")
        await ctx.send(embed=em)

    @help.command()
    async def calculator(self,ctx):
        em = discord.Embed(title="Calculator", description="Calculator command || เครื่องคิดเลข", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%calculator")
        await ctx.send(embed=em)

    @help.command()
    async def covid(self,ctx):
        em = discord.Embed(title="Covid", description="Covid report || รายงานผู้ติดเชื้อโควิด-19", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%calculator")
        await ctx.send(embed=em)

    @help.command()
    async def define(self,ctx):
        em = discord.Embed(title="Define", description="Define Command || หานิยามต่างๆ", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%calculator")
        await ctx.send(embed=em)

    @help.command()
    async def dm(self,ctx):
        em = discord.Embed(title="Direct Message", description="Direct message Command || พูดคุยส่วนตัว",
                           color=0x4432a8)
        em.add_field(name='**Syntax**', value="%calculator")
        await ctx.send(embed=em)

    @help.command()
    async def eightball(self,ctx):
        em = discord.Embed(title="Eightball", description="Eightball command || คำสั่ง 8 ball", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%calculator")
        await ctx.send(embed=em)

    @help.command()
    async def emoji(self,ctx):
        em = discord.Embed(title="Emoji", description="Emojify command || สร้างลูกเล่น emoji", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%emoji <text>")
        await ctx.send(embed=em)

    @help.command()
    async def hello(self,ctx):
        em = discord.Embed(title="Hello", description="Hello command || คำสั่งทักทาย", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%emoji <text>")
        await ctx.send(embed=em)

    @help.command()
    async def nsfw(self,ctx):
        em = discord.Embed(title="Nsfw", description="Nsfw command || คำสั่ง NSFW", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%nsfw")
        await ctx.send(embed=em)

    @help.command()
    async def place(self,ctx):
        em = discord.Embed(title="Place", description="Place OX on the tictactoe board || คำสั่งวาง OX บนตำแหน่งต่างๆ",
                           color=0x4432a8)
        em.add_field(name='**Syntax**', value="%place <position 1-9>")
        await ctx.send(embed=em)

    @help.command()
    async def whois(self,ctx):
        em = discord.Embed(title="Whois", description="Whois Command || เช็คสเตตัสเพื่อนหรือตัวเอง", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%whois <@member>")
        await ctx.send(embed=em)

    @help.command()
    async def quote(self,ctx):
        em = discord.Embed(title="Quote", description="Quote command || คำคมข่มกิเลศ ตัณหา")
        em.add_field(name="**Syntax**", value="%quote")

    @help.command()
    async def remind(self,ctx):
        em = discord.Embed(title="Remind", description="Remind Command || คำสั่งเตือนให้ทำกิจกรรมต่างๆ", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%remind <amount> <unit> [activity]")
        await ctx.send(embed=em)

    @help.command()
    async def weather(self,ctx):
        em = discord.Embed(title="Weather", description="Weather Command || สเตตัสเซิร์ฟเวอร์", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%weather <country>")
        await ctx.send(embed=em)

    @help.command()
    async def translate(self,ctx):
        em = discord.Embed(title="Translate", description="Translate Command || แปลภาษา", color=0x4432a8)
        em.add_field(name='**Syntax**', value="%translate <language> [text]")
        await ctx.send(embed=em)

    @help.command()
    async def wikipedia(self,ctx):
        em = discord.Embed(title="Wikipedia", description="Wikipedia Command || เซิร์ชหาข้อมูลด้วยวิกีพีเดีย",
                           color=0x4432a8)
        em.add_field(name='**Syntax**', value="%wikipedia <information>")
        await ctx.send(embed=em)

    @help.command(aliases=["Admin"])
    async def admin(self,ctx):
        em = discord.Embed(title="👑 : Admin",
                           descripion="`changenickname`,`changeprefix`,`clear`,`color`,`load`,`reactrole`,`reload`,`snipe`,`unload`,`invite`,`invitebot`",
                           color=0xfa3737)
        em.add_field(name="**General Categories**",
                     value="Example : `%help changenickname`,`%help changeprefix`,`%help clear`", inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def changenickname(self,ctx):
        em = discord.Embed(title="Change nickname",
                           description="Change nickname @member || เปลี่ยนชื่อเล่นสมาชิกในดิสคอร์ด", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%changenickname <@member> [newname]")
        await ctx.send(embed=em)

    @help.command()
    async def changeprefix(self,ctx):
        em = discord.Embed(title="Change prefix", description="Change Prefix server || เปลี่ยน prefix ในเซิร์ฟเวอร์",
                           color=0xfa3737)
        em.add_field(name="**Syntax**", value="%changeprefix <new prefix>")
        await ctx.send(embed=em)

    @help.command()
    async def clear(self,ctx):
        em = discord.Embed(title="Clear", description="Clear message || ลบข้อความ", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%clear <amount>")
        await ctx.send(embed=em)

    @help.command()
    async def color(self,ctx):
        em = discord.Embed(title="Color", description="Check Hex Color code || ตรวจสอบสี Hex Color", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%color <hex color code>")
        await ctx.send(embed=em)

    @help.command()
    async def load(self,ctx):
        em = discord.Embed(title="Load", description="Load cogs file || โหลด COGS", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%load")
        await ctx.send(embed=em)

    @help.command()
    async def reactrole(self,ctx):
        em = discord.Embed(title="Reactrole", description="Reactrole to recieve role || กดอีโมจิเพื่อรับยศ",
                           color=0xfa3737)
        em.add_field(name="**Syntax**", value="%reactrole <emoji> [rolename]")
        await ctx.send(embed=em)

    @help.command()
    async def reload(self,ctx):
        em = discord.Embed(title="Reload", description="Reload cogs || รีโหลด COGS", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%reload")
        await ctx.send(embed=em)

    @help.command()
    async def snipe(self,ctx):
        em = discord.Embed(title="Snipe", description="Snipe Message || ดูข้อความที่เคยลบ", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%snipe")
        await ctx.send(embed=em)

    @help.command()
    async def unload(self,ctx):
        em = discord.Embed(title="Unload", description="Unload cogs || ยกเลิกการโหลด cogs", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%unload")
        await ctx.send(embed=em)

    @help.command()
    async def invite(self,ctx):
        em = discord.Embed(title="Invite", description="Invite to Taiyaki World || ลิงค์เชิญเข้าดิสไทยากิเวิร์ล",
                           color=0xfa3737)
        em.add_field(name="**Syntax**", value="%invite")
        await ctx.send(embed=em)

    @help.command()
    async def invitebot(self,ctx):
        em = discord.Embed(title="Invitebot", description="Invite Bot sodynoizzGG || ลิงค์เชิญบอท", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%invitebot")
        await ctx.send(embed=em)

    @help.command()
    async def warn(self,ctx):
        em = discord.Embed(title="Warn", description="Warn command || เตือนผู้กระทำไม่เหมาะสม", color=0xfa3737)
        em.add_field(name="**Syntax**", value="%warn <user> [reason]")
        await ctx.send(embed=em)

    @help.command()
    async def warnings(self,ctx):
        em = discord.Embed(title="Warnings", description="Check Warn command || ตรวจสอบว่ามีความผิดหรือไม่",
                           color=0xfa3737)
        em.add_field(name="**Syntax**", value="%warnings <user>")

    @help.command(aliases=["music"])
    async def Music(self,ctx):
        em = discord.Embed(title="🎵 : Music",
                           descripion="`join`,`leave`,`loop`,`nowplaying`,`pause`,`play`,`queue`,`remove`,`resume`",
                           color=0x37fae6)
        em.add_field(name="**General Categories**", value="Example : `%help join`,`%help leave`,`%help loop`",
                     inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def join(self,ctx):
        em = discord.Embed(title="Join", description="Join Music audio || ให้บอทฟังเพลงเข้ามาใน voice channel",
                           color=0x37fae6)
        em.add_field(name="**Syntax**", value="%join")
        await ctx.send(embed=em)

    @help.command()
    async def leave(self,ctx):
        em = discord.Embed(title="Leave", description="Leave Music audio || ให้บอทฟังเพลงออกจาก voice channel",
                           color=0x37fae6)
        em.add_field(name="**Syntax**", value="%leave")
        await ctx.send(embed=em)

    @help.command()
    async def loop(self,ctx):
        em = discord.Embed(title="Loop", description="Loop Music || วนซ้ำเพลง", color=0x37fae6)
        em.add_field(name="**Syntax**", value="%loop")
        await ctx.send(embed=em)

    @help.command()
    async def nowplaying(self,ctx):
        em = discord.Embed(title="Now playing", description="Now playing song || แสดงเพลงที่เล่นขณะนี้", color=0x37fae6)
        em.add_field(name="**Syntax**", value="%loop")
        await ctx.send(embed=em)

    @help.command()
    async def pause(self,ctx):
        em = discord.Embed(title="Pause", description="Pause the song || หยุดเพลง", color=0x37fae6)
        em.add_field(name="**Syntax**", value="%loop")
        await ctx.send(embed=em)

    @help.command()
    async def play(self,ctx):
        em = discord.Embed(title="Play", description="Play the song || เล่นเพลง", color=0x37fae6)
        em.add_field(name="**Syntax**", value="%play <song>")
        await ctx.send(embed=em)

    @help.command()
    async def queue(self,ctx):
        em = discord.Embed(title="Queue", description="Check queue || เช็คคิวเพลง", color=0x37fae6)
        em.add_field(name="**Syntax**", value="%queue")
        await ctx.send(embed=em)

    @help.command()
    async def remove(self,ctx):
        em = discord.Embed(title="Remove", description="Remove song || ลบคิวเพลง", color=0x37fae6)
        em.add_field(name="**Syntax**", value="%remove <numer queue song>")
        await ctx.send(embed=em)

    @help.command()
    async def resume(self,ctx):
        em = discord.Embed(title="Resume", description="Resume song || เล่นเพลงต่อ", color=0x37fae6)
        em.add_field(name="**Syntax**", value="%resume")
        await ctx.send(embed=em)

    @help.command(aliases=["Economy"])
    async def economy(self,ctx):
        em = discord.Embed(title="📈 : Economy", description="`balance`,`beg`,`deposit`,`give`,`rob`,`withdraw`",
                           color=0x28c732)
        em.add_field(name="**Economy Categories**", value="Example : `%help balance`,`%help beg`,`%help deposit`",
                     inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def balance(self,ctx):
        em = discord.Embed(title="Balance", description="Check your money || เช็คเงินของคุณ", color=0x28c732)
        em.add_field(name="**Syntax**", value="%balance")
        await ctx.send(embed=em)

    @help.command()
    async def beg(self,ctx):
        em = discord.Embed(title="Beg", description="Beg money || เพิ่งเงินในบัญชีคุณ", color=0x28c732)
        em.add_field(name="**Syntax**", value="%beg")
        await ctx.send(embed=em)

    @help.command()
    async def deposit(self,ctx):
        em = discord.Embed(title="Deposit", description="Deposit money || นำเงินเข้าธนาคาร", color=0x28c732)
        em.add_field(name="**Syntax**", value="%dep <amount or all>")
        await ctx.send(embed=em)

    @help.command()
    async def give(self,ctx):
        em = discord.Embed(title="Give", description="Give money || ให้เงินคนอื่น", color=0x28c732)
        em.add_field(name="**Syntax**", value="%give <@member> [amount]")
        await ctx.send(embed=em)

    @help.command()
    async def rob(self,ctx):
        em = discord.Embed(title="Rob", description="Rob money || ขโมยเงินคนอื่น", color=0x28c732)
        em.add_field(name="**Syntax**", value="%rob <@member>")
        await ctx.send(embed=em)

    @help.command()
    async def withdraw(self,ctx):
        em = discord.Embed(title="Withdraw", description="Withdraw money || ถอนเงินจากธนาคาร", color=0x28c732)
        em.add_field(name="**Syntax**", value="%withdraw <amount or all>")
        await ctx.send(embed=em)

    @help.command()
    async def info(self,ctx):
        em = discord.Embed(title=":cyclone: : Info", description="`avatar`,`help`,`level`,`ping`", color=0x28c732)
        em.add_field(name="**Info Categories**", value="Example : `%help avatar`,`%help level`,`%help help`",
                     inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def avatar(self,ctx):
        em = discord.Embed(title="Avatar", description="Show avatar member || แสดงรูปโปรไฟล์สมาชิกในดิสคอร์ด",
                           color=0xff36b8)
        em.add_field(name="**Syntax**", value="%avatar <@member> , %avatar", inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def level(self,ctx):
        em = discord.Embed(title="Level", description="Level member || เช็คเลเวลสมาชิกในดิสคอร์ด", color=0xff36b8)
        em.add_field(name="**Syntax**", value="%level <@member> , %level", inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def ping(self,ctx):
        em = discord.Embed(title="Ping", description="Check Latency || เช็คความเสถียรของอินเทอร์เน็ต", color=0xff36b8)
        em.add_field(name="**Syntax**", value="%ping", inline=True)
        await ctx.send(embed=em)

    @help.command()
    async def members(self,ctx):
        em = discord.Embed(title="Members", description="Display member on your servers || แสดงจำนวนคนในเซิร์ฟเวอร์",
                           color=0xff36b8)
        em.add_field(name="**Syntax**", value="%members", inline=True)
        await ctx.send(embed=em)
    @help.command()
    async def helping(self,ctx):
        em = discord.Embed(title="Help", description="Display help commands||คำสั่งช่วยเหลือ",
                           color=0xff36b8)
        em.add_field(name="**Syntax**", value="%help", inline=True)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Helping(bot))