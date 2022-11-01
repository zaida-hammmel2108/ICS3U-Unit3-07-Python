#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program determines if you're eligible to date


def main():
    # this function uses compound boolean statements

    # input
    age_number = input("Enter your age: ")
    print("")

    # process & output
    try:
        age_number = int(age_number)
        if age_number >= 25 and age_number <= 40:
            print("You are an acceptable age.")
        else:
            print("You aren't an acceptable age.")
    except ValueError:
        print("That is not a valid input.")


if __name__ == "__main__":
    main()
