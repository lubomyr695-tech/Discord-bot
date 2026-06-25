import os
import discord
from discord.ext import commands
from mcstatus import JavaServer

TOKEN = os.getenv("Token")

SERVER_IP = "GoldMoneyS2.aternos.me"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def start(ctx):
    await ctx.send("Server is starting. This may take some time.")

@bot.command()
async def status(ctx):
    try:
        server = JavaServer.lookup(SERVER_IP)
        status = server.status()
        await ctx.send(f"Server is ONLINE. Players: {status.players.online}")
    except:
        await ctx.send("Server is OFFLINE or still starting.")

@bot.command()
async def ip(ctx):
    await ctx.send(f"Server IP: {SERVER_IP}")

bot.run(TOKEN)
      
