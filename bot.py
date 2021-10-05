# bot.py
import os

import discord
from dotenv import load_dotenv

# getting env tokens 
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client = discord.Client()

# starting client 
@client.event

# getting guild data from on_ready()
async def on_ready():
    #looping for the clients in the guild 
    for guild in client.guilds:
        if guild.name == GUILD:
            break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        members = '\n - '.join([member.name for member in guild.members]) 
        print(f'Guild Members:\n - {members}')
    else:
        print(
            f'This are the list of all clients{client.guilds}\n'
            
        )

client.run(TOKEN)