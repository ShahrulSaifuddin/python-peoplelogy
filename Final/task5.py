import tkinter as tk
from tkinter import Label, Entry, Button, Text, ttk

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

def on_calculate_button_click():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())

        rectangle = Rectangle(length, width)

        area_result = rectangle.calculate_area()
        perimeter_result = rectangle.calculate_perimeter()

        result_text.delete(1.0, "end")
        result_text.insert("end", f"Area: {area_result}\nPerimeter: {perimeter_result}")
    except ValueError:
        result_text.delete(1.0, "end")
        result_text.insert("end", "Invalid input. Please enter valid numbers.")

# Create the main tkinter window
root = tk.Tk()
root.title("Rectangle Calculator")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# Create and place ttk widgets with improved styling
label_length = ttk.Label(root, text="Enter the length:", background="#f2f2f2", font=("Helvetica", 12))
label_length.pack(pady=5)

entry_length = ttk.Entry(root, width=30, font=("Helvetica", 12))
entry_length.pack(pady=5)

label_width = ttk.Label(root, text="Enter the width:", background="#f2f2f2", font=("Helvetica", 12))
label_width.pack(pady=5)

entry_width = ttk.Entry(root, width=30, font=("Helvetica", 12))
entry_width.pack(pady=5)

# Change the button style to improve visibility
style = ttk.Style()
style.configure("TButton", background="#3498db", foreground="#333333", font=("Helvetica", 12))

calculate_button = ttk.Button(root, text="Calculate", command=on_calculate_button_click, style="TButton")
calculate_button.pack(pady=10)

result_text = tk.Text(root, height=6, width=40, wrap=tk.WORD, font=("Helvetica", 12))
result_text.pack(pady=10)

# Start the GUI main loop
root.mainloop()
