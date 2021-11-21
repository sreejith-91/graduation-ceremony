"""
## Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or
reduce the fraction to decimal

Test cases:

for 5 days: 14/29

for 10 days: 372/773
"""
import re

from itertools import product


# Function to check four or
# more consecutive
# leaves taken
def is_invalid_combination(combination_string):
    # Regex to check 4 or more consecutive identical leave taken
    regex = "([L])\\1\\1\\1"
    p = re.compile(regex)
    res = False
    if str is None:
        return False
    if re.search(p, combination_string):
        res = True
    return res


def generate_combination(n):
    """
    Generate all the combination, calculates total combinations, generate the invalid combinations,
    calculate probability
    :param n:
    :return:
    """
    combination_lst = ['P', 'L']
    total_combinations = 2 ** n
    total_invalid = 0
    probability = 0
    for cb in product(combination_lst, repeat=n):
        comb = ''.join(cb)
        if is_invalid_combination(comb):
            total_invalid += + 1
        elif comb.endswith('L'):
            probability += 1
    total_valid_ways = total_combinations - total_invalid
    print(f"For {n} days: {probability}/{total_valid_ways}")


if __name__ == '__main__':
    no_of_days = input("Enter number of days: ")
    try:
        no_of_days = int(no_of_days)
        generate_combination(no_of_days)
    except IOError as e:
        print(f"Exception: {e}")
