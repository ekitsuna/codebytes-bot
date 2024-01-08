from discord.ext import commands
import discord

BOT_TOKEN = "MTE5MzcwOTIzMjAwNTA2NjgxNA.GrBXNp.unpKH7AH1cAjtgWnDPSn05XqpEBiGXVDyuOIx8"
CHANNEL_ID = 1141507451259211839

bot = commands.Bot(command_prefix="~", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("codebyter")

@bot.command()
async def hello(ctx):
    await ctx.send("hello")  

bot.run(BOT_TOKEN)