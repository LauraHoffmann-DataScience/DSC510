# Course: DSC 510
# Assignment: 6.1
# Date: 4/14/2020
# Name: Laura Hoffmann
# Description: Strings and Lists

temperatures = []
looping = True
while looping == True:
    temp = input("Please input a temperature (in Fahrenheit) or input an 's' to stop: ")
    if temp == 's':
        looping = False
    else:
        try:
            temp = int(temp)
            looping = True
            temperatures.append(temp)
        except:
            print("Please enter a number.")
print("Your temperatures are ", temperatures)
high = max(temperatures)
low = min(temperatures)
count = len(temperatures)
print("Your highest temperature is", high)
print("Your lowest temperature is", low)
print("You entered a total of", count, "temperatures")
