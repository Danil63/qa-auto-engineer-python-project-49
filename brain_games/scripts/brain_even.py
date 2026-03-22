from security.engine import engine
from games.brain_even import brain_even


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine(brain_even)
