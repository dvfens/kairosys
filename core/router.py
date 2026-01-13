def route(command: str) -> str:
    if "open" in command:
        return "OPEN"
    if "explain" in command:
        return "EXPLAIN"
    if "play" in command:
        return "PLAY"
    if "stop" in command:
        return "STOP"
    return "UNKNOWN"
