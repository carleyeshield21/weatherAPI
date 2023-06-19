import requests

endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = '58c0d548eaa02acefe1d3a23164187a1'

weather_params = {
    'lat': 14.805699,
    'lon': 121.065529,
    'appid': api_key,
}

rispans = requests.get(endpoint,params=weather_params)
print(rispans.status_code)
weather_data = rispans.json()
# print(weather_data['list'][2])
# print(weather_data['list'][2]['weather'])
# print(weather_data['list'][2]['weather'][0])
# print(weather_data['list'][2]['weather'][0]['id'])

# Getting only the first 12 using the slice method
weather_slice = weather_data['list'][:12]
# print(weather_slice)

# Set a boolean condition so we don't have to output Bring Umbrella multiple times
it_will_rain = False

# Looping through the weather slice
for hour_data in weather_slice:
    # print(hour_data['weather'])
    condition_code = hour_data['weather'][0]['id']
    # print(condition_code)
    if int(condition_code) < 700:
        # print('Bring umbrella')
        it_will_rain = True

if it_will_rain:
    print('Bring Umbrella')