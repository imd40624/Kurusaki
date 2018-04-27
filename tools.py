import requests as rq
import json
import os


wu_key=os.environ['WU_API']
owm=os.environ['open_weather']


class rq_ra():
  ra=rq.get('https://private-anon-589c768a77-popcornofficial.apiary-proxy.com/random/anime')
  ra1=rq.get('https://tv-v2.api-fetch.website/random/anime')
  text=ra1.text
  rq_json=json.loads(text)
  title=rq_json['title']
  
class Weather():
  t = u"\u00b0"
  remove_command = ctx.message.content.split("a.weather ")
  city_state = " ".join(remove_command[1:])
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(city_state,owm)
  ser = rq.get(url).text
  rq_json = json.loads(ser)   
  temp = rq_json['main']['temp']
  max_temp = rq_json['main']['temp_max']
  min_temp = rq_json['main']['temp_min']
  dis = rq_json['weather'][0]['description']
  wind = rq_json['wind']['speed']
