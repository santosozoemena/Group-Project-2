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
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dance")
def dance_feature():
    results = db.session.query(Music.Region, Music.DANCE).order_by(func.random()).limit(100).all()
    region = [result[0] for result in results]
    dance = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": dance,
        "type": "bar",
        "title": "test"
    }
    return jsonify(plot_trace)


@app.route("/bpm")
def bpm_feature():
    results = db.session.query(Music.Region, Music.BPM).order_by(
        func.random()).limit(100).all()
    region = [result[0] for result in results]
    bpm = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": bpm,
        "type": "bar"
    }
    return jsonify(plot_trace)


@app.route("/energy")
def energy_feature():
    results = db.session.query(Music.Region, Music.ENERGY).order_by(
        func.random()).limit(100).all()
    region = [result[0] for result in results]
    energy = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": energy,
        "type": "bar"
    }
    return jsonify(plot_trace)


@app.route("/valence")
def valence_feature():
    results = db.session.query(Music.Region, Music.VALENCE).order_by(
        func.random()).limit(100).all()
    region = [result[0] for result in results]
    valence = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": valence,
        "type": "bar"
    }
    return jsonify(plot_trace)


@app.route("/loud")
def loud_feature():
    results = db.session.query(Music.Region, Music.LOUD).order_by(
        func.random()).limit(100).all()
    region = [result[0] for result in results]
    loud = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": loud,
        "type": "bar"
    }
    return jsonify(plot_trace)


@app.route("/acoustic")
def acoustic_feature():
    results = db.session.query(Music.Region, Music.ACOUSTIC).order_by(
        func.random()).limit(100).all()
    region = [result[0] for result in results]
    acoustic = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": acoustic,
        "type": "bar"
    }
    return jsonify(plot_trace)


@app.route("/pop")
def pop_feature():
    results = db.session.query(Music.Region, Music.POP).order_by(
        func.random()).limit(100).all()
    region = [result[0] for result in results]
    pop = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": pop,
        "type": "bar"
    }
    return jsonify(plot_trace)


@app.route("/length")
def length_feature():
    results = db.session.query(Music.Region, Music.LENGTH).order_by(
        func.random()).limit(100).all()
    region = [result[0] for result in results]
    pop = [int(result[1]) for result in results]
    # Generate the plot trace
    plot_trace = {
        "x": region,
        "y": length,
        "type": "bar"
    }
    return jsonify(plot_trace)

if __name__ == "__main__":
    app.run(debug=True)
