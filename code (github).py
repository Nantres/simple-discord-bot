import requests

def get_count():
  url = "https://tscache.com/donation_total.json"
  r = requests.get(url, headers={'-': '-'})
  data = r.json()
  counter = data["count"]
  print(counter)
  return counter

import discord
from discord.ext import commands,tasks
intents = discord.Intents.default()
client = discord.Client(intents=intents)

TOKEN = ''   # put your discord token here, if you don't know how, look it up

@client.event
async def on_ready():
  send.start()
  
@tasks.loop(seconds=5)
async def send():
  channel = client.get_channel()  #put channel id here, if you don't know how, look it up
  await channel.send(get_count()) 
    
client.run(TOKEN)
