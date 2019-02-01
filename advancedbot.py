from discord.ext import commands
from gifplz import hent_gif_url
from dictionary import alle_grundstoffer

TOKEN = "NTQwODE1NzQ5OTgwMjI1NTU2.DzWkdg.8znkvamExm-UCeFjzy7U_OjOSZc"

# Betyder at man starter en bot kommando med !
# Eller hvad man har skrevet i command_prefix
bot = commands.Bot(command_prefix='!')

# Giver en !hello kommando
@bot.command()
async def hello():
    await bot.say("hello world")

# Kommando med en parameter
@bot.command()
async def bedste_spil(spilnavn=None):

    if not spilnavn:
        return

    await bot.say("Det bedste spil er: " + spilnavn)

# Kommando til at sende en gif
@bot.command()
async def gif(gif=None):
    if not gif:
        return

    gif = hent_gif_url(søgeord=gif)navn


    await bot.say("her er din gif: " + gif)

# Kommando til at sende grundstoffer
@bot.command()
async def grundstoffer(grundstof=None):
    if not grundstof:
        return
    stof = alle_grundstoffer[grundstof]
    await bot.say("Her er mere info for " + stof["stof"] + ","  + stof["link"])

# Ikke så vigtig
@bot.event
async def on_ready():
    print("MIN BOT ER STARTET!!!")

bot.run(TOKEN, bot=True)
