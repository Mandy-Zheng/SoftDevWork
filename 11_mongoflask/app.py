#Amanda Zheng, Tiffany Cao, Team Blank
#K10 -- Import/Export Bank
#K11 --
#2020-03-05
from flask import Flask, render_template, request,session
from pymongo import MongoClient
import json

client = MongoClient("localhost", 27017)
anime = client.weeb.anime
anime.drop()
file = open("anime-offline-database.json", "r")
doc = json.load(file)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def form():

    render_template("form.html")


@app.route("/results", methods=['GET'])
def finished():
    li=[]
    for x in anime.find({"staus": "FINISHED"}):
        li.append(x["title"])
    render_template("results.html", collection=li)
def rec():
    all=[]
    li=[]
    for x in anime.find({{},{"title":1} }):
        all.append(x["title"]) #easier way??
    for x in range(10):
        n=random.randint(0,len(all)-1)
        if n not in num:
        num.append(n)
        li.append(all[n])
    render_template("results.html",collection=li)
def gallery():
    all=[]
    pic=[]
    li=[]
    for x in anime.find({{},{"title":1} }):
        all.append(x["title"]) #easier way??
        pic.append(x["picture"])
    render_template("gallery.html",titles=all,pic=pic)

if __name__ == "__main__":
    app.debug = True
    app.run()
