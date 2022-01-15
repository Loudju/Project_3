import requests
import scrape_states

def scrape():
    city = []
    severity = []
    event = []
    urgency = []
    headline = []
    coordinates = []
    states = scrape_states.scrape()
    
    error = 0
    for state in states:
        try:
            weather_response = requests.get(f"https://api.weather.gov/alerts/active?status=actual&message_type=alert&area={state}&severity=Severe").json()
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
