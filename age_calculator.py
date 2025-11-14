# Age Calculator
# Description: Simple Python program that calculates a person's age based on their birth year.

from datetime import date

print("Welcome to the Age Calculator")

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = date.today().year
age = current_year - birth_year

print(f"\n{name}, you are {age} years old in {current_year}")