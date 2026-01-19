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

## Checkpoint-3a: Python → Unity Bridge (Text Only)

### Status
✅ Completed (Python side)

### Description
In this checkpoint, the Python core of Kyrosis is extended with a socket-based bridge that allows communication with a Unity client. At this stage, **only text messages are transmitted**, not audio or microphone data.

Python acts as the **server**, while Unity will act as the **client** in later checkpoints.

---

### What Works
- Python socket server initialized on `localhost`
- Unity-ready communication channel (TCP)
- Kyrosis sends **response text only** after wake-word detection
- No dependency on Unity being active (safe startup)
- Existing Tkinter debug UI remains functional

---

### What Is Explicitly NOT Included
- ❌ Unity client connection (handled in Checkpoint-3b)
- ❌ Voice / Text-to-Speech
- ❌ Audio streaming or microphone sharing
- ❌ Spatial UI or avatar rendering

---

### Architecture (Checkpoint-3a)

```text
Microphone
   ↓
Python (Speech Recognition + Logic)
   ↓
Text Response
   ↓
Socket Server (localhost)
   ↓
[Unity client – not connected yet]
```

