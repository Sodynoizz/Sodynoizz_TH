from discord.ext.commands import Cog
from discord.ext.commands import command
import random
class eightball(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cancelled = False
    @Cog.listener()
    async def on_ready(self):
        print('Bot Eightball is ready')
    @command(aliases=['8ball', '8b'], brief="eightball Q&A")
    async def eightball(self,ctx, *, question):
            responses = [
                'Hell no.',
                'Prolly not.',
                'Idk bro.',
                'Prolly.',
                'Hell yeah my dude.',
                'It is certain.',
                'It is decidedly so.',
                'Without a Doubt.',
                'Yes - Definitaly.',
                'You may rely on it.',
                'As i see it, Yes.',
                'Most Likely.'
                ''
                '',
                'Outlook Good.',
                'Yes!',
                'No!',
                'IDK but you must follow my facebook Chorasit Apilardmongkol',
                'Signs a point to Yes!',
                'Reply Hazy, Try again.',
                'Better not tell you know.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't Count on it.",
                'My reply is No.',
                'My sources say No.',
                'Outlook not so good.',
                'Very Doubtful']
            await ctx.send(f':8ball: Question : {question}\n:8ball: Answer: {random.choice(responses)}')

def setup(bot):
    bot.add_cog(eightball(bot))