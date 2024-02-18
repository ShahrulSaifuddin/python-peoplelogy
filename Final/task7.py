import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk, scrolledtext

class NewsScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News Scraper")
        self.root.geometry("600x400")
        self.root.configure(bg="#f2f2f2")

        self.style = ttk.Style()
        self.style.theme_use("clam")  # Choose from 'clam', 'alt', or 'default'
        self.style.configure("TLabel", background="#f2f2f2", font=("Helvetica", 14))
        self.style.configure("TButton", background="#3498db", foreground="#ffffff", font=("Helvetica", 12))
        self.style.configure("TText", background="#ffffff", font=("Helvetica", 12))

        self.label = ttk.Label(root, text="Top 5 News Headlines BBC News:")
        self.label.pack(pady=(20, 10))

        self.result_text = scrolledtext.ScrolledText(root, height=10, width=50, wrap=tk.WORD, font=("Helvetica", 12))
        self.result_text.pack(pady=(0, 10))

        self.scrape_button = ttk.Button(root, text="Scrape News", command=self.scrape_news, style="TButton")
        self.scrape_button.pack(pady=(0, 20))

    def scrape_news(self):
        url = "https://www.bbc.com/news"
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')

            news_titles = [article.text.strip() for article in article_elements[:5]]
            formatted_titles = "\n".join(news_titles)

            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", formatted_titles)
        else:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Failed to retrieve the page. Status code: {response.status_code}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = NewsScraperApp(root)
    app.run()
