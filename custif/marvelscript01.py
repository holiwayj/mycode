#!/usr/bin/env python3
#
while True:
    age = input("How old are you? ")
    age = int(age)
    if age <= 15 or age >= 60:
        print("Come on, tell the truth next time")
        break
    sex = input("Are you male or female? ")
    trait = input("Which trait describes you the most? Strong, Agile, Intelligent, or Crafty? ")
    if trait.lower() != "strong" and trait.lower() != "agile" and trait.lower() != "intelligent" and trait.lower() != "crafty":
        print("Please try again with an appropriate answer")
        break
    if age < 25 and sex.lower() == "male":
        print("Congratulations! You are Spiderman! Protect the city Web-Slinger!")
        break
    if age < 25 and sex.lower() == "female":
        print("Congratulations! You are the X-Man, Rogue!. Have a great day sugah!")
        break
    if age < 25 and sex.lower() != "male" and sex.lower() != "female":
        print("Congratulations! you get to be Deadpool.")
        break
    if age > 50 and sex.lower() == "male":
        print("Congratulations old man!, You're Cable! Time hopping bad ass!")
        break
    if age > 50 and sex.lower() == "female":
        print("Congratulations!, youre Madame Web!, You are literally the oldest female character I could think of!")
        break
    if age >= 25 and sex.lower() == "male" and trait.lower() == "intelligent":
        print("Congratulations!  Youre Mr. Fantastic! Good going stretcho!")
        break
    if age >= 25 and sex.lower() == "male" and trait.lower() == "strong":
        print("Congratulatins! Youre the Incredible Hulk! We wont like you when youre angry!")
        break
    if age >= 25 and sex.lower() == "male" and trait.lower() == "agile":
        print("Congratulations! You are Spiderman! Protect the city Web-Slinger!")
        break
    if age >= 25 and sex.lower() == "male" and trait.lower() == "crafty":
        print("Congratulations!,You are Frank Castle, the Punisher!, You are the Judge, Jury and Executioner!")
        break
    if age >= 25 and sex.lower() == "female" and trait.lower() == "intelligent":
        print("Congratulations!, You are Captain Marvel!, Protector of the Galaxy!")
        break
    if age >= 25 and sex.lower() == "female" and trait.lower() == "strong":
        print("Congratulations!, You are the Sensational She-Hulk! Like your cousin, you are a force to be reckoned with!")
        break
    if age >= 25 and sex.lower() == "female" and trait.lower() == "agile":
        print("Congratulations! you are the super-spy and Avenger, Black Widow!")
        break
    if age >= 25 and sex.lower == "female" and trait.lower() == "crafty":
        print("Congratulations! you are the X-woman, Storm! The weather is yours to command, and as a bonus, you have great thief skills!")
        break
    else:
        print("If you're not going to play by the rules, maybe you should go read DC Comics")
        break
