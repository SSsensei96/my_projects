

import requests
from bs4 import BeautifulSoup

response = requests.get('https://yandex.kz/')

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    list_of_values = html_doc.find_all('span', {'class': "inline-stocks__value_inner"})
    list_of_names = html_doc.find_all('a', {'class': "home-link home-link_black_yes inline-stocks__link"})

    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)


weather_response = requests.get('https://yandex.kz/pogoda/pavlodar?utm_campaign=informer&utm_content=main_informer'
                                '&utm_medium=web&utm_source=home&utm_term=title')

if weather_response.status_code == 200:
    weather_html_doc = BeautifulSoup(weather_response.text, features='html.parser')
    list_of_weather_in_cities = weather_html_doc.find_all('div', {
        'class': "other-cities__cities"})

    for city_weather in list_of_weather_in_cities:
        result_list = city_weather.text.split('+')
        for city_weather_full in result_list:
            print(city_weather_full)
