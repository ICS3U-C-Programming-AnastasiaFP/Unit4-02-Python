# Copyright by : Anastasia Friedenstein Patino
# Created on : November.11, 2023
# Program that determines the factorial of a while number

user_num_as_string = input("Enter a whole number: ")

try:
    user_num_int = int(user_num_as_string)
    factorial = 1
    counter = user_num_int

    while counter > 1:
        factorial *= counter
        counter -= 1

    print(f"Factorial of {user_num_int} is {factorial}")
except:
    print("Enter a valid whole number.")
