import random


def brain_even():
    numbers = random.randint(1, 10)

    print(f'Question: {numbers}')
    question = 'yes' if numbers % 2 == 0 else 'no'
    return numbers, question
