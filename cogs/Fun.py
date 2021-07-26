from discord.ext import commands
from discord.ext.commands import Cog
from utils.economysys import open_account,update_bank
import random
from random import randint
from googleapiclient.discovery import build
import discord
from config.keys import api_key_giphy,api_instance
import aiohttp
from utils.tictactoe import *
from PIL import Image
from io import BytesIO
class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cancelled = False

    @commands.command(aliases=["flip", "coin"], brief="Flip coin activity to earn money")
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def coinflip(self,ctx, message, amount=None):
        await open_account(ctx.author)
        bal = await update_bank(ctx.author)

        amount = int(amount)

        if amount == None:
            return await ctx.send('Please enter an amount you would like to bet!')
        if amount < 100:
            return await ctx.send('You must bet at least 100 coins')
        else:
            if amount > bal[0]:
                return await ctx.send('You do not have this much money!')
            if amount < 0:
                return await ctx.send('Amount must be positive!')

        answer = message.lower()
        choices = ["heads", "tails"]
        computer_answer = random.choice(choices)
        if answer not in choices:
            await ctx.send("That is not a valid option! Please use one of these options : rock,paper,scissors")
        else:
            if computer_answer == "heads":
                if answer == "heads":
                    await update_bank(ctx.author, 2 * amount)
                    await ctx.send(
                        f"You win! You guessed {answer} !I fliped and coins became {computer_answer} So, You earned {2 * amount} ")
            elif computer_answer == "heads":
                if answer == "tails":
                    await update_bank(ctx.author, -1 * amount)
                    await ctx.send(
                        f"You lost! You guessed {answer} !I fliped and coins became {computer_answer} So, You lost {-1 * amount} ")
            elif computer_answer == "tails":
                if answer == "tails":
                    await update_bank(ctx.author, 2 * amount)
                    await ctx.send(
                        f"You win! You guessed {answer} !I fliped and coins became {computer_answer} So, You earned {2 * amount} ")
            elif computer_answer == "tails":
                if answer == "heads":
                    await update_bank(ctx.author, -1 * amount)
                    await ctx.send(
                        f"You lost! You guessed {answer} !I fliped and coins became {computer_answer} So, You lost {-1 * amount} ")

    @commands.command(helpinfo='Leave it to luck', aliases=['roll'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def dice(self,ctx, number=6):
        '''
        Picks a random int between 1 and number
        '''
        await ctx.send("You rolled a __**{}**__!".format(randint(1, number)))

    @commands.command(brief="GIF command")
    async def gif(self,ctx, *, q="random"):
        try:
            # Search Endpoint

            api_response = api_instance.gifs_search_get(api_key_giphy, q, limit=5, rating='g')
            lst = list(api_response.data)
            giff = random.choice(lst)

            emb = discord.Embed(title='Here is your gif', description='Your gif picture')
            emb.set_image(url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')

            await ctx.channel.send(embed=emb)
        except api_instance as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    @commands.command(aliases=['show'], brief="search image what you want with google")
    async def image(self,ctx, *, search):
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey='AIzaSyDS-PsjhyUt-Sgypn8muoa8DC3giGQEE7A').cse()
        result = resource.list(
            q=f"{search}", cx="115ee45d46b90cbab", searchType="image").execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"Here Your Image ({search.title()})")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)

    @commands.command(helpinfo='Be an assassin')
    async def kill(self,ctx, *, user='You'):
        '''
        Kills the player, minecraft style
        '''
        await ctx.channel.send((user) + ' fell out of the world')

    @commands.command(brief="Meme command")
    async def meme(self,ctx):
        async with aiohttp.ClientSession()as cs:
            async with cs.get("https://www.reddit.com/r/memes.json") as r:
                memes = await r.json()
                embed = discord.Embed(
                    color=discord.Colour.purple()
                )
                embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.set_footer(text=f"Powered by r/memes! | Meme requestes by {ctx.author}")
                await ctx.send(embed=embed)

    @commands.command(aliases=['rockpaperscissors'], brief="Play rock paper scissors")
    async def rps(self,ctx, message, amount=None):
        if amount == None:
            return await ctx.send('Please enter an amount you would like to bet!')
        await open_account(ctx.author)
        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount < 100:
            return await ctx.send('You must bet at least 100 coins')
        else:
            if amount > bal[0]:
                return await ctx.send('You do not havve this much money!')
            if amount < 0:
                return await ctx.send('Amount must be positive!')
            answer = message.lower()
            choices = ["rock", "paper", "scissors"]
            computer_answer = random.choice(choices)
            if answer not in choices:
                await ctx.send("That is not a valid option! Please use one of these options : rock,paper,scissors")
            else:
                if computer_answer == answer:
                    await update_bank(ctx.author, 0 * amount)
                    await ctx.send(f"Tie! We both picked {answer}! and You earned {0 * amount}")
                elif computer_answer == "rock":
                    if answer == "paper":
                        await update_bank(ctx.author, 3 * amount)
                        await ctx.send(
                            f"You win! I picked {computer_answer} ,You earned {3 * amount} and you picked {answer}!")
                    elif answer == "scissors":
                        await ctx.send(
                            f"You lost! I picked {computer_answer} ,You lost {-1 * amount} and you picked {answer}!")
                elif computer_answer == "paper":
                    if answer == "scissors":
                        await update_bank(ctx.author, 3 * amount)
                        await ctx.send(
                            f"You win! I picked {computer_answer} ,You earned {3 * amount} and you picked {answer}!")
                    elif answer == "rock":
                        await ctx.send(
                            f"You lost! I picked {computer_answer} ,You lost {-1 * amount} and you picked {answer}!")
                elif computer_answer == "scissors":
                    if answer == "rock":
                        await update_bank(ctx.author, 3 * amount)
                        await ctx.send(
                            f"You win! I picked {computer_answer} ,You earned {3 * amount} and you picked {answer}!")
                    elif answer == "paper":
                        await ctx.send(
                            f"You lost! I picked {computer_answer} ,You lost {-1 * amount} and you picked {answer}!")

    @commands.command(brief="Play slots to earn money")
    async def slots(self,ctx, amount=None):
        if amount == None:
            return await ctx.send('Please enter an amount you would like to bet!')

        await open_account(ctx.author)
        bal = await update_bank(ctx.author)

        amount = int(amount)

        if amount < 100:
            return await ctx.send('You must bet at least 100 coins')
        else:
            if amount > bal[0]:
                return await ctx.send('You do not havve this much money!')
            if amount < 0:
                return await ctx.send('Amount must be positive!')
        final = []
        for i in range(3):
            a = random.choice([':laughing:'':thumbsup:', ':white_check_mark:'])
            final.append(a)
        em = discord.Embed(title=f"{ctx.author.name}'s Slots Game")
        em.add_field(name="Your slots game", value=str(final))
        await ctx.send(embed=em)

        if final[0] == final[1] == final[2]:
            await update_bank(ctx.author, 3 * amount)
            await ctx.send('You won all 3 slots!!!')
        elif final[0] == final[1] or final[1] == final[2] or final[2] == final[0]:
            await update_bank(ctx.author, 2 * amount)
            await ctx.send('You won all 2 slots!!!')
        else:
            await update_bank(ctx.author, -1 * amount)
            await ctx.send('Sorry,You lost all slots!!!')

    @commands.command()
    async def sodynoizz(self,ctx):
        msg = discord.Embed(title="Sodynoizz", description="เหล่ท่อ = หล่อเท่", color=0xed09ad)
        await ctx.send(embed=msg)


    @commands.command(brief="Play tictactoe between @mention1 and @mention2")
    async def tictactoe(self,ctx, p1: discord.Member, p2: discord.Member):
        global count
        global player1
        global player2
        global turn
        global gameOver
        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            # print the board
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            # determine who goes first
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                myEmbed = discord.Embed(title="GAME IN PROGRESS",
                                        description="IT IS <@" + str(player1.id) + ">'s TURN.",
                                        color=0xe74c3c)
                await ctx.send(embed=myEmbed)
            elif num == 2:
                turn = player2
                myEmbed = discord.Embed(title="GAME IN PROGRESS",
                                        description="IT IS <@" + str(player2.id) + ">'s TURN.",
                                        color=0xe74c3c)
                await ctx.send(embed=myEmbed)
        else:
            myEmbed = discord.Embed(title="GAME IN PROGRESS",
                                    description="A GAME IS STILL IN PROGRESS. FINISH IT BEFORE STARTING A NEW ONE",
                                    color=0xe74c3c)
            await ctx.send(embed=myEmbed)

    @commands.command(brief="Place position on tictactoe board")
    async def place(self,ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver
        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1

                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]

                    checkWinner(winningConditions, mark)
                    print(count)
                    if gameOver == True:
                        myEmbed = discord.Embed(title="WINNER!", description=mark + " :crown: ", color=0xf1c40f)
                        await ctx.send(embed=myEmbed)
                    elif count >= 9:
                        gameOver = True
                        myEmbed = discord.Embed(title="TIE", description="IT'S A TIE :handshake:", color=0xf1c40f)
                        await ctx.send(embed=myEmbed)

                    # switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    myEmbed = discord.Embed(title="PLACE ERROR!",
                                            description="BE SURE TO CHOOSE AN INTEGER BETWEEN 1 AND 9 (INCLUSIVE) AND AN UNMARKED TILE. ",
                                            color=0xe74c3c)
                    await ctx.send(embed=myEmbed)
            else:
                myEmbed = discord.Embed(title="TURN ERROR!", description="IT'S NOT YOUR TURN", color=0xe74c3c)
                await ctx.send(embed=myEmbed)
        else:
            myEmbed = discord.Embed(title="START GAME", description="TO START A NEW GAME, USE -tictactoe COMMAND",
                                    color=0x2ecc71)
            await ctx.send(embed=myEmbed)

    @tictactoe.error
    async def tictactoe_error(ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            myEmbed = discord.Embed(title="MENTION ERROR!", description="PLEASE MENTION 2 USERS", color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif isinstance(error, commands.BadArgument):
            myEmbed = discord.Embed(title="ERROR!",
                                    description="PLEASE MAKE SURE TO MENTION/PING PLAYERS (ie. <@688534433879556134>)",
                                    color=0xe74c3c)
            await ctx.send(embed=myEmbed)

    @place.error
    async def place_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            myEmbed = discord.Embed(title="NO POSITION", description="PLEASE ENTER A POSITION TO MARK", color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif isinstance(error, commands.BadArgument):
            myEmbed = discord.Embed(title="INTEGER ERROR!", description="PLEASE MAKE SURE IT'S AN INTEGER",
                                    color=0xe74c3c)
            await ctx.send(embed=myEmbed)

    @commands.command()
    async def wanted(self,ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        wanted = Image.open("wanted.jpg")
        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((300, 300))

        wanted.paste(profilepic, (78, 219))
        wanted.save("wantedpic.jpg")

        await ctx.send(file=discord.File("wantedpic.jpg"))

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Fun is ready')

def setup(bot):
    bot.add_cog(Fun(bot))