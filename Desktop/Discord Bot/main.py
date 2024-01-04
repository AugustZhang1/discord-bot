import asyncio
import bot
import client
import responses
import random

async def run_bot_and_client(token):
    tasks = [
        asyncio.create_task(bot.bot.start(token)),
        asyncio.create_task(client.client.start(token))
    ]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    TOKEN = 'MTE1MjI1NTI2MzQyOTExMTg4OQ.G4tUZx.gmZERnvvuvTpYJMzPfRZ0ydboR7LuxKik2FDAw'
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot_and_client(TOKEN))
