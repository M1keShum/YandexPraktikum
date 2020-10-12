import requests


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text.strip()
    else:
        return '<ошибка на сервере погоды. попробуйте позже>'


def what_temperature(weather):
    if (weather == '<сетевая ошибка>' or
            weather == '<ошибка на сервере погоды. попробуйте позже>'):
        return weather
    temperature = weather.split()[1]
    parsed_temperature = ''
    for char in temperature:
        if char == '-':
            parsed_temperature += char
        try:
            num = int(char)
            parsed_temperature += char
        except ValueError:
            continue
    return parsed_temperature


def what_conclusion(parsed_temperature):
    try:
        # Приведите parsed_temperature к типу int
        # и сохраните полученное число в переменную temperature
        if "-" in parsed_temperature:
            temperature = int(parsed_temperature[1] + parsed_temperature[2])
        else:
            temperature = int(parsed_temperature)

        # Теперь можно сравнивать temperature с заданными пределами 18°С и 27°С
        # и возвращать нужные фразы в зависимости от результатов сравнения.
        if temperature < 18:
            return "холодно"
        elif temperature >= 18 and temperature <= 27:
            return "в самый раз"
        elif temperature > 27:
            return "жарко"
        # Если (if) температура строго меньше 18:
        # вернуть (return) фразу со словом 'холодно'
        # Если температура в диапазоне от 18 до 27 включительно
        # вернуть фразу со словами 'в самый раз'
        # В остальных случаях:
        # вернуть фразу со словом 'жарко'

    except ValueError:
        return "Не могу узнать погоду"
        # Если parsed_temperature не удалось преобразовать в число —
        # значит, погодный сервис сломался и надо вернуть фразу "Не могу узнать погоду..."
