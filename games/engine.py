import random
import prompt
from brain_games.cli import welcome_user

def engine(brain_even) -> None:                                                                                              
    name = welcome_user()                                                                                                    
                                                                                                                               
    for _ in range(3):                                                                                                       
        numbers, question = brain_even()                                                                                     
        user_response = prompt.string("Your answer: ")
                                                                                                                               
        match user_response:
            case x if x == question:                                                                                         
                print("Correct!")
            case _:
                print(f"'{user_response}' is wrong answer ;(. Correct answer was '{question}'.")
                print(f"Let's try again, {name}!")                                                                           
                return
                                                                                                                               
    print(f"Congratulations, {name}!")
          

