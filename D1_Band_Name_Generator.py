"""
PROJECT: BAND NAME GENERATOR
Description :
1. Create a greeting for your Program
2.Ask the user for city that they grew up in and store it in a
  variable
3.Ask the user for the name of a pet and store it in a Variable.
4.Combine the name of their city and pet and show them their
  band name
"""
print("Welcome to Band Name Generator")
cityname = input("Enter your City Name :\n")
pet_name = input("Enter your Pet Name :\n")
Combined = (cityname + pet_name)
print("Your Band Name is : " + Combined)
