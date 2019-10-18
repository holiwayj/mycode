#!/usr/bin/env python3
char_name = input("Which character would you like to know about? (Flash, Batman or Superman?): ")
char_stat = input("Which statistic would you lkke to know about? (Strength, Speed or Intelligence?: ")
hero_dict = {"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength" : "Lowest"}, "Batman" :{"Speed": "Slowest", "Intelligence":"Highest", "Strength":"Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}}
print(f"The Hero, {char_name}'s {char_stat} is {hero_dict[char_name][char_stat]}")
