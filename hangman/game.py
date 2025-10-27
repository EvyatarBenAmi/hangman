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
