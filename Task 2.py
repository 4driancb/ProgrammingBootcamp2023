"""
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.

Note that you will need to use the random library’s randint function.

Remember:
- Use functions to group code
- Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
- Check for invalid inputs, notifying the user and re-prompting for a valid input
"""

import random

def guess():
    number = random.randint(1, 100)

    while True:
        try:
            answer = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input! Please input an integer")
        else:
            if answer < 1 or answer > 100:
                print("Out of range!")
                continue
            elif answer > number:
                print("Lower!")
                continue
            elif answer < number:
                print("Higher!")
                continue
            else:
                print(f"Correct! The number is {number}")
                return


guess()
