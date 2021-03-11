import os
from flask import Flask
from threading import Thread
from blog import get_new_blognnone_contetnt,update_blogs
from replit import db
from dhooks import Webhook


app = Flask('')

@app.route('/')
def webhook():
    hook = Webhook(os.getenv('WEBHOOK_URL'))
    new_blogs = get_new_blognnone_contetnt()
    for new_blog in new_blogs:
      if new_blog not in db["blog_path"]:
        hook.send(new_blog)
        update_blogs(new_blog)
    
    return "Webhook ..."

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()