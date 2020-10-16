# Course: DSC510
# Assignment: 4.1
# Date: 3/31/20
# Name: Laura Hoffmann
# Description: Program to demonstrate use of functions

Welcome_Message = "Welcome to Fiber Optics R Us!"
print(Welcome_Message)
def Total_Cost(Feet, Costperfoot):
    return(int(Feet) * float(Costperfoot))
Company_Name = input("What is your company's name?\n")
Feet = input("How many feet of fiber optic cable do you need to be installed?\n")
if int(Feet) <= 100:
    Costperfoot = ("{:.2f}".format(.87))
elif 100 < int(Feet) <= 250:
    Costperfoot = ("{:.2f}".format(.80))
elif 250 < int(Feet) <= 500:
    Costperfoot = ("{:.2f}".format(.70))
elif 500 < int(Feet):
    Costperfoot = ("{:.2f}".format(.50))
print(Feet, "Feet of fiber optic cable to be installed.")
print("At $", Costperfoot, "per foot of cable.")
print("Total cost: $", ("\b{:.2f}".format(Total_Cost(Feet, Costperfoot))))
print("The total cost for", Company_Name, "will be $", ("\b{:.2f}".format(Total_Cost(Feet, Costperfoot))), "for", Feet, "feet of fiber optic cable to be installed.")
