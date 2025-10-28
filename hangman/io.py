def prompt_guess() -> str:
    return input(str("Please enter a letter to guess: "))
    # return "ג"
def print_status(state: dict) -> None:

    print(f"this is a letter: {state["display"]} \n this is a letter guessed: {state["guessed"]} \n remaining guesses: {state["max_tries"] - state["wrong_guesses"]}")

def print_result(state: dict) -> None:
    
    print(f"The word: {state["secret"][::-1]} \n Guessed letters: {state["guessed"]} \n Number of attempts: {state["wrong_guesses"]}")