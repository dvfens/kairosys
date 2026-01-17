# Kyrosis

Kyrosis is a voice-based AI assistant project focused on building a clean, modular core before adding spatial UI and voice output.

---

## Current Status: Checkpoint-2

### Features Implemented
- Continuous speech listening
- Robust wake-word detection with phonetic tolerance
- Command routing logic
- Modular project structure
- Tkinter-based debug UI (temporary)

---

## Architecture (Checkpoint-2)
- Core logic handled in Python
- Wake-word and command detection separated from UI
- UI layer used only for debugging and visibility

---

## Project Structure

```text
kyrosis/
├── main.py
├── core/
│   ├── wake_words.py
│   ├── detector.py
│   └── router.py
├── ui/
│   └── tk_ui.py

```



---

## Roadmap
- Checkpoint-3: Python → Unity communication
- Checkpoint-4: Unity-based voice output
