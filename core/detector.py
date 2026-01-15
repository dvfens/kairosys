from core.wake_words import WAKE_WORDS, GREETINGS


def is_wake_word(text: str) -> bool:
    return any(word in text for word in WAKE_WORDS)

def is_greeting(text: str) -> bool:
    return any(greet in text for greet in GREETINGS)
