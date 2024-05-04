import discord, random
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
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

bot.run()
