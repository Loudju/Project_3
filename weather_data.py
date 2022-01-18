import requests
import scrape_states
from geojson import Point, Feature, FeatureCollection, dump
from pymongo import MongoClient

def api(state):
    city = []
    severity = []
    event = []
    urgency = []
    headline = []
    coordinates = []
    #states = scrape_states.scrape()
    error = 0
    
    
    try:
            query = f"https://api.weather.gov/alerts/active?status=actual&message_type=alert&area={state}&severity=Severe"
            weather_response = requests.get(query).json()
            print(state)
            print(query)
            if len(weather_response["features"]) > 0:
                impacts = len(weather_response["features"])
                for x in range(impacts):
                    city.append(weather_response["features"][x]["properties"]["areaDesc"])
                    severity.append(weather_response["features"][x]["properties"]["severity"])
                    event.append(weather_response["features"][x]["properties"]["event"])
                    urgency.append(weather_response["features"][x]["properties"]["urgency"])
                    headline.append(weather_response["features"][x]["properties"]["headline"])
                    coordinates.append(weather_response["features"][x]["geometry"]["coordinates"])
    except KeyError:
            error = error + 1
    except TypeError:
            error = error + 1
    return weather_response

def json(state):
    features = []
    point = Point(())
    properties = {}
    error = 0
    
    try:
            query = f"https://api.weather.gov/alerts/active?status=actual&message_type=alert&area={state}&severity=Severe"
            weather_response = requests.get(query).json()

            #validating inputs
            print(state)
            print(query)

            if len(weather_response["features"]) > 0:
                impacts = len(weather_response["features"])
                for x in range(impacts):
                    point = weather_response["features"][x]["geometry"]["coordinates"]
                    properties = {"headline": weather_response["features"][x]["properties"]["headline"]}
                    features.append(Feature(geometry=point, properties=properties))
    except KeyError:
            error = error + 1
    except TypeError:
            error = error + 1
    feature_collection = FeatureCollection(features)
    with open("feature_collection_geoJson.geojson", 'w') as g:
         dump(feature_collection, g)
    client = MongoClient("localhost", 27017)
    db = client["weather_db"]
    collection = db["collections"]
    with open("feature_collection_json.json", 'w') as j:
         collection_file = json.load(j)
    collection.insert_one(collection_file)
    client.close()
    return feature_collection


