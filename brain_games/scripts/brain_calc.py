from security.engine import engine

from games.brain_calc import brain_calc


def main():
    print("What is the result of the expression?")
    engine(brain_calc)

