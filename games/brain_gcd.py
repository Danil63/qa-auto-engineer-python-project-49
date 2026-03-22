import random

from math import gcd     


def brain_gcd():
    first_term = random.randint(1, 100)
    second_term = random.randint(1, 100)

    print(f'Question: {first_term} {second_term}')
    numbers = f'{first_term} {second_term}'
    question = gcd(first_term, second_term)
    
    return numbers, str(question)