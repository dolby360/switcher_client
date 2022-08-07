import json
import pathlib
import os
from prompt_handler import show_prompt_for_questions
CURR_DIR = pathlib.Path(__file__).resolve().parent
FIRST_QUESTION_PATH = os.path.join(CURR_DIR, "questions", "first_question.json")

def ask_first_question():
    with open(FIRST_QUESTION_PATH, 'r') as first_q:
        show_prompt_for_questions(json.load(first_q))