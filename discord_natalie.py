import os

import discord

from secret import token
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_member_join(member):
    channel = client.get_channel(741241273268043816)
    await channel.send(f"{member} has joined a server")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(741241273268043816)
    await channel.send(f"{member} has left a server")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
