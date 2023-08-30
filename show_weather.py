import requests


def get_weather(location):
    payload = {'n': '', 'M': '', 'T': '', 'q': '', 'lang': 'ru'}
    response = requests.get(f'https://wttr.in/{location}', params=payload)
    response.raise_for_status()
    return response.text


if __name__ == '__main__':
    locations = ['Лондон', 'Шереметьево', 'Череповец']
    for location in locations:
        weather_report = get_weather(location)
        print(weather_report)
