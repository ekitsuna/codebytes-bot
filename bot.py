from datetime import datetime
from discord.ext import commands
import discord
import io, asyncio
import aiohttp
import datetime
import config

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
timer = datetime.datetime.now

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

@bot.command(pass_context=True)
async def schedule(ctx, t, min, message):
    channel = bot.get_channel(config.CHANNEL_ID)
    #delay of 30 seconds, not quite accurate but it does schedule
    while True:
        if timer().hour == int(t) and timer().minute == int(min):
            await channel.send(message)
        await asyncio.sleep(60)

bot.run(config.BOT_TOKEN)