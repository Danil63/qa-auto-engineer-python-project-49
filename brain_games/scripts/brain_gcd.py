from games.brain_gcd import brain_gcd
from security.engine import engine

def main() -> None:
    print('Find the greatest common divisor of given numbers.')
    engine(brain_gcd)