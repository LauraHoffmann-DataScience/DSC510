# Course: DSC510
# Assignment: 10.1
# Date: 5/12/20
# Name: Laura Hoffmann
# Description: Program to demonstrate web services

import requests

url = "https://api.chucknorris.io/jokes/random"

welcome_message = "Welcome to the Chuck Norris Joke Center!"
print(welcome_message)

# [1] Adding a loop allows the user to see as many jokes as they'd like
# [2] Using a try block in case the url does not work the user will see a nice error message
# [3] Using JSON and printing value from the dict pulls out only the joke from the url so the user doesn't see extra data
# [4] The user is able to use capital or lowercase
# [5] User sees nice error message in case they use unrecognizable input

looping = True
while looping:  # [1]
    user_inp = input("Type 'y' if you would like to hear a joke or 'q' to quit: ")
    if user_inp == 'y':  # [4]
        try:  # [2]
            response = requests.request("GET", url)
            dict = response.json()
            print(dict['value'])  # [3]
            looping = True
        except:
            print("We apologize, there was an issue connecting to the website. Try again later.")
            looping = False
    elif user_inp == 'Y':  # [4]
        try:
            response = requests.request("GET", url)
            dict = response.json()
            print(dict['value'])
            looping = True
        except:
            print("We apologize, there was an issue connecting to the website. Try again later.")
            looping = False
    elif user_inp == 'q':  # [4]
        print("Thank you for joining us today!")
        looping = False
    elif user_inp == 'Q':  # [4]
        print("Thank you for joining us today!")
        looping = False
    else:  # [5]
        print("We didn't understand, please print a 'y' or 'q'.")
