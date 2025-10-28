# from hangman.data.words import word
from hangman.words import choose_secret_word
from hangman.game import init_state, validate_guess, render_display, is_won, is_lost
from hangman.io import print_status, prompt_guess, print_result

word = ["בננה", "תפוח", "חציל", "עגבניה", "מלפפון", "מחשב", "עכבר", "מקלדת", "מסך", "טלפון",
"חלון", "דלת", "קיר", "שולחן", "כיסא", "מחברת", "עט", "עיפרון", "תיק", "ספר",
"אוטובוס", "מכונית", "מטוס", "סירה", "אופניים", "רכבת", "כביש", "מפה", "עיר", "כפר",
"מדבר", "יער", "ים", "הר", "שלג", "גשם", "שמש", "ירח", "כוכב", "שמיים",
"חולצה", "מכנסיים", "נעליים", "גרביים", "מעיל", "כובע", "צעיף", "מטריה", "שעון", "משקפיים",
"חתול", "כלב", "דג", "ציפור", "סוס", "כבשה", "עז", "פרה", "תרנגולת", "ברווז",
"נמר", "פיל", "קוף", "אריה", "דוב", "גמל", "שועל", "זאב", "תן", "ינשוף",
"פרח", "עלה", "עץ", "שיח", "דשא", "אבן", "נהר", "אגם", "מפלים", "מדורה",
"מים", "חול", "אדמה", "שמיים", "רוח", "ברק", "ענן", "סערה", "קשת", "שלולית",
"רופא", "מורה", "נהג", "כבאי", "שוטר", "חייל", "טבח", "חקלאי", "אופה", "מנקה",
"צייר", "מוזיקאי", "נגר", "חשמלאי", "מדען", "סופר", "מהנדס", "צלם", "תלמיד", "מאמן",
"שמחה", "עצב", "פחד", "אהבה", "כעס", "התרגשות", "שעמום", "תקווה", "דאגה", "שלווה",
"לחם", "גבינה", "ביצה", "חמאה", "שוקולד", "עוגה", "גלידה", "קפה", "תה", "פיצה",
"סוכר", "מלח", "פלפל", "בצל", "שום", "קמח", "אורז", "מרק", "חלב", "עוף",
"אוניה", "רכב", "אופנוע", "מסוק", "מטען", "נמל", "תחנה", "כביש", "מחלף", "מנהרה",
"בית", "בניין", "מדרגות", "קומה", "גג", "חדר", "מטבח", "אמבטיה", "שירותים", "סלון"]

def play(words: list[str], max_tries: int =10 ) -> None:
    singel_word = choose_secret_word(words)
    user_card = init_state(singel_word, max_tries)
    
    cuonter = True
    while cuonter is True: 
        print_status(user_card)
        user_choice = prompt_guess()
        validate = validate_guess(user_choice, user_card)
        if validate[0] is True:
            user_card["wrong_guesses"] += 1
            user_card["guessed"].add(user_choice)
            render_display(user_card, user_choice)
            print(validate[1])
        else:
            user_card["wrong_guesses"] += 1
            print(validate[1])

        if is_won(user_card) is True:
            cuonter = False
            print("You won!")
            print_result(user_card)
        if is_lost(user_card) is True:
            cuonter = False
            print("Opss you losing.")
            print_result(user_card)

    return

play(word)


