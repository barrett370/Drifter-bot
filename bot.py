import discord
from discord.ext import commands
from discord.message import File
import os

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f"Client, {client}, has logged in")


@client.event
async def on_message(message):
    if message.content.startswith("!"):
        # Commands
        if message.content[1:] == "ping":
            await message.channel.send("pong!")

    if message.content.lower().__contains__("poggers"):
        await message.channel.send(f"{message.author.mention} Fuck off")

    if message.content.upper() == message.content:
        msg = f"Automated Translation: {message.content.lower()}"
        await message.channel.send(msg)

    if message.content.lower().__contains__("indeed") and message.author != client.user:
        await message.channel.send("http://barrett370.github.io/Ricardo-bot/ricardo-resources/indeed.jpeg")


token = open(".envrc").read().split("=")[1]

client.run(token)
