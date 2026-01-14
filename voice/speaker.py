import pyttsx3
import time

_engine = None

def get_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty("rate", 170)
    return _engine


def speak(text: str):
    time.sleep(0.2)  # allow mic to fully release
    engine = get_engine()
    engine.say(text)
    engine.runAndWait()
