#!/usr/bin/env python3

def main():
    user_score = 0;
    add_points = 20;
    play_again = true;

    human_anatomy = [
            "What is the largest organ in the body?",
            "Where are the smallest muscles in the body found?",
            "Which is the only organ capable of regeneration?",
            "What does the orbital cavity contain?",
            "Which blood type is considered the universal donor?"
            ]

    american_history = [];

    user_name = input("Welcome to the Quiz-Me-Experience!  Please enter a username.\n-->").title()
    print(f"{user_name}, It's now time to pick a 'Quiz-Me' Category.")

    topic_choice = input("\nYour quiz will have 5 questions, you must get 3 correct to pass.\nSelect 1 for Human Anatomy, select 2 for American History.\n-->")

while play_again == true:

    if topic_choice == "1":
        print(f"Question 1: {human_anatomy[0]}")
        answer_one = input("\n-->").lower()
        if "skin" in answer_one:
            user_score += add_points 
            print("Correct!")
            print(f"\n {user_name}, your current score is {user_score}")
        else:
            print("Sorry, the correct answer was: skin");



main()
