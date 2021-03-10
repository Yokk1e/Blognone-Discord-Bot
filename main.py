import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Hi YOkk1e')

@client.event
async def on_message(message):
  if message.author == client:
    return
  
  if message.content.startswith('$test'):
    await message.channel.send('test naja')

client.run(os.getenv('TOKEN'))