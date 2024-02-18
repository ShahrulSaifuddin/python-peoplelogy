from tkinter import Tk, Label, Entry, Button, Text

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            # If the key already exists, append the value to a list
            if isinstance(merged_dict[key], list):
                merged_dict[key].append(value)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value

    return merged_dict

def on_merge_button_click():
    try:
        dict1_input = eval(entry_dict1.get())  # Using eval to convert the input string to a dictionary
        dict2_input = eval(entry_dict2.get())

        if not (isinstance(dict1_input, dict) and isinstance(dict2_input, dict)):
            result_text.delete(1.0, "end")
            result_text.insert("end", "Invalid input. Please enter valid dictionaries.")
            return

        merged_result = merge_dicts(dict1_input, dict2_input)

        result_text.delete(1.0, "end")
        result_text.insert("end", str(merged_result))
    except Exception as e:
        result_text.delete(1.0, "end")
        result_text.insert("end", f"Error: {str(e)}")

# Create the main tkinter window
root = Tk()
root.title("Dictionary Merger")

# Create and place widgets
label_dict1 = Label(root, text="Enter Dictionary 1 (Python syntax):")
label_dict1.pack()

entry_dict1 = Entry(root, width=30)
entry_dict1.pack()

label_dict2 = Label(root, text="Enter Dictionary 2 (Python syntax):")
label_dict2.pack()

entry_dict2 = Entry(root, width=30)
entry_dict2.pack()

merge_button = Button(root, text="Merge Dictionaries", command=on_merge_button_click)
merge_button.pack()

result_text = Text(root, height=6, width=40)
result_text.pack()

# Start the GUI main loop
root.mainloop()
