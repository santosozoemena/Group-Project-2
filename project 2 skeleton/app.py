from sqlalchemy import func
import datetime as dt
import numpy as np
import pandas as pd
import sqlite3

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    g)

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/spotify_data.sqlite"

db = SQLAlchemy(app)

class Music(db.Model):
    __tablename__ = 'spotify_table'

    id = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Integer)
    Position = db.Column(db.Integer)
    Streams = db.Column(db.Integer)
    Track_name = db.Column(db.String)
    Artist = db.Column(db.String)
    Region = db.Column(db.String)
    URL = db.Column(db.String)
    RELEASE = db.Column(db.Integer)
    BPM = db.Column(db.Integer)
    ENERGY = db.Column(db.Integer)
    LOUD = db.Column(db.Integer)
    DANCE = db.Column(db.Integer)
    VALENCE = db.Column(db.Integer)
    LENGTH = db.Column(db.Float)
    ACOUSTIC = db.Column(db.Integer)
    POP = db.Column(db.Integer)
    Population = db.Column(db.Integer)
    Country_Primary_Language = db.Column(db.String)
    Latitude = db.Column(db.Integer)
    Longitude = db.Column(db.Integer)
    Normalized_streams = db.Column(db.Float)
    
    def __repr__(self):
        return f"id={self.id}, name={self.name}"

# Create database classes
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/music")
def emoji_char_data():
    """Return region data and danceability"""

    results = db.session.query(Music.Region, Music.DANCE).order_by(func.random()).limit(100).all()

    emoji_char = [result[0] for result in results]
    scores = [int(result[1]) for result in results]

    # Generate the plot trace
    plot_trace = {
        "x": emoji_char,
        "y": scores,
        "type": "bar"
    }
    return jsonify(plot_trace)

if __name__ == "__main__":
    app.run(debug=True)
