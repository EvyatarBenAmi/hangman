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

def validate_guess(ch: str, state: dict) -> tuple[bool, str]:

    if ch.isalpha and len(ch) == 1 :
        if ch in state["secret"] and ch not in state["guessed"]:
            return True, "wow you good!"
        elif ch  in state["guessed"]:
            return False, "this word was used."
    else:
        return False, "Opss try again."
# print(validate_guess("4",{"k"}))

def apply_guess(state: dict, ch: str) -> bool:
    if ch in state["secret"]:
        return True
    else:
        return False
# אופציונלי להוסיף פה המשך פעולות בהסתמך תשובה מתקבלת
# print(apply_guess({"grt":25, "secret": "a"}, "a"))

def is_won(state: dict) -> bool:

    if "_" not in state["display"]:
        return True
    return False
    
def is_lost(state: dict) -> bool:

    if state["wrong_guesses"] >= state["max_tries"]:
        return True
    
def render_display(state: dict, ch: str) -> str:

    for i in range(len(state["display"])):

        if state["secret"][i] == ch:
            state["display"][i] = ch

    return state["display"]
# print(render_display({"secret":"Hello","display":["_","_","_","_","_"]},"o"))

def render_summary(state: dict) -> str:
    return state["secret"], state["gussed"]
