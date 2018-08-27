import discord
import asyncio
#Hellow
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ')
    print(client.user.name)
    print(client.user.id)
    print('-------')

@client.event
async def on_message(message):
    if message.contet.startswhith('!teste'):
        counter = 0
        tmp = await client.send_message(message.channel,'Hellow')