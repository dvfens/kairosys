from core.detector import is_wake_word, is_greeting

def route(text: str):
    if not is_wake_word(text):
        return None

    if is_greeting(text):
        return "Hi. What would you like me to do?"

    return "Yes. I'm listening."
