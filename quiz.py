from random import choice
import random

name = input("Enter your name : ")

class Question:
     def __init__(self,prompt,answer):
            self.prompt = prompt
            self.answer = answer         
            
            
question_prompts = open('questions.txt','r')
#question_prompts.seek(0,0)
content = question_prompts.read()


questions = [
    Question(content[1:124],"c"),
    Question(content[124:274],"d"),
    Question(content[274:579],"b"),
    Question(content[579:719],"c"),
    Question(content[719:811],"a"),
    Question(content[811:983],"d"),
    Question(content[983:1051],"a"),
    Question(content[1051:1231],"a"),
    Question(content[1231:1375],"b"),
    Question(content[1375:1541],"b"), 
]                          
random.shuffle(questions)
             

def run_quiz(questions):
    score=0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
             score += 1
    print(f"Hey!",name, "you got" ,score, "out of", len(questions))
run_quiz(questions)  