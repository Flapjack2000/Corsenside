"""
Zachary Williams
Problem 7: 10001st Prime
What is the 10001st prime number?

Example:
By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see
that the 6th prime is 13.
"""
def list_factors(n) -> list:
    """ Find all factors of a number n, including 1 and n. """

    # check for factors under sqrt(n)
    # (not n/i % 1) means (n/i % 1 == 0)
    factors: list = [i for i in range(1, int(n ** 0.5) + 1) if not n / i % 1]

    # if (i) is a factor, then (n/i) must also be a factor
    # don't add duplicates from perfect squares
    factors.extend([int(n / f) for f in factors if (not n / f % 1) and (n / f not in factors)])

    return sorted(factors)

def check_prime(n) -> bool:
    """ Check if a number n is prime. """
    if len(list_factors(n)) == 2:
        return True

if __name__ == "__main__":
    num_primes_found = 0
    i = 0
    while True:
        i += 1
        if check_prime(i):
            num_primes_found += 1
        if num_primes_found == 10001:
            break
    answer = i
    print(answer)
