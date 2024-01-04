import bot
import client
import responses


if __name__ == '__main__':
    TOKEN = 'MTE1MjI1NTI2MzQyOTExMTg4OQ.G4tUZx.gmZERnvvuvTpYJMzPfRZ0ydboR7LuxKik2FDAw'  # Replace with your bot token
    
    # Assuming bot and client are instances of commands.Bot and discord.Client respectively
    bot.bot.run(TOKEN)
    client.client.run(TOKEN)
