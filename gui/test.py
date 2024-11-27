import tkinter as tk
from tkinter import messagebox

class YouTubeSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Yt Search")
        self.root.geometry("400x200")

        # Title Label
        self.title_label = tk.Label(root, text="Yt Search", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Search Bar Frame
        search_frame = tk.Frame(root)
        search_frame.pack(expand=True)

        # URL Entry
        self.url_entry = tk.Entry(search_frame, width=40)
        self.url_entry.pack(pady=10)
        self.url_entry.insert(0, "Enter YouTube URL here")
        self.url_entry.bind("<FocusIn>", self.on_entry_click)
        self.url_entry.bind("<FocusOut>", self.on_focus_out)

        # Search Button
        search_button = tk.Button(search_frame, text="Search", command=self.search_youtube)
        search_button.pack(pady=5)

    def on_entry_click(self, event):
        """Remove default text when entry is clicked"""
        if self.url_entry.get() == "Enter YouTube URL here":
            self.url_entry.delete(0, tk.END)
            self.url_entry.config(fg='black')

    def on_focus_out(self, event):
        """Restore default text if no input"""
        if self.url_entry.get() == "":
            self.url_entry.insert(0, "Enter YouTube URL here")
            self.url_entry.config(fg='gray')

    def search_youtube(self):
        """Placeholder method for YouTube URL search"""
        url = self.url_entry.get()
        if url and url != "Enter YouTube URL here":
            messagebox.showinfo("Search", f"Searching for: {url}")
        else:
            messagebox.showwarning("Error", "Please enter a valid YouTube URL")

