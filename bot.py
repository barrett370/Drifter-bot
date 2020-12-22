import discord
import os

client = discord.Client()


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



token = open(".envrc").read().split("=")[1]

client.run(token)
