# Course: DSC510
# Assignment: 3.1
# Date: 3/24/20
# Name: Laura Hoffmann
# Description: Program to calculate cost at a bulk discount
Welcome_Message = "Welcome to Fiber Optics R Us!"
print(Welcome_Message)
Company_Name = input("What is your company's name?\n")
Feet = input("How many feet of fiber optic cable do you need to be installed?\n")
if int(Feet) <= int(100):
    Total_Cost = (.87) * int(Feet)
elif int(100) < int(Feet) <= int(250):
    Total_Cost = (.80) * int(Feet)
elif int(250) < int(Feet) <= int(500):
    Total_Cost = (.70) * int(Feet)
else:
    Total_Cost = (.50) * int(Feet)
print("The total cost for", Company_Name, "will be $", Total_Cost, "for", Feet, "of fiber optic cable to be installed.")


