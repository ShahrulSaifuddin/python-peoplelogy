import tkinter as tk
from tkinter import Label, Entry, Button, ttk

def find_average(numbers):
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average

def on_calculate_button_click():
    try:
        input_numbers = [float(x) for x in entry.get().split()]
        average_result = find_average(input_numbers)
        result_label.config(text=f"Average: {average_result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers separated by spaces.")

# Create the main tkinter window
root = tk.Tk()
root.title("Average Calculator")
root.geometry("300x200")
root.configure(bg="#f2f2f2")

# Create and place ttk widgets with improved styling
label = ttk.Label(root, text="Enter numbers (space-separated):", background="#f2f2f2", font=("Helvetica", 12))
label.pack(pady=10)

entry = ttk.Entry(root, width=30, font=("Helvetica", 12))
entry.pack(pady=10)

# Change the button style for better visibility
style = ttk.Style()
style.configure("TButton", background="#3498db", foreground="#2c3e50", font=("Helvetica", 12))

calculate_button = ttk.Button(root, text="Calculate Average", command=on_calculate_button_click, style="TButton")
calculate_button.pack(pady=15)

result_label = ttk.Label(root, text="Average:", background="#f2f2f2", font=("Helvetica", 12))
result_label.pack()

# Start the GUI main loop
root.mainloop()
