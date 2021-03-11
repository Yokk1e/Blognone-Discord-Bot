import discord
import os
from blog import get_new_blognnone_contetnt,update_blogs
from replit import db
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('blognone content ready')

@client.event
async def on_message(message):
  if message.author.bot:
    return

  if message.content.startswith('$trigger'):
    new_blogs = get_new_blognnone_contetnt()
    has_blog = False

    for new_blog in new_blogs:
      if new_blog not in db["blog_path"]:
        has_blog = True
        await message.channel.send(new_blog)
        update_blogs(new_blog)
    
    if has_blog == False:
      await message.channel.send('Blog up to date')


keep_alive()
client.run(os.getenv('TOKEN'))