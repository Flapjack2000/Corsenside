"""
Base Conversion Algorithm
Zachary Williams
"""

# Reference table for digits after 9
digit_table: dict = {
    10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", 16: "g", 17: "h", 18: "i", 19: "j", 20: "k",
    21: "l", 22: "m", 23: "n", 24: "o", 25: "p", 26: "q", 27: "r", 28: "s", 29: "t", 30: "u", 31: "v",
    32: "w", 33: "x", 34: "y", 35: "z", 36: "A", 37: "B", 38: "C", 39: "D", 40: "E", 41: "F", 42: "G",
    43: "H", 44: "I", 45: "J", 46: "K", 47: "L", 48: "M", 49: "N", 50: "0", 51: "P", 52: "Q", 53: "R",
    54: "S", 55: "T", 56: "U", 57: "V", 58: "W", 59: "X", 60: "Y", 61: "Z", 62: "!", 63: "@", 64: "#",
    65: "$", 66: "%", 67: "^", 68: "&", 69: "*", 70: "(", 71: ")", 72: "_", 73: "-", 74: "+", 75: "=",
    76: "`", 77: "~", 78: "[", 79: "]", 80: "{", 81: "}", 82: "|", 83: "/", 84: "\\", 85: "'", 86: '"',
    87: ",", 88: ".", 89: "<", 90: ">", 91: "?", 92: "Δ", 93: "µ", 94: "∑", 95: "δ", 96: "β", 97: "Ω",
    98: "ϴ", 99: "π"}

# Dynamically keeps track of the highest base allowed according to the digit_table
upper_limit: int = list(digit_table.keys())[-1] + 1

def change_base(num: int, base: int) -> str:

    # Check the validity of the inputs
    if base < 2 or base > upper_limit:
        return f"Base must be between 2 and {upper_limit}."

    if num % 1:
        return f"Number must be an integer."

    # Use the Base Conversion Algorithm, which itself employs the Division Algorithm,
    # to divide the decimal number by the new base and record the remainder. Continue by dividing the new quotient
    # by the base and recording the sequence of remainders until the quotient reaches 0. The new integer is the reversed sequence of remainders.
    remainders: str = ''
    while num != 0:

        # Find remainder
        remainder: int = (num % base)

        # Check if the remainder needs to be converted to a one digit symbol
        if remainder in digit_table.keys():
            remainder: str = digit_table[remainder]

        # Record the remainder
        remainders += (str(remainder))

        # Switch to the next quotient
        num //= base

    # Reverse the sequence and put it all together
    return remainders[::-1]

print(f"This program lets you convert a decimal integer to any base between 2 and {upper_limit}.\n"
      "Once you get past base 62 you'll start seeing symbols and greek letters, so it's kind of stupid and unreadable.\n"
      "Try to spell your name. 61101217 is Zach in base 100. Enter -1 to quit.\n")

# Run the program
while True:
    n: int = int(float(input("Enter a positive integer: ")))
    if n == -1:
        print("Thank you. Have a nice day.")
        break
    b: int = int(float(input("Enter a base: ")))
    if b == -1:
        print("Thank you. Have a nice day.")
        break

    print(change_base(n, b))
