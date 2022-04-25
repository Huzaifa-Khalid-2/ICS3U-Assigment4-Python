#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the total cost of croissants with user input


import constants


def main():
    # This program calculates the total cost of the croissants with user input
    total = 0
    print("Croissants are ${0} each.".format(constants.CROISSANT_PRICE))

    # input
    number_of_croissants = input("\nHow many croissants would you like?: ")

    # process & ouput
    try:
        number_of_croissants = int(number_of_croissants)
        # if the user buys 6 or more croissants then they will get the tax off
        if number_of_croissants >= 6:
            total = number_of_croissants * constants.CROISSANT_PRICE
            print("\nThe total cost will be ${:,.2f} (no HST).".format(total))
        elif number_of_croissants < 0:
            print("\nYour number of croissants must be positive")
        else:
            total = (number_of_croissants * constants.CROISSANT_PRICE) * constants.HST
            print("\nThe total cost will be ${:,.2f} (with HST).".format(total))
    except (Exception):
        print("")
        print("Invalid Input, enter an integer you dunderhead.")
    print("\nDone.")


if __name__ == "__main__":
    main()
