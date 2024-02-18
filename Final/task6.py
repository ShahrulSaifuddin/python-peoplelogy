import tkinter as tk
from tkinter import Label, Entry, Button, Text, ttk

def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap elements if they are in the wrong order
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def on_sort_button_click():
    try:
        input_numbers = [int(x) for x in entry_numbers.get().split()]

        bubble_sort(input_numbers)

        result_text.delete(1.0, "end")
        result_text.insert("end", f"Sorted List: {input_numbers}")
    except ValueError:
        result_text.delete(1.0, "end")
        result_text.insert("end", "Invalid input. Please enter valid integers.")

# Create the main tkinter window
root = tk.Tk()
root.title("Bubble Sort Algorithm")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# Create and place ttk widgets with improved styling
label_numbers = ttk.Label(root, text="Enter integers (space-separated):", background="#f2f2f2", font=("Helvetica", 12))
label_numbers.pack(pady=10)

entry_numbers = ttk.Entry(root, width=30, font=("Helvetica", 12))
entry_numbers.pack(pady=10)

# Change the button style to a different color
style = ttk.Style()
style.configure("TButton", background="#e74c3c", foreground="#333333", font=("Helvetica", 12))

sort_button = ttk.Button(root, text="Sort List", command=on_sort_button_click, style="TButton")
sort_button.pack(pady=10)

result_text = tk.Text(root, height=6, width=40, wrap=tk.WORD, font=("Helvetica", 12))
result_text.pack(pady=10)

# Start the GUI main loop
root.mainloop()
