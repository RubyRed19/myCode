#!/usr/bin/python3

# An object of Flask class is our WSGI application
from flask import Flask
from flask import render_template
from flask import jsonify
import requests
import json

app = Flask(__name__)


#motivational quotes
quotes = [
            "Concentrate all your thoughts upon the work in hand. The sun's rays do not burn until brought to a focus. - Alexander Graham Bell",
            "Either you run the day or the day runs you. -Jim Rohn",
            "I’m a greater believer in luck, and I find the harder I work the more I have of it. - Thomas Jefferson",
            "Opportunity is missed by most people because it is dressed in overalls and looks like work. - Thomas Edison",
            "Setting goals is the first step in turning the invisible into the visible.- Tony Robbins",
         ]

#list of songs to make you feel good
songs = [
            "Don't Stop Me Now -Queen",
            "Walking on Sunshine -Katrina & The Waves",
            "Eye of the Tiger -Survivor",
            "I'm a Believer -The Monkees",
            "Livin' on a Prayer -Jon Bon Jovi",
         ]
            

def get_meme():
    sr = "/wholesomememes"
    url = "https://meme-api.herokuapp.com/gimme"  + sr
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

#this is where the app loads
@app.route("/")
def index():
   meme_pic, subreddit = get_meme()
   #passing variables to the index.html
   return render_template("index.html", meme_pic=meme_pic,  subreddit=subreddit)

@app.route("/songs")
def show_songs():
    return jsonify(songs)

@app.route("/quotes")
def show_quotes():
    return jsonify(quotes)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

