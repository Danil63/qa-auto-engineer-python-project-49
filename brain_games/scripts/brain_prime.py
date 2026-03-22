from security.engine import engine

from games.brain_prime import brain_prime


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine(brain_prime)
