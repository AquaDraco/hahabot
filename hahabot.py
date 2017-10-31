import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")

@client.event
async def on_message(message):
    if message.content == 'haha':
        await client.send_message(message.channel, 'me too thanks')
    await client.process_commands(message)

client.run("INSERT TOKEN HERE")
