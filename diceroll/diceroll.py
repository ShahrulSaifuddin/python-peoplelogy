# Import necessary libraries
import tkinter as tk
from PIL import Image, ImageTk
import random

# Create the main window
window = tk.Tk()
window.geometry("500x360")  # Adjusted window size
window.title("Dice Roll")

# List of paths to dice images
dice = ["diceroll/dice-1.1024x1024.png", "diceroll/dice-2.1024x1024.png", "diceroll/dice-3.1024x1024.png",
        "diceroll/dice-4.1024x1024.png", "diceroll/dice-5.1024x1024.png", "diceroll/dice-6.1024x1024.png"]

# Initialize images for dice labels
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200, 200)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200, 200)))

# Create labels for displaying dice images
label1 = tk.Label(window, image=image1)
label2 = tk.Label(window, image=image2)

# Store references to images to prevent them from being garbage collected
label1.image = image1
label2.image = image2

# Place the labels in the window
label1.place(x=50, y=80)   # Adjusted label1 placement
label2.place(x=280, y=80)  # Adjusted label2 placement

# Function to handle dice roll button click
def dice_roll():
    # Update image for label 1
    new_image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200, 200)))
    label1.configure(image=new_image1)
    label1.image = new_image1

    # Update image for label 2
    new_image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((200, 200)))
    label2.configure(image=new_image2)
    label2.image = new_image2

# Create and place the "ROLL" button
button = tk.Button(window, text="ROLL", bg="black", fg="white", font="Times 20 bold", command=dice_roll)
button.place(x=200, y=0)  # Adjusted button placement

# Function to simulate rolling a six-sided dice
def roll_dice():
    # Generate a random number between 1 and 6
    a = random.randint(1, 6)

    # Display the result label
    result_label = tk.Label(window, text=a, font="Times 20 bold")
    result_label.place(x=230, y=300)  # Adjusted result label placement

# Create and place the "Click" button for rolling the dice
button = tk.Button(window, text="Click", command=roll_dice)
button.place(x=220, y=270)  # Adjusted button placement
# Hide the "Click" button after it is clicked
button.place_forget()

# Start the Tkinter event loop
window.mainloop()
