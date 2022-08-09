import json
import pathlib
import os
from prompt_handler import show_prompt_for_questions
from enum import Enum

class firstStates(Enum):
    DISCOVER = "Discover new switcher devices"
    KNOWN_DEVICE = "I want to make something with known device"

data = [
    {
        "type": "list",
        "name": "action",
        "message": "What action do you want to perform?",
        "choices": [firstStates.DISCOVER.value, firstStates.KNOWN_DEVICE.value]
    }
]

def ask_first_question() -> dict:
    return show_prompt_for_questions(data)
        