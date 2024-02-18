import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import seaborn as sns
import random

def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

class DuplicateFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Duplicate Finder")
        self.root.geometry("400x300")
        self.root.configure(bg='#F0F0F0')
        self.root.resizable(False, False)

        self.main_frame = ttk.Frame(root, padding="10", relief='groove', borderwidth=5)
        self.main_frame.pack(expand=True, fill="both")

        self.label = ttk.Label(self.main_frame, text="Enter numbers (comma-separated):", background='#F0F0F0', font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.entry_numbers = ttk.Entry(self.main_frame, font=("Helvetica", 12))
        self.entry_numbers.pack(pady=10)

        self.find_duplicates_button = ttk.Button(self.main_frame, text="Find Duplicates", command=self.find_and_display_duplicates, style='TButton', cursor='hand2')
        self.find_duplicates_button.pack(pady=10)

        self.result_text = ScrolledText(self.main_frame, height=6, width=40, wrap=tk.WORD, font=("Helvetica", 12))
        self.result_text.pack(pady=10)

        self.style = ttk.Style()
        self.style.configure('TButton', font=("Helvetica", 12))

    def find_and_display_duplicates(self):
        try:
            input_numbers = [int(x) for x in self.entry_numbers.get().split(',')]
            duplicates = find_duplicates(input_numbers)

            self.result_text.delete(1.0, tk.END)
            if duplicates:
                self.result_text.insert(tk.END, f"Duplicates: {', '.join(map(str, duplicates))}")
                # Add a simple transition effect
                self.root.after(100, lambda: self.root.configure(bg='#D1F1E3'))
                self.root.after(200, lambda: self.root.configure(bg='#F0F0F0'))
            else:
                self.result_text.insert(tk.END, "No duplicates found.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DuplicateFinderApp(root)
    root.mainloop()
