"""
Problem 1: Multiples of 3 or 5
Find the sum of all the multiples of 3 or 5 below 1000.

Example:
If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
"""

# Find multiples of target_nums below bound
def multiples_below_bound(target_nums: list, bound: int) -> list:
    multiples = []
    for i in range(1, bound):
        for j in target_nums:
            if i%j == 0:
                multiples.append(i)
    return list(set(multiples))

if __name__ == '__main__':
    print(multiples_below_bound([3, 5], 1000))
    answer = sum(multiples_below_bound([3, 5], 1000))
    print(answer)
