import requests as rq
import json



ra1=rq.get('https://private-anon-589c768a77-popcornofficial.apiary-proxy.com/random/anime')
ra2=rq.get('https://tv-v2.api-fetch.website/random/anime')
#     if ra1.status_code == 200:
text=ra1.text
rq_json=json.loads(text)
title=rq_json['title']
