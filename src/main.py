import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from integrity import calculate_sha256, save_hash, verify_integrity


class FileIntegrityChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("File Integrity Checker")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        self.selected_file = None

        self.build_ui()

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="File Integrity Checker",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self.root,
            text="SHA-256 Cryptographic Hash Verification",
            font=("Arial", 11)
        )
        subtitle.pack(pady=(0, 25))

        file_frame = tk.Frame(self.root)
        file_frame.pack(pady=10)

        self.file_label = tk.Label(
            file_frame,
            text="No file selected",
            width=55,
            anchor="w"
        )
        self.file_label.pack(side="left", padx=10)

        select_button = tk.Button(
            file_frame,
            text="Select File",
            command=self.select_file,
            width=12
        )
        select_button.pack(side="right")

        self.hash_label = tk.Label(
            self.root,
            text="SHA-256: Not calculated",
            wraplength=580,
            justify="left",
            font=("Consolas", 10)
        )
        self.hash_label.pack(pady=25)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        register_button = tk.Button(
            button_frame,
            text="Register Baseline",
            command=self.register_file,
            width=20,
            height=2
        )
        register_button.pack(side="left", padx=10)

        verify_button = tk.Button(
            button_frame,
            text="Verify Integrity",
            command=self.verify_file,
            width=20,
            height=2
        )
        verify_button.pack(side="right", padx=10)

        self.status_label = tk.Label(
            self.root,
            text="Status: Waiting for file...",
            font=("Arial", 14, "bold")
        )
        self.status_label.pack(pady=35)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a file"
        )

        if file_path:
            self.selected_file = file_path

            self.file_label.config(
                text=Path(file_path).name
            )

            file_hash = calculate_sha256(file_path)

            self.hash_label.config(
                text=f"SHA-256:\n{file_hash}"
            )

            self.status_label.config(
                text="Status: File selected"
            )

    def register_file(self):
        if not self.selected_file:
            messagebox.showwarning(
                "No File",
                "Please select a file first."
            )
            return

        file_hash = save_hash(self.selected_file)

        self.status_label.config(
            text="Status: Baseline registered"
        )

        messagebox.showinfo(
            "Success",
            "File baseline hash has been registered."
        )

    def verify_file(self):
        if not self.selected_file:
            messagebox.showwarning(
                "No File",
                "Please select a file first."
            )
            return

        result, info = verify_integrity(self.selected_file)

        if result is None:
            self.status_label.config(
                text=f"Status: {info}"
            )
            messagebox.showwarning(
                "Verification Failed",
                info
            )

        elif result:
            self.status_label.config(
                text="Status: ✓ File integrity intact"
            )

            messagebox.showinfo(
                "Integrity Check",
                "The file has NOT been modified."
            )

        else:
            self.status_label.config(
                text="Status: ⚠ FILE MODIFIED"
            )

            messagebox.showwarning(
                "Security Warning",
                "The file has been modified!"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = FileIntegrityChecker(root)
    root.mainloop()