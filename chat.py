import flask
import json
import requests as rq
import time
import apiai


app=flask.Flask(__name__)


@app.route('/<data>',methods=['POST'])
def get_query(data):
    data=flask.request.get_json()
    return data



if __name__ =="__main__":
    app.run(debug=True)
