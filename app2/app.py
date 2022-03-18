# -*- coding: utf-8 -*-
import collections
import os
import pymongo
from flask import Flask

app = Flask(__name__)

@app.route("/app2/")
def home():

    # Docker will set the address of the linked MongoDB container in the following
    # environmental variable.  We already know the port that MongoDB is exposed on.
    #db_host = str(os.environ["DB_PORT_27017_TCP_ADDR"])
    db_port = 27017

    # # Get a connection to MongoDB, then get the collection 'webStats' from the
    # # database 'app2Db'.
    client = pymongo.MongoClient("mongo", db_port)
    collection = client["food"]["fruits"]
    array=[]
    for x in collection.find():
        array.append(x)
    print(array)

    
    # mystring ="""<h1>This is app2!</h1>
    #           <p>Hit Count:{1} </p>
    #           <img src='static/images/flask-badge-2.png'/>"""

    # return mystring.format(collection)

    return """<h1>This is app2!</h1>
              <p>Hit Counts: %s </p>
              <img src='static/images/flask-badge-2.png'/>""" % (str(array))


if __name__ == '__main__':
    app.run() 