from first_question import ask_first_question

class stateGen:
    def __init__(self) -> None:
        self.state_list = []

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

def main():
    state_manager = stateGen()
    for state in state_manager:
        state()
        
if __name__ == "__main__":
    main()