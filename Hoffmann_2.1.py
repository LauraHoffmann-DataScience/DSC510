# Course: DSC510
# Assignment: 2.1
# Date: 3/18/20
# Name: Laura Hoffmann
# Description: Program for Calculating Costs and Printing Receipt
Welcome_Message = "Welcome to Fiber Optics R Us!"
print(Welcome_Message)
Company_Name = input("What is your company's name?") #User inputs a company name
FeetofFOC = input("How many feet of fiber optic cable do you need to have installed?") #User inputs the amount
Installation_Cost = int(FeetofFOC) * .87 #Multiplies the amount they need by the cost per foot
print("Here is the receipt for", Company_Name, "the total cost for the installation of", FeetofFOC, "feet of fiber optic cable will be $", Installation_Cost)




