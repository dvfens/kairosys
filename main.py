from voice.listener import listen
from voice.speaker import speak
from core.router import route

WAKE_WORD = "kyrosis"

def main():
    speak("Kyrosis is online.")
    print("Kyrosis listening...")

    while True:
        text = listen()
        if not text:
            continue

        print("Heard:", text)

        if WAKE_WORD in text:
            speak("Yes?")
            command = listen()
            print("Command:", command)

            intent = route(command)
            speak(f"I understood command type {intent}")

if __name__ == "__main__":
    main()
