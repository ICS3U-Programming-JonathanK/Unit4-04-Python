#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May 26 2021
# This program asks the user to guess a number between 0 to 9
# and tells the user if the guess is right or wrong

import random


def main():
    # generate a number between 0 to 9
    correct_guess = random.randint(0, 9)
    # uses a while loop to continue a sequence of gettting the right answer
    while True:
        # get the user number as a string
        user_number_string = input("Enter a whole number between 0 to 9: ")
        try:
            user_number_int = int(user_number_string)
        except ValueError:
            print("")
            print("Please enter a valid number")

        else:
            if user_number_int != correct_guess:
                print("")
                print("You are not correct. Please try again!")
                print("")
            else:
                print("")
                print("You are correct. Thank you for playing")
                print("")
                break


if __name__ == "__main__":
    main()
