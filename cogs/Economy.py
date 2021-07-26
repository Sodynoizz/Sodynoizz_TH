import discord
from discord.ext import commands
from discord.ext.commands import Cog
import json
from utils.economysys import open_account,get_bank_data,update_bank
import random
class Economy(Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['bal'], brief="Check your balance money")
    async def balance(self,ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        await open_account(member)

        users = await get_bank_data()
        user = member
        wallet_amount = users[str(user.id)]["wallet"]
        bank_amount = users[str(user.id)]["bank"]
        embed = discord.Embed(title=f"{member.name}'s Balance", color=discord.Color.red())
        embed.add_field(name="Wallet", value=wallet_amount)
        embed.add_field(name="Bank", value=bank_amount)
        await ctx.send(embed=embed)

    @commands.command(brief="Beg for a money")
    @commands.cooldown(5, 30, commands.cooldowns.BucketType.user)
    async def beg(self,ctx):
        await open_account(ctx.author)
        users = await get_bank_data()
        user = ctx.author
        earnings = random.randrange(1001)

        await ctx.send(f"Congractulation!! Someone gave you {earnings} coins!")

        users[str(user.id)]["wallet"] += earnings
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    @commands.command(aliases=['with'], brief="Withdraw your money")
    async def withdraw(self,ctx, amount=None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send('Please enter amount you would like to withdraw')
            return
        bal = await update_bank(ctx.author)

        if amount == "all":
            amount = bal[1]
        elif amount == "max":
            amount = bal[1]

        amount = int(amount)
        if amount < 0:
            await ctx.send("Amount must be larger than 0")
            return
        if amount > bal[1]:
            await ctx.send("You do not have enough money")

        await update_bank(ctx.author, amount, "wallet")
        await update_bank(ctx.author, -1 * amount, "bank")

        await ctx.send(f"You withdrew {amount} coins")

    @commands.command(aliases=['dep'], brief="Deposit your money")
    async def deposit(self,ctx, amount=None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send('Please enter amount you would like to deposit')
            return
        bal = await update_bank(ctx.author)

        if amount == "all":
            amount = bal[0]
        elif amount == "max":
            amount = bal[0]

        amount = int(amount)
        if amount < 0:
            await ctx.send("Amount must be larger than 0")
            return
        if amount > bal[0]:
            await ctx.send("You do not have enough money")

        await update_bank(ctx.author, -1 * amount, "wallet")
        await update_bank(ctx.author, amount, "bank")

        await ctx.send(f"You deposited {amount} coins")

    @commands.command(aliases=['send'], brief="Give your money to your @mention")
    async def give(self,ctx, member: discord.Member, amount=None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send('Please enter amount you would like to give')
            return
        bal = await update_bank(ctx.author)
        if amount == "all":
            amount = bal[0]
        elif amount == "max":
            amount = bal[0]
        amount = int(amount)
        if amount < 0:
            await ctx.send("Amount must be larger than 0")
            return
        if amount > bal[0]:
            await ctx.send("You do not have enough money")

        await update_bank(ctx.author, -1 * amount, "wallet")
        await update_bank(member, amount, "wallet")

        await ctx.send(f"You gave ***{member} ***{amount} coins")

    @commands.command(brief="Rob @mention user")
    async def rob(self,ctx, member: discord.Member = None):
        if member == None:
            return await ctx.send('Who will you rob!')
        await open_account(ctx.author)
        await open_account(member)

        bal = await update_bank(member)
        robberBal = await update_bank(ctx.author)
        if robberBal[0] < 250:
            return await ctx.send('You need at least 250 coins to rob!')
        else:
            if bal[0] < 250:
                return await ctx.send('They do not even have 250 coins!')

        stolen = random.randrange(-1 * (robberBal[0]), bal[0])

        await update_bank(ctx.author, stolen)
        await update_bank(member, stolen)

        if stolen > 0:
            return await ctx.send(f'You stole {stolen} coins!')
        elif stolen < 0:
            stolen = stolen * -1
            return await ctx.send(f'You tried to steal but got caught then you paid {stolen} coins')

    @beg.error
    async def error(self,ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Sorry! Please try this command again in {:2f}s'.format(error.retry_after)
        await ctx.send(msg)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Economy is ready')
def setup(bot):
    bot.add_cog(Economy(bot))