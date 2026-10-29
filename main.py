from rich.console import Console
console = Console
print("whats the best CMS?")
print("A: Wordpress")
print("B: joomla")
print("c: Drupal")
print("B: headless")
user_answer: str = input("your choice:").strip().upper()
if user_answer == "A":
    print("Correct")
else:
    print("Incorrect")
questions=[
    ("whats the best CMS?",["A:Wordpress","B:Joomla","C:Drupal","D:Headless"],"A"),
    ("whats the best programming language?",["A:Wordppress","B:Javascript","C:Java","D:C++"],"B"),
    ("whats the best CMS?",["A:Mysquol","B:Javascript","C:mangoDB","D:sQlite"],"c")

]

while True:
    user_input: str = input("Do you want to start the quiz? (yes/no):").strip().lower()
    if user_input == "yes":
        break
    elif user_input=="no":
        print("Existing the quiz. Goodbye!")
        exit()
    else:
        print("invalid input. please enter 'yes or 'no'.")

def play_quiz():
    score=0
    BONUS=10
    user_corrects=0
    PENALTY=3
    for question,options,correct_answer in questions:
        print(questions)
    for option in options:
        print(option)
    user_answer: str = input("your choice:").strip().upper
    if user_answer == correct_amswer:
        print("Correct")
        scoret+=BONUS
        user_corrects +=1
    else:
        print("Incorrect")

        score -= PENALTY
        score=3
    return score,user_corrects
def show_results():
    print(f"your final score is :{score}")
    print(f"your answerd{user_corrects} quesrtions correctly.")
    print(f"percentage:{user_corrects /len(questrions)*100}")

    while True:
        if show_menu():
            break
    score,user_corrects= play_quiz()
    show_results(score, user_corrects)


