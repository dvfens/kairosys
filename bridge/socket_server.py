import socket
import threading

HOST = "127.0.0.1"
PORT = 5050

class UnityBridge:
    def __init__(self):
        self.conn = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen(1)
        print(f"[Bridge] Waiting for Unity on {HOST}:{PORT}...")

        threading.Thread(target=self._accept_client, daemon=True).start()

    def _accept_client(self):
        self.conn, addr = self.server.accept()
        print(f"[Bridge] Unity connected from {addr}")

    def send(self, message: str):
        if self.conn:
            try:
                self.conn.sendall((message + "\n").encode("utf-8"))
            except Exception as e:
                print("[Bridge] Send failed:", e)
