#!/usr/bin/env python3

# Created by Yiyun Qin
# Created on March 2022
# This is the math program, comparing the number and 0


def main():
    # This function compares the number and 0

    # input
    number_compared = int(input("Enter the integer you want to check: "))

    # process & output
    print("")
    if number_compared > 0:
        print("{} is a positive number.".format(number_compared))
    elif number_compared < 0:
        print("{} is a negative number.".format(number_compared))
    else:
        print("{} is just 0!".format(number_compared))
    print("\nDone.")


if __name__ == "__main__":
    main()
