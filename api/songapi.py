from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_songs import *

song_api = Blueprint('song_api', __name__,
                   url_prefix='/api/song')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(song_api)

class SongsAPI:
    # not implemented
    class _Create(Resource):
        def post(self, song):
            pass
            
    # getSongs()
    class _Read(Resource):
        def get(self):
            return jsonify(getSongs())

    # getSong(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getSong(id))

    # getRandomSong()
    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomSong())
    
    # getRandomSong()
    class _ReadCount(Resource):
        def get(self):
            count = countSongs()
            countMsg = {'count': count}
            return jsonify(countMsg)

    # put method: addSongSad
    class _UpdateSad(Resource):
        def put(self, id):
            addSongSad(id)
            return jsonify(getSong(id))
    # put method: addSongHappy
    class _UpdateHappy(Resource):
        def put(self, id):
            addSongHappy(id)
            return jsonify(getSong(id))
    # put method: addSongRage
    class _UpdateRage(Resource):
        def put(self, id):
            addSongRage(id)
            return jsonify(getSong(id))
    # put method: addSongIndian
    class _UpdateIndian(Resource):
        def put(self, id):
            addSongIndian(id)
            return jsonify(getSong(id))
    

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:song>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateSad, '/sad/<int:id>')
    api.add_resource(_UpdateHappy, '/happy/<int:id>')
    api.add_resource(_UpdateRage, '/rage/<int:id>')
    api.add_resource(_UpdateIndian, '/indian/<int:id>')
    
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://ssjncpt.duckdns.org' # run from web
    url = server + "/api/song"
    responses = []  # responses list

    # get count of songs on server
    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update emotion opinion test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read song by id
        ) 
    responses.append(
        requests.put(url+"/sad/"+num) # add to sad count
        ) 
    responses.append(
        requests.put(url+"/happy/"+num) # add to happy count
        ) 
    responses.append(
        requests.put(url+"/rage/"+num) # add to rage count
        ) 
    responses.append(
        requests.put(url+"/indian/"+num) # add to indian count
        ) 

    # obtain a random song
    responses.append(
        requests.get(url+"/random")  # read a random song
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")