import discord
import os
import requests
from bs4 import BeautifulSoup

client = discord.Client()

def get_new_blognnone_contetnt():
  URL = 'https://www.blognone.com'
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  result_main = soup.find('div',id='block-system-main')
  contents = result_main.find('div',class_='content')
  contents_title_box = contents.find_all('div',class_='content-title-box')

  for title_box in contents_title_box:
    tag_a = title_box.find('a')
    print(tag_a['href'])

@client.event
async def on_ready():
  print('blognone content ready')

@client.event
async def on_message(message):
  if message.author == client:
    return

  get_new_blognnone_contetnt()
  

  # print(content.prettify())
  # if message.content.startswith('$getHTML'):
    # await message.channel.send(content.prettify())

client.run(os.getenv('TOKEN'))