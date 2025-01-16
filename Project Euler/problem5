"""
Zachary Williams
Problem 6: Sum Square Difference
Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.

Example:
The sum of the squares of the first ten natural numbers is:
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is:
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence, the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.
"""

if __name__ == "__main__":
    sum_of_squares = sum([i**2 for i in range(1, 101)])

    square_of_sum = sum([i for i in range(1, 101)]) ** 2

    answer = abs(sum_of_squares - square_of_sum)
    print(answer)

