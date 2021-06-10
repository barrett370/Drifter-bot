import discord
import pickle
from discord.ext import commands
from discord.message import File
import os
import random

client = discord.Client()
bot = commands.Bot(command_prefix='!')

class Raid():
    
    def __init__(self,name,date,time):
        self.name = name
        self.date = date
        self.time = time
        self.members = []

    def add_member(self,member):
        self.members.append(member)

    def remove_member(self,member):
        self.members.remove(member)


    def __str__(self):
        return f"""
        Name: {self.name}
        Date: {self.date}
        Time: {self.time}
        Team: {self.members}
        """

def init():
    global raids
    try:
        ledger = open("raids.pkl","rb")
        raids = pickle.load(ledger)
        ledger.close()
    except:
        open("raids.pkl","w+").close()
        raids = []
    print(raids)
       
def save_raids():
    ledger = open("raids.pkl","wb")
    pickle.dump(raids,ledger)
    ledger.close()
    


def new_raid(ms):
    name = ms[1]
    date = ms[2]
    time = ms[3]
    raid = Raid(name,date,time)
    print(f"added new raid {raid}")
    raids.append(raid)
    save_raids()
    pass

def join_raid(ms,author):
    raids[int(ms[2])].add_member(author.name)

def leave_raid(ms,author):
    raids[int(ms[2])].remove_member(author.name)

def delete_raid(ms):
    raids.pop(int(ms[2]))

async def raid(m):
    ms = m.content.split(" ")
    print(ms)
    if ms[1] == "new":
        new_raid(ms[1:])
    elif ms[1] == "show":
        ret = ""
        c = 0 
        for raid in raids:
            ret += f"{c} : {raid}\n"
            print(f"{c} : {raid}")
            c+=1
        await m.channel.send(ret) 
    elif ms[1] == "join":
        join_raid(ms,m.author)
    elif ms[1] == "leave":
        leave_raid(ms,m.author)
    elif ms[1] == "delete":
        delete_raid(ms)

@client.event
async def on_ready():
    print(f"Client, {client}, has logged in")


@client.event
async def on_message(message):
    if message.content.startswith("!"):
        # Commands
        
        if message.content[1:] == "ping":
            print("pong!")
            await message.channel.send("pong!")
        elif message.content.split(" ")[0][1:] == "raid":
            print("new command")
            await raid(message)
            await message.add_reaction("👍")

    if message.content.lower().__contains__("poggers"):
        await message.channel.send(f"{message.author.mention} Fuck off")

    if message.content.upper() == message.content:
        msg = f"Automated Translation: {message.content.lower()}"
        await message.channel.send(msg)

    if message.content.lower().__contains__("indeed") and message.author != client.user:
        await message.channel.send("http://barrett370.github.io/Ricardo-bot/ricardo-resources/indeed.jpeg")

    drifter_phrases = [
"Ding, Ding, Ding, Ding, Ding!",
"Oooh!",
"Enough foolin' around.",
"Welcome aboard.",
"Welcome to Gambit.",
"Ever pull a gun off a Vex arm? Don't bother. It won't shoot anymore.",
"Go throw some Taken at your friends.",
"You're always welcome on the Derelict."
            ]
    if random.choices([True,False], weights=[0.01,0.99])[0]:
        await message.channel.send(drifter_phrases[random.randint(0,len(drifter_phrases)-1)])


token = open(".envrc").read().split("=")[1]

init()

client.run(token)
