import requests
from twilio.rest import Client

endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = '58c0d548eaa02acefe1d3a23164187a1'
account_sid = 'AC19a08ecffde25e6720eb9152fbbd304e'
auth_token = '343da4ac6dd0c73366de5332625ffb1e'

weather_params = {
    'lat': 14.805699,
    'lon': 121.065529,
    'appid': api_key,
}

rispans = requests.get(endpoint,params=weather_params)
weather_data = rispans.json()

weather_slice = weather_data['list'][:12]
it_will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        it_will_rain = True

if it_will_rain:
    # print('Bring Umbrella')
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☂︎",
        from_='+14066292641',
        to='+639282022640'
    )

    print(message.sid)
    print(message.status)
