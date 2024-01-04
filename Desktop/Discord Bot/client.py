import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

# Provide a command_prefix for the Bot instance
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('In Avalon'))
    print(f'{client.user} asks if you are her master!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hello':
        await message.channel.send('Sup')
    
    if message.content == 'roll':
        await message.channel.send(str(random.randint(1, 6)))

    if message.content == 'how are you doing today':
        await message.channel.send('Better now that you are here')

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print (f'{username} said:"{user_message}"({channel})' )



    



#client.run('MTE1MjI1NTI2MzQyOTExMTg4OQ.G4tUZx.gmZERnvvuvTpYJMzPfRZ0ydboR7LuxKik2FDAw') 