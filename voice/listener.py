import speech_recognition as sr
import time

def listen(timeout=5, phrase_time_limit=4):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )
        except sr.WaitTimeoutError:
            return ""

    try:
        result = recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        result = ""
    except sr.RequestError:
        result = ""

    # IMPORTANT: allow microphone to fully release
    time.sleep(0.1)
    return result
