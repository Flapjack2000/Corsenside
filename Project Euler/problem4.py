"""
Zachary Williams
Problem 4: Largest Palindrome Product
Find the largest palindrome made from
the product of two 3-digit numbers.

Example:
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 * 99.
"""

def rev(string: str) -> str:
    """ Reverses a string with string slicing. """
    return string[::-1]

def check_palindrome(text: int | str) -> bool:
    """
    Checks if a word or number is a palindrome
    like 7, "racecar", 8008, "eye", 12321, and "tattarrattat".
    """
    if str(text) == rev(str(text)):
        return True
    else:
        return False

if __name__ == '__main__':
    # 3-digit numbers are from 100 to 999
    three_digit_nums: list = [i for i in range(100, 1000)]

    # loop over the 3-digit numbers and find their products, then check for palindromes
    palindromes: list = [(a * b) for a in three_digit_nums for b in three_digit_nums if check_palindrome(a * b)]

    largest_palindrome: int = max([int(pal) for pal in palindromes])

    answer = largest_palindrome
    print(answer)
