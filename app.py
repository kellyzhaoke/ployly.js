# import necessary libraries
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DataSets/belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

class Belly(db.Model):
    __tablename__ = 'belly'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    type = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<Belly %r>' % (self.name)


@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

labels=[
    1166,2858,481,2263,
    40,1188,351,188,2317,
    1976
]

values=[
                163,
                126,
                113,
                78,
                71,
                51,
                50,
                100,
                30,
                256
        ]


@app.route('/pie')
def data():
    labels, values = zip()
    data=[{
        "labels":labels,
        "values": values,
        "type": "pie"
    }]
    return jsonify(data)
# Query the database and send the jsonified results


if __name__ == "__main__":
    app.run(debug=True)
