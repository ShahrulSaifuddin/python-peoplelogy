import tkinter as tk
from tkinter import Label, Entry, Button, Canvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import ttk

class TemperaturePlotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Trend Plot")
        self.root.geometry("800x600")
        self.root.configure(bg="#e0e0e0")

        self.style = ttk.Style()
        self.style.theme_use("clam")  # Choose from 'clam', 'alt', or 'default'
        self.style.configure("TFrame", background="#e0e0e0")
        self.style.configure("TLabel", background="#e0e0e0", font=("Helvetica", 12))
        self.style.configure("TButton", background="#3498db", foreground="#ffffff", font=("Helvetica", 12))

        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)

        self.label = ttk.Label(self.main_frame, text="Enter temperature data (comma-separated):")
        self.label.grid(row=0, column=0, pady=(0, 10), sticky="w")

        self.entry_data = ttk.Entry(self.main_frame, width=50)
        self.entry_data.grid(row=1, column=0, pady=(0, 10))

        self.plot_button = ttk.Button(self.main_frame, text="Plot", command=self.plot_temperature_trend, style="TButton")
        self.plot_button.grid(row=2, column=0, pady=(0, 10))

        self.canvas_frame = ttk.Frame(self.main_frame)
        self.canvas_frame.grid(row=3, column=0)

        self.canvas = Canvas(self.canvas_frame, bg="#ffffff", highlightthickness=0)
        self.canvas.pack(expand=1, fill=tk.BOTH)

    def plot_temperature_trend(self):
        try:
            temperature_data = [float(x) for x in self.entry_data.get().split(',')]
            days = list(range(1, len(temperature_data) + 1))

            # Clear previous plot if any
            self.canvas.delete("all")

            # Create a figure and axis for the plot
            figure, ax = plt.subplots()
            ax.plot(days, temperature_data, marker='o', linestyle='-', color='#3498db')  # Change to a blue color
            ax.set_title('Temperature Trend Over Days', fontweight="bold", fontsize=14)
            ax.set_xlabel('Day', fontweight="bold")
            ax.set_ylabel('Temperature (°C)', fontweight="bold")
            ax.grid(True)

            # Embed the plot in the tkinter window
            canvas = FigureCanvasTkAgg(figure, master=self.canvas)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        except ValueError:
            self.canvas.delete("all")
            self.canvas.create_text(300, 200, text="Invalid input. Please enter valid numbers.", fill="red", font=("Helvetica", 12))


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperaturePlotApp(root)
    root.mainloop()
