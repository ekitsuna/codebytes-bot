from datetime import datetime
from discord.ext import commands
import discord
import io, asyncio, os
import aiohttp, typing
import datetime, pathlib
import config
import requests
from matplotlib.pyplot import imshow
import numpy as np
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
timer = datetime.datetime.now

@bot.event
async def on_ready():
    print("Logged in as:", bot.user.name)

@bot.command(pass_context=True)
async def upload(ctx, attachment: discord.Attachment,* , message):
    file = attachment.url
    channel = bot.get_channel(config.CHANNEL_ID) #whatever channel you want to send image to
    async with aiohttp.ClientSession() as session:
        async with session.get(file) as resp:
            img = await resp.read()
            with io.BytesIO(img) as file:
                await channel.send(message)
                await channel.send(file=discord.File(file, "image.gif"))

@bot.command(pass_context=True)
async def schedule(ctx, t, min, *, message):
    channel = bot.get_channel(config.CHANNEL_ID)
    #delay of 30 seconds, not quite accurate but it does schedule
    while True:
        if timer().hour == int(t) and timer().minute == int(min):
            await channel.send(message)
        await asyncio.sleep(60)

"""
@bot.command(pass_context=True)
async def spicture(ctx, attachment: discord.Attachment, t, min, *, message):
    channel = bot.get_channel(config.CHANNEL_ID)
    file = attachment.url
    async with aiohttp.ClientSession() as session:
        async with session.get(file) as resp:
            img = await resp.read()
            with io.BytesIO(img) as file:
                while True:
                    if timer().hour == int(t) and timer().minute == int(min):
                        await channel.send(message)
                        await channel.send(file=discord.File(file, "image.gif"))
                    await asyncio.sleep(60)
"""
                    
@bot.command(pass_context=True)
async def message(ctx, *, message):
    channel = bot.get_channel(config.CHANNEL_ID)
    await channel.send(message)

bot.run(config.BOT_TOKEN)