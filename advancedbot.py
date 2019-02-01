from discord.ext import commands
from gifplz import hent_gif_url



TOKEN = "NTQwODE1NzQ5OTgwMjI1NTU2.DzWkdg.8znkvamExm-UCeFjzy7U_OjOSZc"

# Betyder at man starter en bot kommando med !
# Eller hvad man har skrevet i command_prefix
bot = commands.Bot(command_prefix='!')

# Giver en !hello kommando
@bot.command()
async def hello():
    await bot.say("hello world")

# Giver en !jonas kommando
@bot.command()
async def jonas():
    await bot.say("JEG ER JONAS BOT")


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

    gif = hent_gif_url(søgeord=gif)


    await bot.say("her er din gif: " + gif)
#


# Ikke så vigtig
@bot.event
async def on_ready():
    print("MIN BOT ER STARTET!!!")

bot.run(TOKEN, bot=True)
