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

 
class Reaction():
  heart=1000
  rolling_eyes=900
  cherry_blossom=1150
  ok_hand=900
  kiss=800
  thinking=700
  poop=800
  zzz=500
  scream=700
  innocent=800
