correct_number = 7
Guess = input("Guess a number between 1 and 10: \n")
if int(Guess) == int(correct_number):
    print("You are correct!")
elif int(Guess) > int(correct_number):
    print("That is too high.")
    Guess = input("Guess another number: \n")
    if int(Guess) == int(correct_number):
        print("You are correct!")
    elif int(Guess) > int(correct_number):
        print("That is still too high.")
        Guess = input("Guess another number: \n")
        if int(Guess) == int(correct_number):
            print("That is correct!")
        elif int(Guess) is not int(correct_number):
            print("Sorry you didn't get it.")
    elif int(Guess) < int(correct_number):
        print("Now that number is too low.")
        Guess = input("Guess another number: \n")
        if int(Guess) == int(correct_number):
            print("That is correct!")
        elif int(Guess) is not int(correct_number):
            print("Sorry you didn't get it.")
elif int(Guess) < int(correct_number):
    print("That is too low.")
    Guess = input("Guess another number: \n")
    if int(Guess) == int(correct_number):
        print("You are correct!")
    elif int(Guess) > int(correct_number):
        print("Now you number is too high.")
        Guess = input("Guess another number: \n")
        if int(Guess) == int(correct_number):
            print("That is correct!")
        elif int(Guess) is not int(correct_number):
            print("Sorry you didn't get it.")
    elif int(Guess) < int(correct_number):
        print("That number is still too low.")
        Guess = input("Guess another number: \n")
        if int(Guess) == int(correct_number):
            print("That is correct!")
        elif int(Guess) is not int(correct_number):
            print("Sorry you didn't get it.")
