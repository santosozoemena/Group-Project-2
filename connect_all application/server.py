from sqlalchemy import func
from flask import  (
                Flask, 
                render_template,
                jsonify,
                request,
                redirect
                )

import pandas as pd

server = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite_data/spotify_data.sqlite'

db = SQLAlchemy(server)

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

@server.before_first_request
def setup():
    db.create_all()

@server.route('/')
def home():
    return render_template('index.html')

@server.route("/scatter_polar")
def scatterPolar_feature():
    
    results = db.session.query(Music.Region, 
                        func.sum(Music.DANCE), 
                        func.sum(Music.ACOUSTIC), 
                        func.sum(Music.LENGTH), 
                        func.sum(Music.POP),
                        func.sum(Music.LOUD), 
                        func.sum(Music.VALENCE), 
                        func.sum(Music.ENERGY), 
                        func.sum(Music.BPM)).group_by(Music.Region).all()  

    region = [result[0] for result in results]
    dance = [int(result[1]) for result in results]
    acoustic = [int(result[2]) for result in results]
    pop = [int(result[4]) for result in results]
    valence = [int(result[6]) for result in results]
    energy = [int(result[7]) for result in results]
    bpm = [int(result[8]) for result in results]

    scatterPolar_trace = [
        {
            'type': 'scatterpolar',
            'name': 'dance',
            'r': dance,
            'theta': region,
            'fill': 'toself',
        },
        {
            'type': 'scatterpolar',
            'name': 'acoustic',
            'r': acoustic,
            'theta': region,
            'fill': 'toself',
        },
        {
            'type': 'scatterpolar',
            'name': 'pop',
            'r': pop,
            'theta': region,
            'fill': 'toself',
        },
        {
            'type': 'scatterpolar',
            'name': 'valence',
            'r': valence,
            'theta': region,
            'fill': 'toself',
        },
        {
            'type': 'scatterpolar',
            'name': 'energy',
            'r': energy,
            'theta': region,
            'fill': 'toself',
        },
        {
            'type': 'scatterpolar',
            'name': 'bpm',
            'r': bpm,
            'theta': region,
            'fill': 'toself',
        }
    ]

    return jsonify(scatterPolar_trace)

# @server.route("/dance")
# def dance_feature():
#     results = db.session.query(Music.Region, func.avg(Music.DANCE)).group_by(Music.Region).all()
#     region = [result[0] for result in results]
#     dance = [int(result[1]) for result in results]
#     plot_trace = {
#         "x": region,
#         "y": dance,
#         "type": "bar",
#         "textposition": 'auto',
#         "opacity": 0.8,
#         "marker": {
#             "color": 'rgb(58,202,25)',
#             "line": {
#                 "color": 'rbg(8,48,107)',
#                 "width": 1.5
#             }
#             }
#         }
#     return jsonify(plot_trace)

# @server.route("/bpm")
# def bpm_feature():
#     results = db.session.query(Music.Region, func.avg(Music.BPM)).group_by(Music.Region).all()
#     region = [result[0] for result in results]
#     bpm = [int(result[1]) for result in results]
#     plot_trace = {
#         "x": region,
#         "y": bpm,
#         "type": "bar"
#     }
#     return jsonify(plot_trace)

# @server.route("/energy")
# def energy_feature():
#     results = db.session.query(
#         Music.Region, func.avg(Music.ENERGY)).group_by(Music.Region).all()
#     region = [result[0] for result in results]
#     energy = [int(result[1]) for result in results]
#     plot_trace = {
#         "x": region,
#         "y": energy,
#         "type": "bar"
#     }
#     return jsonify(plot_trace)

# @server.route("/valence")
# def valence_feature():
#     results = db.session.query(
#         Music.Region, func.avg(Music.VALENCE)).group_by(Music.Region).all()
#     region = [result[0] for result in results]
#     valence = [int(result[1]) for result in results]
#     plot_trace = {
#         "x": region,
#         "y": valence,
#         "type": "bar"
#     }
#     return jsonify(plot_trace)

# @server.route("/loud")
# def loud_feature():
#     results = db.session.query(
#         Music.Region, func.avg(Music.LOUD)).group_by(Music.Region).all()
#     region = [result[0] for result in results]
#     loud = [int(result[1]) for result in results]
#     plot_trace = {
#         "x": region,
#         "y": loud,
#         "type": "bar"
#     }
#     return jsonify(plot_trace)

# @server.route("/acoustic")
# def acoustic_feature():
#     results = db.session.query(
#         Music.Region, func.avg(Music.ACOUSTIC)).group_by(Music.Region).all()
#     region = [result[0] for result in results]
#     acoustic = [int(result[1]) for result in results]
#     plot_trace = {
#         "x": region,
#         "y": acoustic,
#         "type": "bar"
#     }
#     return jsonify(plot_trace)

# @server.route("/test")
# def test_feature():
#     results = db.session.query(Music.Artist, func.avg(Music.DANCE),
#                                func.avg(Music.ACOUSTIC),
#                                func.avg(Music.LOUD),
#                                func.avg(Music.VALENCE),
#                                func.avg(Music.ENERGY),
#                                func.avg(Music.BPM),
#                                func.avg(Music.LENGTH),
#                                func.sum(Music.Streams).label('total')).group_by(Music.Artist).order_by(desc('total')).limit(15).all()

#     artist = [result[0] for result in results]
#     dance = [int(result[1]) for result in results]
#     acoustic = [int(result[2]) for result in results]
#     loudness = [int(result[3]) for result in results]
#     valence = [int(result[4]) for result in results]
#     energy = [int(result[5]) for result in results]
#     bpm = [int(result[6]) for result in results]

#     return jsonify(plot_trace)


if __name__ == "__main__":
    server.run(debug=True)
