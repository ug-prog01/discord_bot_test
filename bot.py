import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is operational')

client.run('Njk5Nzg4NDk3Mzk2OTU3Mjc1.XpZe-Q.7gHHwFgRsTw2Ms8LVC6O6NhYno0')