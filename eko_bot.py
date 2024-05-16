import discord, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    '''eko'''
eko_fact1 = "Глобальное потепление вызвано деятельностью человека, выбрасывающей парниковые газы, что приводит к устойчивому повышению средней температуры на Земле."
eko_fact2 = "Глобального потепления последствия включают повышение уровня моря, более экстремальные погодные явления, такие как волны тепла и штормы, а также нарушения экосистем и сельского хозяйства."
eko_fact3 = "Решение проблемы глобального потепления требует сокращения выбросов парниковых газов посредством устойчивых методов и перехода на возобновляемые источники энергии."

ice_glacier_fact1 = "Таяние ледников влияет на уровень мировых океанов, увеличивая его и угрожая прибрежным областям и экосистемам."
ice_glacier_fact2 = "Этот процесс ускоряется из-за выбросов парниковых газов, таких как углекислый газ, в атмосферу из-за человеческой деятельности."
ice_glacier_fact3 = "Таяние ледников происходит из-за глобального потепления, которое приводит к повышению средней температуры на Земле."

@bot.command()
async def eko_list(ctx):
    await ctx.send("Список команд, содержащих экологические аспекты:")
    await ctx.send("**$global_warming_facts**   ->   факты о глобальном потеплении")
    await ctx.send("**$ice_glaciers_melting**    ->   информация о таянии ледников")

@bot.command()
async def global_warming_facts(ctx):
    global_warming_fact_chosen = random.randint(1,3)
    if global_warming_fact_chosen == 1:
        await ctx.send(f"Вот вам факт о глобальном потеплении:\n{eko_fact1}")
    if global_warming_fact_chosen == 2:
        await ctx.send(f"Вот вам факт о глобальном потеплении:\n{eko_fact2}")
    if global_warming_fact_chosen == 3:
        await ctx.send(f"Вот вам факт о глобальном потеплении:\n{eko_fact3}")

@bot.command()
async def ice_glaciers_melting(ctx):
    ice_glaciers_fact_chosen = random.randint(1,3)
    if ice_glaciers_fact_chosen == 1:
        await ctx.send(f"Вот вам факт о ледниках:\n{ice_glacier_fact1}")
    if ice_glaciers_fact_chosen == 2:
        await ctx.send(f"Вот вам факт о ледниках:\n{ice_glacier_fact2}")
    if ice_glaciers_fact_chosen == 3:
        await ctx.send(f"Вот вам факт о ледниках:\n{ice_glacier_fact3}")

#TOKEN
bot.run()
