#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

#meme categories for user to select from
meme_categories = ["funny", "wholesome", "silly", "cats" ]
category = ""

#function to get meme from external api by the category requested by the user
@app.route("/<category>", methods=["GET"])
def get_meme():
    #category = "wholesome"
    url = "https://meme-api.herokuapp.com/gimme" + category
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return render_template("meme_index.html", pic= meme_large, subreddit=subreddit)


#the memes are viewed on this route
@app.route("/")
def index():
   #meme_pic, subreddit = get_meme()
   #passing variables to the index.html
   return render_template("meme_index.html", cat=meme_categories,)    # meme_pic=meme_pic, subreddit=subreddit)

#when a user selects a meme category to search by
@app.route("/select", methods=["POST"])
def select_category():
     # check if anything was in the form submitted
    if request.form.get("nm"):
            # if so, pull the value and normalize it
            category = request.form.get("nm")
            # call the get_meme() to get new meme
            gofetch = get_meme(category)
    elif answer == "":
                print("You must type in an answer!")
    return redirect("/category")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

