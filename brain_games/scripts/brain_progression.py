from games.brain_progression import brain_progression

from security.engine import engine


def main() -> None:
    print('What number is missing in the progression?')
    engine(brain_progression)