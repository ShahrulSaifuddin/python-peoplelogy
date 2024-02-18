from tkinter import Tk, Label, Text, Button
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spell Checker")

        self.label = Label(root, text="Enter text to spell check:")
        self.label.pack()

        self.text_input = Text(root, height=10, width=50)
        self.text_input.pack()

        self.check_button = Button(root, text="Check Spelling", command=self.spell_check)
        self.check_button.pack()

    def spell_check(self):
        text = self.text_input.get("1.0", "end-1c")  # Retrieve text from Text widget
        spell = SpellChecker()

        # Split the text into words
        words = text.split()

        # Find misspelled words
        misspelled = spell.unknown(words)

        # Display suggestions in a new window
        suggestions_window = Tk()
        suggestions_window.title("Spelling Suggestions")

        for word in misspelled:
            suggestions = spell.candidates(word)
            suggestion_label = Label(suggestions_window, text=f"Misspelled word: {word}, Suggestions: {suggestions}")
            suggestion_label.pack()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = SpellCheckerApp(root)
    app.run()
