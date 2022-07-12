import requests
from twilio.rest import Client
import os
KEYS = os.getenv('weather_api_key')
ACCOUNT = os.getenv('twilio_account')
TOKEN = os.getenv('twilio_token')
NUMBER = os.getenv('phone_number')
API_END_POINT =os.getenv('weather_end_point')
class WeatherAlert:
    def __init__(self):
        self.latitude = 39.960491
        self.longitude = -75.262779
        self.will_rain =False
    def get_weather_data(self):
        parameters = {
            "lat": self.latitude,
            "lon": self.longitude,
            "appid": KEYS,
            "exclude": "current,minutely,daily,"
        }
        response = requests.get(url=API_END_POINT, params=parameters)
        response.raise_for_status()
        data = response.json()
        for things in range(12):
            save_two = (data["hourly"][things]["weather"][0]["id"])
            if save_two <= 700:
                self.will_rain = True
            else:
                self.will_rain = False
    def notification(self):

        if self.will_rain == True:
            client = Client(ACCOUNT, TOKEN)
            message = client.messages \
            .create(
            body="It's going to rain today. Bring an umberella ☂",
            from_='+19897621014',
            to=NUMBER
    )
            print(message.sid)
        else:
            pass

rain_alert = WeatherAlert()
rain_alert.get_weather_data()
rain_alert.notification()
