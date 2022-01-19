from asyncio import events
from distutils.log import set_verbosity
from werkzeug.utils import secure_filename
import weather_data
import scrape_states
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, jsonify, make_response
app = Flask(__name__)

state_codes = scrape_states.scrape()
print("This is the state code list:", state_codes)

@app.route("/", methods = ['POST', 'GET'])
def index():
    #home page for info and navigation
    return render_template("index_test.html")

@app.route("/states")
def states():
    return jsonify(state_codes.to_list())

@app.route("/charts")
def charts():
    #display drop down menu with states list
    #accept the state selection and display charts
    return  render_template("charts.html")

@app.route("/map")
def map(state):
    #display drop down menu with states list
    #accept the state selection and display map
    return render_template("map.html")    

if __name__ == '__main__':
    app.run()
