import discord
import responses  
from discord import app_commands

from discord.ext import commands
import interactions
import bot






async def send_message(message,user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE1MjI1NTI2MzQyOTExMTg4OQ.G4tUZx.gmZERnvvuvTpYJMzPfRZ0ydboR7LuxKik2FDAw'
    intents = discord.Intents.default()
    intents.message_content=True
    client = discord.Client(intents=intents)



    @client.event
    async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Game('Pleasing Her Master'))
        print(f'{client.user} asks if you are her master!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        await send_message(message,user_message,is_private=False)
        channel = str(message.channel)



        print(f"{username} said: '{user_message}' ({channel})")


    """  # Check if user_message is empty or too short before accessing its first character
        if user_message.strip() and len(user_message) > 0:
            if user_message[0] == '?':
                user_message = user_message[1:]  # Exclude the question mark
                await send_message(message, user_message, is_private=True)  # You need to define send_message
            else:
                await send_message(message, user_message, is_private=False)  # You need to define send_message """
    
        
    client.run(TOKEN)


