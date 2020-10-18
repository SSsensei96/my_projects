import random

from discord.ext import commands
from pornhub_api import PornhubApi
import asyncio


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
    async def roll(self, ctx, _1d20):
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
    async def choose(self, ctx, words):
        try:
            user_message_to_choose = ctx.message.content[7::]
            words = user_message_to_choose.split()
            res = random.choice(words)
            await ctx.send(f'{res}')
        except:
            await ctx.send('None')

    @commands.command(pass_context=True)
    async def choke(self, ctx, member):
        random_num = random.randint(1, 20)
        user_name = ctx.message.content[6::]
        if random_num >= 17:
            await ctx.send(f"{ctx.message.author} chokes {member}")
        else:
            await ctx.send(f"{ctx.message.author} cant choke {member}")

    @commands.command(aliases=['ilyas'])
    async def Ilyas(self, ctx):
        responses = ["Affable", "Agreeable",
                     "Amiable",
                     "Charming",
                     "Polite",
                     "Likeable",
                     "Gregarious", "Considerate",
                     "Sympathetic", "Understanding",
                     "Diplomatic ", "Impartial ",
                     "Sincere ", "Straight-forward",
                     "Generous ", "Helpful ", "Giving ",
                      "Observant ",
                     "Quick-witted", "Patient ",
                     "Dynamic ", "Self-disciplined",
                     "Resourceful ", "Proactive ",
                     "Diligent ",
                     "Versatile ", "Intuitive ", "Adaptable ", "Dependable ",
                     "Reliable "]
        await ctx.send(f'{random.choice(responses)}')


def setup(client):
    client.add_cog(FunCommands(client))
