import tkinter as tk
from tkinter import Label, Entry, Button, ttk

def reverse_string(input_string):
    return input_string[::-1]

def on_reverse_button_click():
    input_text = entry.get()
    reversed_text = reverse_string(input_text)
    result_label.config(text=f"Reversed String: {reversed_text}")

# Create the main tkinter window
root = tk.Tk()
root.title("String Reversal")
root.geometry("300x200")
root.configure(bg="#f2f2f2")

# Create and place ttk widgets with improved styling
label = ttk.Label(root, text="Enter a string:", background="#f2f2f2", font=("Helvetica", 12))
label.pack(pady=10)

entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=10)

# Change the button style for better visibility
style = ttk.Style()
style.configure("TButton", background="#3498db", foreground="#2c3e50", font=("Helvetica", 12))

reverse_button = ttk.Button(root, text="Reverse", command=on_reverse_button_click, style="TButton")
reverse_button.pack(pady=15)

result_label = ttk.Label(root, text="Reversed String:", background="#f2f2f2", font=("Helvetica", 12))
result_label.pack()

# Start the GUI main loop
root.mainloop()
