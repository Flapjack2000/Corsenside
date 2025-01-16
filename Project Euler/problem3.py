"""
Zachary Williams
Problem 3: Largest Prime Factor
What is the largest prime factor of the number 600851475143?

Example:
The prime factors of 13195 are 5, 7, 13, and 29.
"""
import math

def list_factors(n: int) -> list:
    # Check for factors under sqrt(n)
    factors = [i for i in range(1, int(math.sqrt(n)) + 1) if n / i % 1 == 0]

    # If (i) is a factor, then (n/i) must also be a factor
    # Don't add duplicates from perfect squares
    factors.extend([int(n / f) for f in factors if (n / f % 1 == 0) and (n / f not in factors)])

    return sorted(factors)

def check_prime(n) -> bool:
    """ Check if a number n is prime. """
    return True if len(list_factors(n)) == 2 else False
        
def list_prime_factors(n) -> list:
    """ Find all prime factors of a number n, including 1 and n (if n is prime). """
    return [f for f in list_factors(n) if check_prime(f)]

def largest_prime_factor(n) -> int:
    return max(list_prime_factors(n))

if __name__ == '__main__':
    answer = largest_prime_factor(600851475143)
    print(answer)
