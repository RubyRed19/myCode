#!/usr/bin/env python3
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
#question prompts with answer choices for quiz
questions_prompt = [
            "What is the largest organ in the body? \n(a) heart \n(b) stomach \n(c) intestines \n(d) skin\n->",
            "Where are the smallest muscles in the body found? \n(a) eyes \n(b) ears \n(c) toes \n(d) nose\n-> ",
            "Which is the only organ capable of regeneration? \n(a) kidney \n(b) liver \n(c) spleen \n(d) heart\n->",
            "What does the orbital cavity contain? \n(a) eyes \n(b) teeth \n(c) intestine \n(d) stomach\n->",
            "Which is the longer of the two bones in the forearm? \n(a) ulna \n(b) humerous \n(c) radius \n(d) femur\n->"
            ]
#questions with correct answer
questions = [
          Question(questions_prompt[0], "d"),
          Question(questions_prompt[1], "b"),
          Question(questions_prompt[2], "b"),
          Question(questions_prompt[3], "a"),
          Question(questions_prompt[4], "a"),
        ];
#output to users, game intro
user_name = input("Welcome to the Quiz-Me-Experience!  Please enter a username.\n-->").title()
print(f"{user_name}, it's now time to pick a 'Quiz-Me' Category.")

topic_choice = input("\nYour quiz will have 5 questions on human anatomy. Press any key to continue.\n-->")

#logic for the quiz 
def main(questions):
    user_score = 0
    play_again = True

    for question in questions:
        while play_again == True:
            answer = input(question.prompt)
            if answer == question.answer:
                user_score += 20
                print(f"Correct! {user_name} your score is {user_score}")
                break
            elif answer == "" or answer not in ["a", "b", "c", "d"]:
                print("You must select one of the answer choices!")
            elif answer != question.answer:
                print(f"Sorry, the correct answer was {question.answer}")
                break
        print(f"{user_name} your final score was {user_score}")

if __name__ = "__main__":
    main(questions)
