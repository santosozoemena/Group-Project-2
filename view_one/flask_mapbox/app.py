import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pandas as pd

from flask import (
    Flask, 
    render_template,
    jsonify,
    request,
    redirect)

engine = create_engine('sqlite:///spotify_data.sqlite')

Base = automap_base()
Base.prepare(engine, reflect= True)
Music = Base.classes.spotify_table

session = Session(engine)

app = Flask(__name__)


from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotify_data.sqlite'

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

@app.route('/region_intensities')
def region_intensity():
    
    regions = [
    'Ecuador',
    'France',
    'Argentina',
    'Finland',
    'Norway',
    'Italy',
    'Lithuania',
    'Phillipines',
    'Taiwan',
    'New Zealand',
    'Estonia',
    'Turkey',
    'United States of America',
    'El Salvador',
    'Costa Rica',
    'Germany',
    'Chile'
    ]

    sel = [
        Music.ENERGY,
        Music. BPM,
        Music.DANCE,
        Music.ACOUSTIC,
        Music.POP,
        Music.Latitude,
        Music.Longitude
    ]

    features = []
    ecuador_intensity = []
    france_intensity = []
    argentina_intensity = []
    finland_intensity = []
    norway_intensity = []
    italy_intensity = []
    lithuania_intensity = []
    phillipines_intensity = []
    taiwan_intensity = []
    zealand_intensity = []
    estonia_intensity = []
    turkey_intensity = []
    america_intensity = []
    salvador_intensity = []
    costa_intensity = []
    germany_intensity = []
    chile_intensity = []

    for region in regions:
        features.append({
            region : session.query(*sel).filter(Music.Region == region).all()  
        })
        
    ecuador_features = features[0]['Ecuador']
    ecuador_features = pd.DataFrame(ecuador_features)

    for key in ecuador_features:
        ecuador_intensity.append({
            key: ecuador_features[key].sum()
        })

    france_features = features[1]['France']
    france_features = pd.DataFrame(france_features)

    for key in france_features:
        france_intensity.append({
            key: france_features[key].sum()
        })
        
    argentina_features = features[2]['Argentina']
    argentina_features = pd.DataFrame(argentina_features)

    for key in argentina_features:
        argentina_intensity.append({
            key: argentina_features[key].sum()
        })       
        
    finland_features = features[3]['Finland']
    finland_features = pd.DataFrame(finland_features)

    for key in finland_features:
        finland_intensity.append({
            key: finland_features[key].sum()
        })

    norway_features = features[4]['Norway']
    norway_features = pd.DataFrame(norway_features)

    for key in norway_features:
        norway_intensity.append({
            key: norway_features[key].sum()
        })

    italy_features = features[5]['Italy']
    italy_features = pd.DataFrame(italy_features)

    for key in italy_features:
        italy_intensity.append({
            key: italy_features[key].sum()
        })

    lithuania_features = features[6]['Lithuania']
    lithuania_features = pd.DataFrame(lithuania_features)

    for key in lithuania_features:
        lithuania_intensity.append({
            key: lithuania_features[key].sum()
        })

    phillipines_features = features[7]['Phillipines']
    phillipines_features = pd.DataFrame(phillipines_features)

    for key in phillipines_features:
        phillipines_intensity.append({
            key: phillipines_features[key].sum()
        })

    taiwan_features = features[8]['Taiwan']
    taiwan_features = pd.DataFrame(taiwan_features)

    for key in taiwan_features:
        taiwan_intensity.append({
            key: taiwan_features[key].sum()
        })

    zealand_features = features[9]['New Zealand']
    zealand_features = pd.DataFrame(zealand_features)

    for key in zealand_features:
        zealand_intensity.append({
            key: zealand_features[key].sum()
        })

    estonia_features = features[10]['Estonia']
    estonia_features = pd.DataFrame(estonia_features)

    for key in estonia_features:
        estonia_intensity.append({
            key: estonia_features[key].sum()
        })     

    turkey_features = features[11]['Turkey']
    turkey_features = pd.DataFrame(turkey_features)

    for key in turkey_features:
        turkey_intensity.append({
            key: turkey_features[key].sum()
        })   

    america_features = features[12]['United States of America']
    america_features = pd.DataFrame(america_features)

    for key in america_features:
        america_intensity.append({
            key: america_features[key].sum()
        }) 

    salvador_features = features[13]['El Salvador']
    salvador_features = pd.DataFrame(salvador_features)

    for key in salvador_features:
        salvador_intensity.append({
            key: salvador_features[key].sum()
        }) 

    costa_features = features[14]['Costa Rica']
    costa_features = pd.DataFrame(costa_features)

    for key in costa_features:
        costa_intensity.append({
            key: costa_features[key].sum()
        })    
            
    germany_features = features[15]['Germany']
    germany_features = pd.DataFrame(germany_features)

    for key in germany_features:
        germany_intensity.append({
            key: germany_features[key].sum()
        })

    chile_features = features[16]['Chile']
    chile_features = pd.DataFrame(chile_features)

    for key in chile_features:
        chile_intensity.append({
            key: chile_features[key].sum()
        })
            
    return jsonify(
        ecuador_intensity,
        france_intensity,
        argentina_intensity,
        finland_intensity,
        norway_intensity,
        italy_intensity,
        lithuania_intensity,
        phillipines_intensity,
        taiwan_intensity,
        zealand_intensity,
        estonia_intensity,
        turkey_intensity,
        america_intensity,
        salvador_intensity,
        costa_intensity,
        germany_intensity,
        chile_intensity
        )

if __name__ == '__main__':
    app.run(debug = True)
