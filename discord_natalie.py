import os

from secret import token
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event
async def on_member_join(member):
    channel = client.get_channel(741241273268043816)
    await channel.send(f"{member} has joined the server")


@client.event
async def on_member_remove(member):
    channel = client.get_channel(741241273268043816)
    await channel.send(f"{member} has left the server")


@client.command()
async def load(extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
async def reload(extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
