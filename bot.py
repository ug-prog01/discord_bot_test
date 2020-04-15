import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is operational')

client.run(os.environ["ACCESS_TOKEN"])
