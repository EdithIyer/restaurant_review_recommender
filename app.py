# import flask
from flask import Flask, jsonify
import json
app = Flask(__name__)

#Instantiate/create the app and designate the home page
#contains info about the methods
@app.route('/')
def hello():
    return "App that returns some Denver food reviews - taken from theinfatuation.com"

#Get some data
f = open('./denver_infatuation_reviews.json')
data = json.load(f)

#Designate path for all data to be returned with a "GET" request
@app.route('/api/v1/resources/data/all', methods=['GET'])
#function to return all the json data
def api_all():
    return jsonify(data)


