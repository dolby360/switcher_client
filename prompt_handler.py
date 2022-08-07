from PyInquirer import prompt
from examples import custom_style_2

def show_prompt_for_questions(questions: dict):
    return prompt(questions, style=custom_style_2)