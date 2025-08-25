"""

Decimal to Binary Converter

This script takes a decimal (base-10) number as input
and converts it to its binary (base-2) equivalent using
a simple while loop.

Author: Karan Heera

Usage:
    Run the script and enter a decimal number when prompted.

Example:
    Input: 21
    Output: Binary is: 10101
    
"""


# Take input from the user and convert it to an integer
decimal = int(input("Enter Decimal No: "))

# Create an empty string to store the binary number
binary = ""

# Repeat the loop until the decimal number becomes 0
while decimal > 0:
    remainder = decimal % 2              # Get the remainder (0 or 1)
    binary = str(remainder) + binary     # Add the remainder to the left of the binary string
    decimal = decimal // 2               # Reduce the number by dividing it by 2

# Print the final binary result
print("Binary is:", binary)
