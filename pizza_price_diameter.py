#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the price of a pizza


import constants


def main():
    # this function calculates the cost of pizza

    # input
    diameter = int(
        input("Enter the diameter of the pizza you would " + "like (inch): ")
    )

    # process
    sub_total = constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is ${1:,.2f}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
