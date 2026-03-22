import random


def brain_progression():
    first_term = random.randint(1, 10)
    step = random.randint(2, 5)
    hidden_index = random.randint(0, 5)
    progression = []

    for i in range(6):
        progression.append(first_term + step * i)

    question = str(progression[hidden_index])
    progression[hidden_index] = '..'

    numbers = ' '.join(str(x) for x in progression)
    print(f'Question: {numbers}')

    return numbers, question
