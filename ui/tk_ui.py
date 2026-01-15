import tkinter as tk

class KyrosisUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kyrosis (Checkpoint-2)")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        title = tk.Label(
            self.root,
            text="KYROSIS",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=10)

        self.status_var = tk.StringVar(value="⏳ Waiting for wake word...")
        status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Segoe UI", 11)
        )
        status_label.pack(pady=10)

        self.heard_var = tk.StringVar(value="Heard: —")
        heard_label = tk.Label(
            self.root,
            textvariable=self.heard_var,
            font=("Segoe UI", 10),
            fg="gray"
        )
        heard_label.pack(pady=5)

    def set_status(self, text: str):
        self.status_var.set(text)

    def set_heard(self, text: str):
        self.heard_var.set(f"Heard: {text}")

    def run(self):
        self.root.mainloop()
