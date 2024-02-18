import tkinter as tk
from tkinter import Label, Entry, Button, Text, ttk

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")

def on_divide_button_click():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        result = divide_numbers(num1, num2)

        result_text.delete(1.0, "end")
        result_text.insert("end", f"Result: {result}")
    except ValueError:
        result_text.delete(1.0, "end")
        result_text.insert("end", "Invalid input. Please enter valid numbers.")
    except ZeroDivisionError as e:
        result_text.delete(1.0, "end")
        result_text.insert("end", f"Error: {str(e)}")

# Create the main tkinter window
root = tk.Tk()
root.title("Division Calculator")
root.geometry("400x300")
root.configure(bg="#f2f2f2")

# Create and place ttk widgets with improved styling
label_num1 = ttk.Label(root, text="Enter the numerator:", background="#f2f2f2", font=("Helvetica", 12))
label_num1.pack(pady=5)

entry_num1 = ttk.Entry(root, width=30, font=("Helvetica", 12))
entry_num1.pack(pady=5)

label_num2 = ttk.Label(root, text="Enter the denominator:", background="#f2f2f2", font=("Helvetica", 12))
label_num2.pack(pady=5)

entry_num2 = ttk.Entry(root, width=30, font=("Helvetica", 12))
entry_num2.pack(pady=5)

# Change the button style for better visibility
style = ttk.Style()
style.configure("TButton", background="#3498db", foreground="#333333", font=("Helvetica", 12))

divide_button = ttk.Button(root, text="Divide Numbers", command=on_divide_button_click, style="TButton")
divide_button.pack(pady=10)

result_text = tk.Text(root, height=6, width=40, wrap=tk.WORD, font=("Helvetica", 12))
result_text.pack(pady=10)

# Start the GUI main loop
root.mainloop()
