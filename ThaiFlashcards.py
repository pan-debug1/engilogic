import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai"), ("\u0e02", "Khor Khai"), ("\u0e03", "Khor Khuat"),
    ("\u0e04", "Khor Khwai"), ("\u0e05", "Khor Khon"), ("\u0e06", "Khor Rakhang"),
    ("\u0e07", "Ngor Ngu"), ("\u0e08", "Jor Jan"), ("\u0e09", "Chor Ching"),
    ("\u0e0a", "Chor Chang"), ("\u0e0b", "Sor So"), ("\u0e0c", "Chor Cher"),
    ("\u0e0d", "Yor Ying"), ("\u0e0e", "Dor Chada"), ("\u0e0f", "Tor Patak")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.configure(bg="#f0f8ff")
        self.current_card = {}
        
        self.card_frame = tk.Frame(root, width=300, height=200, bg="#ffebcd", bd=5, relief=tk.RIDGE)
        self.card_frame.pack(pady=20)
        
        self.label = tk.Label(self.card_frame, text="", font=("Arial", 50, "bold"), bg="#ffebcd")
        self.label.pack(expand=True)
        
        self.flip_button = tk.Button(root, text="Flip", command=self.flip_card, font=("Arial", 14), bg="#87ceeb", fg="white", width=10, relief=tk.GROOVE)
        self.flip_button.pack(pady=5)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 14), bg="#32cd32", fg="white", width=10, relief=tk.GROOVE)
        self.next_button.pack(pady=5)
        
        self.next_card()

    def next_card(self):
        self.current_card = random.choice(thai_consonants)
        self.label.config(text=self.current_card[0], fg="#8b0000")
        self.is_flipped = False
    
    def flip_card(self):
        if not self.is_flipped:
            self.label.config(text=self.current_card[1], fg="#00008b")
            self.is_flipped = True
        else:
            self.label.config(text=self.current_card[0], fg="#8b0000")
            self.is_flipped = False

# Run the application
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()