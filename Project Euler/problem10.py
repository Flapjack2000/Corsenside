"""
Zachary Williams
Problem 10: Summation of Primes
Find the sum of all the primes below two million (2,000,000).

Example:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
"""

def factor(n: int) -> list:
    # check for factors under sqrt(n)
    factors: list = [i for i in range(1, int(n**0.5) + 1) if not n/i % 1]

    # if (i) is a factor, then (n/i) must also be a factor
    # don't add duplicates from perfect squares
    factors.extend([int(n/f) for f in factors if (not n/f % 1) and (n/f not in factors)])

    return sorted(factors)

def check_prime(n) -> bool:
    return len(factor(n)) == 2

if __name__ == "__main__":
    two_mil: int = 2000000
    primes_below_two_mil = [n for n in range(1, two_mil) if check_prime(n)]

    answer = sum(primes_below_two_mil)
    print(answer)
