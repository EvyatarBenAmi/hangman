def init_state(secret: str, max_tries: int) -> dict:
    play_data = { 
                "secret": secret,
                "display": [" _" * len(secret)],
                "guessed": set(),
                "wrong_guesses": 0,
                "max_tries": max_tries
                }
    return play_data
# print(init_state("stav", 5))

def validate_guess(ch: str, guessed:set[str]) -> tuple[bool, str]:

    if ch.isalpha and len(ch) == 1 :
        if ch not in guessed:
            return True , "The guess  was successful."
        else:
            return False , "The signal has already been received."
    else:
        return False , " invalid character was received."
# print(validate_guess("4",{"k"}))

def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["secret"]:
        return True
    else:
        return False
# print(apply_guess({"grt":25, "secret": "a"}, "a"))

def is_won(state: dict) -> bool:

    if "_" not in state["display"]:
        return True
    
def is_lost(state: dict) -> bool:

    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    