import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"

client.run("NDY3ODEwNzUwNjg2Mjk4MTEy.XS0gAA.ahTmz4W7i4voEn8vUxX76amIhms")
