# bot.py
import os

import discord
from dotenv import load_dotenv

#fetching token from .env file 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# Creatting client discord connection 
client = discord.Client()

#creating client 
@client.event

# implemented on_ready() event handler 
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)