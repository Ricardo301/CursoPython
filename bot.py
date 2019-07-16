import discord

TOKEN = 'NDY3ODEwNzUwNjg2Mjk4MTEy.XS0hrg.B9JJrIeUxSM3UFf1SBz-7F44CKM'
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Iae irmão!')
client.run(TOKEN)
