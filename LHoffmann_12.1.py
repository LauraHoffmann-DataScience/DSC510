# Course: DSC 510
# Assignment: 12.1
# Date: 5/29/2020
# Name: Laura Hoffmann
# Description: Final project to demonstrate fundamental programming skills through Python

# Ask the user for their zip code or city.
# Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
# Display the weather forecast in a readable format to the user.
# Use functions including a main function.
# Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
# Validate whether the user entered valid data.
# Use requests library
# Use try blocks to ensure that your request was successful.
# Use try blocks when establishing connections to the webservice.

import requests, json

api_key = "a763af2efc2dd95d886ae4a14c5ca53a"
url = "http://api.openweathermap.org/data/2.5/weather?"

welcome_message = "Welcome to the weather app!"
length = len(welcome_message)
print('-' * length)
print(welcome_message)
print('-' * length)


def city_url():
    place = input("What U.S. City?: ")
    complete_url = url + "q=" + place + ",us&appid=" + api_key + "&units=imperial"
    try:
        reach_server(complete_url, place)
    except:
        print("We did not find that city, please try again.")


def zip_url():
    place = input("What U.S. Zip Code?: ")
    complete_url = url + "zip=" + place + "&appid=" + api_key + "&units=imperial"
    try:
        reach_server(complete_url, place)
    except:
        print("We did not find that zip code, please try again.")


def pretty_print(response):
    dict = response.json()
    temps = dict['main']
    weather = dict['weather']
    winds = dict['wind']
    current_temp = temps['temp']
    feels_like = temps['feels_like']
    temp_min = temps['temp_min']
    temp_max = temps['temp_max']
    temp_hum = temps['humidity']
    wea_skies = weather[0]['main']
    clouds = weather[0]['description']
    wind = winds['speed']
    print('- ' * 25)
    print("Temperatures:")
    print("The current temperature is:", current_temp, u"\b\N{DEGREE SIGN}", "F")
    print("It currently feels like:", feels_like, u"\b\N{DEGREE SIGN}", "F")
    print("The max temperature today is:", temp_max, u"\b\N{DEGREE SIGN}", "F")
    print("The min temperature today is:", temp_min, u"\b\N{DEGREE SIGN}", "F")
    print("The humidity in this area is:", temp_hum, "\b%")
    print('- ' * 25)
    print("Other weather data:")
    print("Current skies:", wea_skies)
    print("There are:", clouds)
    print("The wind speed is currently:", wind, "mph")
    print('--' * 25)


def reach_server(complete_url, place):
    response = requests.request("GET", complete_url)
    print("In", place, "...")
    pretty_print(response)


def main():
    looping = True
    while looping == True:
        try:
            requests.request("GET", url)
        except:
            print("Connection unsuccessful, please try again later.")
            break
        city_zip = input("Input '1' if you would you like to retrieve weather data by city, or '2' by zip code. Enter 'q' to quit: ")
        if city_zip == '1':
            city_url()
        elif city_zip == '2':
            zip_url()
        elif city_zip == 'q':
            looping = False
            print("--" * 25)
            print("Thank you for joining us today!")
        else:
            print("We did not understand, please be sure to choose from the list below.")


if __name__ == "__main__":
    main()
