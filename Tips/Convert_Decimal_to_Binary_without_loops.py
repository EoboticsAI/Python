"""
Decimal to Binary Converter using Python's built-in bin() function.

This script takes a decimal (base-10) number as input from the user
and prints its binary (base-2) equivalent. It uses the bin() function
and removes the '0b' prefix using string slicing.

Usage:
    Run the script and enter any whole number when prompted.

Example:
    Input: 10
    Output: Binary is: 1010
"""

# Decimal Number to Binary Number Converter without using loops

decimal_num = int(input("Enter Decimal No: "))
print("Binary No is:", bin(decimal_num)[2:])



#Happy Coding!
