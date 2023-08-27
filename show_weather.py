import requests

def show_weather():
    payload = {"n" : "", "M" : "", "T" : "", "q" : "", "lang" : "ru"}
    locations = ['Лондон', 'Шереметьево', 'Череповец']
    responses = []
    for location in locations:
        response = requests.get(f'https://wttr.in/{location}', params=payload)
        response.raise_for_status()
        responses.append(response)
    return responses

if __name__ == '__main__':
    weather_report = show_weather()
    for i in weather_report:
        print(i.text)