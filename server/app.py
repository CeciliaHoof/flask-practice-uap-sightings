#!/usr/bin/env python3

from flask import Flask, make_response, request
from flask_migrate import Migrate

# import model and db instance
from models import Sighting, db

# Initialize Flask app
app = Flask(__name__)

# configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize the db instance
db.init_app(app)

# Define routes and views
@app.route('/')
def index():
    response_body = {'message': "The UAPID welcome our new extraterrestrial overlords!"}
    response = make_response(response_body, 200)
    return response

@app.route('/sightings')
def sightings():
    sightings = []
    for sighting in Sighting.query.all():
        sightings.append(sighting.to_dict())
    body = {'sightings': sightings}
    return make_response(body, 200)

@app.route('/sightings/<int:id>')
def sighting_by_id(id):
    sighting = Sighting.query.filter(Sighting.id == id).first()
    body = {'sighting': sighting.to_dict()}
    return make_response(body, 200)

@app.route('/sightings/<string:location>')
def sighting_by_location(location):
    sighting = Sighting.query.filter(Sighting.location == location).first()
    body = {'sighting': sighting.to_dict()}
    return make_response(body, 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)