import prompt

def welcome_user() -> None:
    name = prompt.string('May I have your name? ')
    welcome_name = print(f'Hello, {name}!')
    return welcome_name

