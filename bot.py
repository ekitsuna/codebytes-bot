from datetime import datetime
from discord.ext import commands
import discord
import io, asyncio
import aiohttp
import time
import config

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Logged in as:", bot.user.name)
    channel = bot.get_channel(config.CHANNEL_ID)

@bot.command(pass_context=True)
async def picture(ctx, message, file):
    channel = bot.get_channel(config.CHANNEL_ID) #Whatever channel you want to send image to
    async with aiohttp.ClientSession() as session:
        async with session.get(file) as resp:
            img = await resp.read()
            with io.BytesIO(img) as file:
                await channel.send(message)
                await channel.send(file=discord.File(file, "image.png"))

bot.run(config.BOT_TOKEN)