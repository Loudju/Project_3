from flask import Flask, render_template, request, redirect, jsonify, make_response
app = Flask(__name__)

@app.route("/")
def index():
    #home page for info and navigation
    return render_template("index.html")

@app.route("/charts")
def charts():
    #display drop down menu with states list
    #accept the state selection and display charts
    return  render_template("charts.html")

@app.route("/map")
def map():
    #display drop down menu with states list
    #accept the state selection and display map
    return render_template("map.html")    

if __name__ == '__main__':
    app.run()