from Day14DATA import data
from typing import Dict, List
import random

print('''______  ______        ______              
___  / / /__(_)______ ___  /______________
__  /_/ /__  /__  __ `/_  __ \  _ \_  ___/
_  __  / _  / _  /_/ /_  / / /  __/  /    
/_/ /_/  /_/  _\__, / /_/ /_/\___//_/     
              /____/                      
______                                    
___  / _________      ______________      
__  /  _  __ \_ | /| / /  _ \_  ___/      
_  /___/ /_/ /_ |/ |/ //  __/  /          
/_____/\____/____/|__/ \___//_/           
                                          ''')

print("Welcome to the Higher Lower Game!")
print("You are given two options and you must guess who has a greater number "
      "of followers on Instagram.")


def generate_examples(datadict: List[Dict]) -> List[Dict]:
    dictA = random.choice(datadict)
    dictB = random.choice(datadict)

    while dictA == dictB:
        dictB = random.choice(datadict)

    return [dictA, dictB]


def generate_new_examples(datadict: List[Dict], examples: List[Dict]) -> List[Dict]:
    if same_num_followers(examples[0], examples[1]) or \
            examples[0]['follower_count'] > examples[1]['follower_count']:
        first_example = examples[0]
    else:
        first_example = examples[1]

    second_example = random.choice(datadict)

    while second_example == first_example:
        second_example = random.choice(datadict)

    return [first_example, second_example]


def print_template(person_dict: Dict) -> str:
    template = person_dict['name'] + ', ' + person_dict['description'] + \
               ' from ' + person_dict['country'] + '.'
    return template


def compare_followers(dictA: Dict, dictB: Dict) -> str:
    if dictA['follower_count'] >= dictB['follower_count']:
        return 'A'
    return 'B'


def same_num_followers(dictA: Dict, dictB: Dict) -> bool:
    if dictA['follower_count'] == dictB['follower_count']:
        return True


def game():
    score = 0
    examples = generate_examples(data)
    ans = True

    while ans:
        print(f"Compare A: {print_template(examples[0])}")
        print('''___    _________  
__ |  / /_  ___/  
__ | / /_____ \   
__ |/ / ____/ /__ 
_____/  /____/_(_)''')
        print(f"Against B: {print_template(examples[1])}")
        user_ans = input("Who has more followers? A/B: ").upper()
        if same_num_followers(examples[0], examples[1]):
            user_ans = 'A'

        if compare_followers(examples[0], examples[1]) != user_ans:
            ans = False
            print(f"Wrong! {examples[0]['name']} has "
                  f"{examples[0]['follower_count']} followers while "
                  f"{examples[1]['name']} has {examples[1]['follower_count']} "
                  f"followers.")
        else:
            score += 1
            print(f"Correct! {examples[0]['name']} has "
                  f"{examples[0]['follower_count']} followers while "
                  f"{examples[1]['name']} has {examples[1]['follower_count']} "
                  f"followers.")
            examples = generate_new_examples(data, examples)
            print('\n' * 10)

    print(f"Game over! You got {score} comparison(s) right.")


game()
