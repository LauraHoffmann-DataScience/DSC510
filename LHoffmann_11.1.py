# Course: DSC 510
# Assignment: 11.1
# Date: 5/22/2020
# Name: Laura Hoffmann
# Description: Cash register program to demonstrate use of object oriented programming with classes

# Must have a welcome message.
# Create one class called CashRegister.
# Have one instance method (addItem) with one parameter for price that also keeps track of items in your cart.
# Create two getter methods.
    # getTotal – returns totalPrice
    # getCount – returns the itemCount of the cart
# Create an instance of the CashRegister class.
# Create a loop which allows the user to continue to add items to the cart until they request to quit.
# Print the total number of items in the cart.
# Print the total $ amount of the cart.
# Output should be formatted as currency.

import locale

locale.setlocale(locale.LC_ALL, '')


class CashRegister:

    def __init__(self):
        self.price = 0
        self.count = 0

    def add_item(self, price):  # adds item to register
        self.price += price
        self.count += 1

    @property
    def get_total(self):  # return total price
        return self.price

    @property
    def get_count(self):  # return count of items
        return self.count

    def clear(self):  # reset register to zero
        self.price = 0


def main():
    welcome_message = "Welcome to the Store Cash Register!"
    length = len(welcome_message)
    print('-' * length)
    print(welcome_message)
    print('-' * length)
    register = CashRegister()
    looping = True
    while looping == True:
        item_price = input("Please input the price to add an item, 'c' to checkout, or 'e' to empty your cart: ")
        if item_price == 'c':
            print('- ' * 44)
            print("Your total price today is:", locale.currency(register.get_total))
            print("Your total number of items today is:", register.get_count)
            print("Thank you for shopping with us!")
            looping = False
        elif item_price == 'C':
            print('- ' * 44)
            print("Your total price today is:", locale.currency(register.get_total))
            print("Your total number of items today is:", register.get_count)
            print("Thank you for shopping with us!")
            looping = False
        elif item_price == 'e':
            (register.clear())
            print("You have emptied your cart.")
            looping = False
        elif item_price == 'E':
            (register.clear())
            print("You have emptied your cart.")
            looping = False
        else:
            try:
                item_price = float(item_price)
                register.add_item(item_price)
                print("Your current total is now at:", locale.currency(register.get_total))
                print("The number of items in your cart is currently:", register.get_count)
                print('- ' * 44)
                looping = True
            except:
                print("I'm sorry, we did not understand.")
                looping = True


if __name__ == "__main__":
    main()
