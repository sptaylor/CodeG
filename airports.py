from sqlalchemy import BigInteger, Column, Float, Integer, Text
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airports.sqlite'

db = SQLAlchemy(app)


class Airport(db.Model):
    __tablename__ = 'airports'

    id = db.Column(db.Integer, primary_key=True)
    Airport_ID = db.Column(db.BigInteger)
    Name = db.Column(db.Text)
    City = db.Column(db.Text)
    Country = db.Column(db.Text)
    IATA_FAA = db.Column(db.Text)
    ICAO = db.Column(db.Text)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    Altitude = db.Column(db.BigInteger)
    Timezone = db.Column(db.Float)
    DST = db.Column(db.Text)
    Tz_db_time_zone = db.Column(db.Text)


ALL_AIRPORTS = Airport.query.all()


def filter_airport_by_country(country):
    country_airports = []
    for airport in ALL_AIRPORTS:
        if airport.Country == country:
            country_airports.append(airport.Name)
    return country_airports


def get_countries():
    country_set = set()
    for airport in ALL_AIRPORTS:
        country_set.add(airport.Country)
    return country_set


@app.route("/")
def index():
    # see page 101 for html example
    countries = get_countries()
    return render_template('index.html', countries=countries)


@app.route("/solve")
def airports():
    country = request.args['country']
    solutions = filter_airport_by_country(country)
    return render_template('solve.html', data=sorted(solutions))


