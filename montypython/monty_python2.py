#!/usr/bin/env python3
round = 0
while True:
    round = round + 1
    print('Monty Python\s The Life of _____"')
    answer = input("Your Guess--->")
    if answer.lower() == "brian":
        print("Correct!")
        break
    elif round == 3:
        print("Sorry the correct answer was Brian")
        break
    else:
        print("Sorry!, Please try again!")

