import requests as rq
import json
import datetime






class Req():
  ra=rq.get('https://private-anon-589c768a77-popcornofficial.apiary-proxy.com/random/anime')
  ra1=rq.get('https://tv-v2.api-fetch.website/random/anime')
  text=ra1.text
  rq_json=json.loads(text)
  title=rq_json['title']
  

 class Time():
  c_time=datetime.datetime.now()
