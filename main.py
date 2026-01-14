from voice.listener import listen
from voice.speaker import speak

WAKE_WORDS = [
    "kyrosis",
    "process",
    "roses",
    "cirrhosis",
    "viruses",
    "meiosis"
]

def is_wake_word(text):
    words = text.split()
    return words and words[0] in WAKE_WORDS


def main():
    speak("Kyrosis is online.")
    print("Kyrosis listening...")

    while True:
        text = listen()
        if not text:
            continue

        print("Heard:", text)

        if is_wake_word(text):
            print("WAKE WORD DETECTED")

            # 🔥 CRITICAL: exit listening loop BEFORE speaking
            break

    # Speak AFTER mic is fully released
    speak("I heard you. I am awake.")

    # Resume listening (loop again)
    main()


if __name__ == "__main__":
    main()
