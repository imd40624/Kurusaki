import flask
import requests as rq
import simplejson as json
import random
import time
import os
import apiai



apiai_token=os.environ['api_ai']
app=flask.Flask(__name__)

# @app.route('/', methods=['POST','GET'])
# def ran(data):
#     while True:
#         games=['Bread Puppies','Jump Rope Kitten: Nyawatobi','TripTrap','Potion Maker','Crusaders Quest','My Waffle Maker','AfroCat','Hello Kitty','Halo 4','My Cat Album','LINE: Disney Tsum Tsum','Cat Room','Alphabear','Play With Cats','My Dog Album','Giant Turnip Game','MEOW MEOW STAR ACRES','Patchmania','Tiny Sheep','Hello Kitty World – Fun Park Game']
#         r=random.choice(games)
#         return r
#         time.sleep(20)
        
        
@app.route('/kurusaki/<data>', methods=['POST','GET'])
def ran(data):
        ai = apiai.ApiAI(apiai_token)
        request = ai.text_request()
        request.lang = 'en'
        request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"
        request.query = data
        response = request.getresponse()
        rope = str(response.read())
        rope = rope[rope.index("speech") + 10:]
        rope = rope[0:rope.index("\"")]
        if "$yukinno" in rope:
                rope=rope.replace('$yukinno',"")
                
        return rope
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    app.run(debug=True)
