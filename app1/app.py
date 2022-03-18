# -*- coding: utf-8 -*-
from flask import Flask, redirect
import pymongo
from flask import render_template


app = Flask(__name__)

@app.route("/app1/")
def home():
    # return """<h1>This is app1!</h1>"""
    return render_template('index.html', title='Welcome', username='Jake')

@app.route("/app1/add")
def my_form_post():

    db_port = 27017

    # # Get a connection to MongoDB, then get the collection 'webStats' from the
    # # database 'app2Db'.
    client = pymongo.MongoClient("mongo", db_port)
    mydb = client["food"]
    mycol = mydb["fruits"]

    mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(mydict)

    return redirect("http://localhost:80/app2")

if __name__ == '__main__':
    app.run() 