import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def random_emoji(ctx):
    emoji_list = ["😀","😁","😂","🤣","😎","🥱","🥳","🤓"]
    emoji_chosen = random.choice(emoji_list)
    await ctx.send(f"{emoji_chosen}")

@bot.command()
async def coin_toss(ctx):
    coin_side = random.randint(1,2)
    if coin_side == 1:
        await ctx.send(f"Монетка упала на орла!")
    elif coin_side == 2:
        await ctx.send(f"Монетка упала на режку!")

@bot.command()
async def animal(ctx):
    animal_choice = random.randint(1,2)
    if animal_choice == 1:
        image_url = get_dog_image_url()
        await ctx.send(image_url)
    elif animal_choice == 2:
        image_url = get_duck_image_url()
        await ctx.send(image_url)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

    '''IMAGE/FILE COMMANDS'''
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    '''API'''
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#TOKEN
bot.run()
