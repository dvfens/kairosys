import threading
import speech_recognition as sr


from core.router import route
from ui.tk_ui import KyrosisUI

recognizer = sr.Recognizer()
ui = KyrosisUI()

def listen():
    with sr.Microphone() as source:
        ui.set_status("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except:
        return None


def listen_loop():
    while True:
        text = listen()
        if not text:
            continue

        text = text.lower().strip()
        print("Heard:", text)

        ui.set_heard(text)

        response = route(text)

        if response:
            ui.set_status(f"🤖 Kyrosis: {response}")
        else:
            ui.set_status("⏳ Waiting for wake word...")


threading.Thread(target=listen_loop, daemon=True).start()
ui.run()
