import threading
import speech_recognition as sr

from core.router import route
from ui.tk_ui import KyrosisUI
from bridge.socket_server import UnityBridge


# =========================
# INIT
# =========================
recognizer = sr.Recognizer()
ui = KyrosisUI()
bridge = UnityBridge()


# =========================
# SPEECH LISTENING
# =========================
def listen():
    with sr.Microphone() as source:
        ui.set_status("🎤 Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        ui.set_status(f"Speech error: {e}")
        return None


# =========================
# MAIN LISTEN LOOP
# =========================
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
            bridge.send(response)   # 🔥 SEND TO UNITY
        else:
            ui.set_status("⏳ Waiting for wake word...")


# =========================
# START EVERYTHING
# =========================
threading.Thread(target=listen_loop, daemon=True).start()
ui.run()
