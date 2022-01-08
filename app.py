from flask import Flask, render_template, request, redirect, jsonify, make_response
import scrape_states
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    state_codes = scrape_states.scrape()
    severity = []
    event = []
    urgency = []
    message = []
    title = []

    for state in state_codes:
        weather_response = requests.get(f"https://api.weather.gov/alerts/active?status=actual&message_type=alert&area={state}&severity=Severe").json()
        severity.append(weather_response["features"][0]["properties"]["severity"])
        event.append(weather_response["features"][0]["properties"]["event"])
        urgency.append(weather_response["features"][0]["properties"]["urgency"])
        message.append(weather_response["features"][0]["properties"]["message"])
        title.append(weather_response["features"]["title"])

    return redirect("/")

@app.route("/charts.html")
def charts():
    return  render_template("charts.html")

@app.route("/map.html")
def map():
    return render_template("map.html")    

if __name__ == '__main__':
    app.run()