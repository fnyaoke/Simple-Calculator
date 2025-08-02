"""
Simple Calculator Program
Author: Florence Nyaoke
Date: 2025-08-01

Description:
This program asks the user to input two numbers and a mathematical operation
(addition, subtraction, multiplication, or division). It then performs the
requested operation and prints the result in a readable format.

"""
# Ask the user to input the first number
num1 = input("Enter the first number: ")

# Ask the user to input the second number
num2 = input("Enter the second number: ")

# Ask the user to input the operation (+, -, *, /)
operation = input("Enter the operation (+, -, *, /): ")

# Convert the input strings to float to allow decimals
try:
    num1 = float(num1)
    num2 = float(num2)

 

