#!/usr/bin/env python3
round = 0
answer = " "
while round < 3 and answer != "Brian":
    round += 1
    answer = input('Finish the movie title, "Monty Pythons The life of _____ "')
    if answer.lower() == "brian":
        print("Correct!")
        break
    elif round == 3:
        print("Sorry the correct answer was Brian")
        break
    else:
        print("Sorry!, Please try again!")
