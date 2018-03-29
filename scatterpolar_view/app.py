from sqlalchemy import func
from flask import  (
                Flask, 
                render_template,
                jsonify,
                request,
                redirect
                )

import pandas as pd

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/spotify_data.sqlite'

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

@app.before_first_request
def setup():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/scatterPolar")
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



if __name__ == "__main__":
    app.run(debug=True)
