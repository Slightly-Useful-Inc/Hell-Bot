import discord
from discord.ext import tasks, commands
import random
import time

client = commands.Bot(command_prefix='*')
TOKEN = ''

@client.event
async def on_ready():
    print('On')

@client.command()
async def spam(ctx):
     x = True
     while x:
        await ctx.send('Welcome To Hell')
        time.sleep(5)


client.run(TOKEN)