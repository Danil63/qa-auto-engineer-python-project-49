import random                                                                                                                                           
                                                                                                                                                          
   
def brain_calc():                                                                                                                                       
    first_term = random.randint(1, 10)
    second_term = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
                                                                                                                                                          
    numbers = f'{first_term} {operator} {second_term}'
    print(f'Question: {numbers}')                                                                                                                       
                  
    if operator == '+':
        question = first_term + second_term
    elif operator == '-':
        question = first_term - second_term                                                                                                             
    else:
        question = first_term * second_term                                                                                                             
                  
    return numbers, str(question)


