import discord
from io import BytesIO
import requests
from discord.ext import commands
import responses
import random


intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

# Send message
async def send_message(message, user_message, is_private, image_url=None):
    try:
        response = responses.handle_response(user_message)
        if is_private:
            await message.author.send(responses)
        else:
            await message.channel.send(responses)
    except Exception as e:
        print(e)
    try:
        if image_url:
            response = responses.get_response(user_message)
            image_data = requests.get(image_url).content
            file = discord.File(BytesIO(image_data), filename="image.png")
            if response:
                if is_private:
                    await message.author.send(content=response, file=file)
                else:
                    await message.channel.send(content=response, file=file)
            else:
                print("Empty response from 'get_response'")
        else:
            response = responses.get_response(user_message)
            if response:
                if is_private:
                    await message.author.send(response)
                else:
                    await message.channel.send(response)
            else:
                print("Empty response from 'get_response'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



    
# Waifu
@bot.command()
async def waifu(ctx):
    # Define a function to get a random waifu image from the API
    def get_waifu_image():
        try:
            response = requests.get("https://api.waifu.im/search")
            if response.status_code == 200:
                data = response.json()
                if 'images' in data and data['images']:
                    first_image = data['images'][0]
                    if 'url' in first_image:
                        return first_image['url']
                    else:
                        print("No 'url' found in the waifu image response.")
                else:
                    print("No images found in the response.")
            else:
                print(f"Failed to fetch waifu image, HTTP status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching waifu image: {str(e)}")
        return None

    waifu_url = get_waifu_image()
    if waifu_url:
        await ctx.send(f"Here's your random waifu: {waifu_url}")
    else:
        await ctx.send("Sorry, I couldn't fetch a waifu image at the moment.")
#Random dog
@bot.command()
async def dog(ctx):
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['message'])
    await ctx.send(embed=em)

#Bot status
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Pleasing Her Master'))
    print(f'{bot.user} asks if you are her master!')

#Dotroy command
@bot.command()
async def dotroy(ctx):
    image_url = "https://cdn.discordapp.com/attachments/1064305767215288321/1162234112543838299/IMG_0218.png?ex=653b31dd&is=6528bcdd&hm=b96fde269321d2cb7d3a1788d2d3eb8558d0a6c39da280e39841899df1f05161&"
    user_message = ctx.message.content  
    await send_message(ctx.message, user_message, is_private=False, image_url=image_url)

@bot.command()
async def feftywacky(ctx):
    image_url = "https://media.discordapp.net/attachments/1062926223111635002/1151375310206545952/IMG_5471.png?ex=6541d551&is=652f6051&hm=04e4b600b23c0b047a4c8045067e17185fa735ae2f565c410e8f03137ea42c8e&=&width=280&height=606"
    user_message =ctx.message.content
    await send_message(ctx.message,user_message,is_private=False,image_url=image_url)


    

#bot.run('MTE1MjI1NTI2MzQyOTExMTg4OQ.G4tUZx.gmZERnvvuvTpYJMzPfRZ0ydboR7LuxKik2FDAw')