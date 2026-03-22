import random

from math import gcd     


def brain_gcd():
    first_term = random.randint(1, 100)
    second_term = random.randint(1, 100)

    numbers = print(f'{first_term} {second_term}')
    question = gcd(first_term, second_term)
    
    return numbers, str(question)