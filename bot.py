from datetime import datetime
from discord.ext import commands
import discord
import io, asyncio
import aiohttp
import time

BOT_TOKEN = "MTE5MzcwOTIzMjAwNTA2NjgxNA.GrBXNp.unpKH7AH1cAjtgWnDPSn05XqpEBiGXVDyuOIx8"
CHANNEL_ID = 1141507451259211839

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Logged in as:", bot.user.name)
    channel = bot.get_channel(CHANNEL_ID)

@bot.command(pass_context=True)
async def picture(ctx, message, file):
    channel = bot.get_channel(CHANNEL_ID) #Whatever channel you want to send image to
    async with aiohttp.ClientSession() as session:
        async with session.get(file) as resp:
            img = await resp.read()
            with io.BytesIO(img) as file:
                await channel.send(message)
                await channel.send(file=discord.File(file, "image.png"))

bot.run(BOT_TOKEN)