#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_number = number % 10
else:
    last_number = number % -10
used_string = "Last digit of"
if last_number > 5:
    print(f"{used_string} {number} is {last_number} and is greater than 5")
elif last_number < 6 and last_number != 0:
    print(f"{used_string} {number} is {last_number} and is less than 6 and not 0")
else:
    print(f"{used_string} {number} is {last_number} and is 0")
