import random


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def brain_prime():
    number = random.randint(1, 50)
    print(f'Question: {number}')
    question = 'yes' if is_prime(number) else 'no'
    return number, question
