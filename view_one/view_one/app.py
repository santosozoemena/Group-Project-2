import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import Flask, jsonify

engine = create_engine('sqlite:///spotify_data.sqlite')

#create inspector and connect to engine
inspector = inspect(engine)

print(inspector.get_table_names())

columns = inspector.get_columns('spotify_table')
for column in columns:
    print(column['name'], column['type'])

print(columns)

#reflect an existing database into a new model
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect= True)

print(Base.classes.keys())


#save reference
# Music = Base.classes.music

# app = Flask(__name__)

# @app.route('/')



# if __name__ == '__main__':
#     app.run(debug = True)
