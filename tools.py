import requests as rq
import json
import datetime
import random





class Req():
  ra=rq.get('https://private-anon-589c768a77-popcornofficial.apiary-proxy.com/random/anime')
  ra1=rq.get('https://tv-v2.api-fetch.website/random/anime')
  text=ra1.text
  rq_json=json.loads(text)
  title=rq_json['title']
  
class Time():
  c_time=datetime.datetime.now()
  s_t=str(c_time)

  

  
  
class Apiai():
  words=['#anime','$time']

 
class Games():
  while True:
    games=['Bread Puppies','Jump Rope Kitten: Nyawatobi','TripTrap','Potion Maker','Crusaders Quest','My Waffle Maker','AfroCat','Hello Kitty','Halo 4','My Cat Album','LINE: Disney Tsum Tsum','Cat Room','Alphabear','Play With Cats','My Dog Album','Giant Turnip Game','MEOW MEOW STAR ACRES','Patchmania','Tiny Sheep','Hello Kitty World – Fun Park Game']
    random_game=random.choice(games)
    time.sleep(10800)
  
