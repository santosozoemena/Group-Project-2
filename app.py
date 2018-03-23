from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import pymongo
import csv

# create a connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# choose a database to connect #
db = client.spotify_db
collection = db.spotify_db
def csv_to_dict():
    reader = csv.DictReader(open('sample_data.csv'))
    result = {}
    for row in reader:
        key = row.pop('Position')
        result[key] = row
        db.collection.insert_one(row)

    return row
# csv_to_dict()
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
