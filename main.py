import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv("variables\.env.txt")
KEYS = os.getenv("api_key")
ACCOUNT = os.getenv("account_sid")
TOKEN = os.getenv("auth_token")
lat =39.960491
lon = -75.262779
parameters ={
    "lat": lat,
    "lon": lon,
    "appid": KEYS,
    "exclude": "current,minutely,daily,"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for things in range(12):
    save_two = (data["hourly"][things]["weather"][0]["id"])
    if save_two <= 700:
      will_rain = True
    else:
      will_rain = False

if will_rain == True:
    client = Client(ACCOUNT, TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umberella ☂",
        from_='+19897621014',
        to='+12158239955'
    )
    print(message.sid)
else:
    pass



