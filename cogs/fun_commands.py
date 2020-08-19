import random

from discord.ext import commands


class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Natalie is online")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx):
        responses = ["As I see it", "yes.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don’t count on it.",
                     "It is certain.",
                     "It is decidedly so.",
                     "Most likely.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Outlook good.",
                     "Reply hazy, try again.",
                     "Signs point to yes.",
                     "Very doubtful.",
                     "Without a doubt.",
                     "Yes.",
                     "Yes – definitely.",
                     "You may rely on it.", ]

        await ctx.send(f'{random.choice(responses)}')

    @commands.command()
    async def roll(self, ctx):
        try:
            user_roll_to_message = ctx.message.content[6::]

            numbers = user_roll_to_message.split('d')

            sec_number_plus = numbers[1].split('+')

            if '+' in user_roll_to_message:
                res = random.randint(int(numbers[0]), int(sec_number_plus[0])) + int(sec_number_plus[1])
                await ctx.send(f'{res}')
            else:
                res = random.randint(int(numbers[0]), int(sec_number_plus[0]))
                await ctx.send(f'{res}')
        except:
            await ctx.send('None')

    @commands.command()
    async def choose(self, ctx):
        try:
            user_message_to_choose = ctx.message.content[7::]
            words = user_message_to_choose.split()
            res = random.choice(words)
            await ctx.send(f'{res}')
        except:
            await ctx.send('None')


def setup(client):
    client.add_cog(FunCommands(client))
