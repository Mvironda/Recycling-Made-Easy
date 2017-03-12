from flask import Flask
from flask import render_template

from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

#import recycle

import csv

borough_data = {}

class BoroughData:
    def __init__(self, name, recycling_day, recycling_frequency, general_waste_days, general_waste_frequency, food_waste_days, food_waste_frequency, materials_provided, contact):
        self.name = name
        self.recycling_day = recycling_day
        self.recycling_frequency = recycling_frequency
        self.general_waste_days = general_waste_days
        self.general_waste_frequency = general_waste_frequency
        self.food_waste_days = food_waste_days
        self.food_waste_frequency = food_waste_frequency
        self.materials_provided = materials_provided
        self.contact = contact

def find_BoroughData(boroughName):
   	return borough_data.get(boroughName)

def load_data():
    with open('library.csv', 'rU') as f:
        reader = csv.reader(f)
        for row in reader:
            a_borough_data = BoroughData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            borough_data[str(a_borough_data.name).lower()] = a_borough_data


app = Flask("MyApp")

@app.route("/")
def borough():
    return render_template("recycle.html")

@app.route("/<boroughName>")
def borough_name(boroughName):
    print boroughName
    load_data()
    bdata = find_BoroughData(boroughName)
    print bdata
    return render_template("recycle.html", recycleday=bdata.recycling_day, frequency=bdata.recycling_frequency, generalwastedays=bdata.general_waste_days, generalwastefrequency=bdata.general_waste_frequency, foodwastedays=bdata.food_waste_days, foodwastefrequency=bdata.food_waste_frequency, materialsprovided=bdata.materials_provided, contact=bdata.contact)

app.run()
