from PyInquirer import prompt, Separator
from examples import custom_style_2
import json
import pathlib
import os

CURR_DIR = pathlib.Path(__file__).resolve().parent
FIRST_QUESTION_PATH = os.path.join(CURR_DIR, "questions", "first_question.json")  

def main():
    with open(FIRST_QUESTION_PATH, 'r') as first_q:
        questions = json.load(first_q)
        answers = prompt(questions, style=custom_style_2)

if __name__ == "__main__":
    main()