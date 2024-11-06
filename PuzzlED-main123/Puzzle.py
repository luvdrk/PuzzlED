import tkinter as tk
import random
from tkinter import messagebox, simpledialog

class WordSearchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("PuzzlED")
        self.root.geometry("1000x700")

        self.categories = {
            "Food": ["APPLE", "ORANGE", "BANANA", "GRAPE", "PEAR", "KIWI", "MANGO", "PINEAPPLE", "STRAWBERRY", "WATERMELON", "CHERRY", "LEMON", "PEACH", "CANTALOUPE", "AVOCADO", "CARROT", "POTATO", "TOMATO", "ONION", "GARLIC", "CUCUMBER", "BROCCOLI", "SPINACH", "PEPPER", "ZUCCHINI", "CAULIFLOWER", "PIZZA", "BURGER", "PASTA", "SUSHI", "SALAD", "SOUP", "OMELETTE", "LASAGNA", "FAJITAS", "KEBAB", "PAELLA", "QUICHE", "CASSEROLE"],
            "Animals": ["DOG", "CAT", "HORSE", "COW", "SHEEP", "GOAT", "TIGER", "LION", "PANDA", "GIRAFFE", "ZEBRA", "ELEPHANT", "KANGAROO", "SLOTH", "PARROT", "EAGLE", "HAWK", "FLAMINGO", "PENGUIN", "WHALE", "DOLPHIN", "FROG", "PEACOCK", "SWAN", "DUCK", "GOOSE", "PIG", "BEAR", "RABBIT", "SQUIRREL", "MOUSE", "RAT", "BAT"],
            "Colors": ["RED", "GREEN", "BLUE", "YELLOW", "PURPLE", "ORANGE", "PINK", "BLACK", "WHITE", "BROWN", "CRIMSON", "MAROON", "SCARLET", "LIME", "OLIVE", "EMERALD", "TEAL", "CYAN", "MAGENTA", "GOLD", "SILVER", "IVORY", "NAVY", "TURQUOISE", "PLUM", "LAVENDER", "CHARCOAL", "COBALT"],
            "Programming": ["PYTHON", "JAVA", "CPLUSPLUS", "JAVASCRIPT", "RUBY", "SWIFT", "PHP", "VARIABLE", "FUNCTION", "ALGORITHM", "LOOP", "ARRAY", "OBJECT", "CLASS", "INHERITANCE", "RECURSION", "DATA", "DATABASE", "DEBUG", "SYNTAX", "STRING", "INTEGER", "BOOLEAN", "LOOP", "CONDITION", "COMPILER", "INTERPRETER", "DEVELOPER", "IDE", "CONSOLE", "GITHUB", "VERSIONCONTROL", "TESTING", "ENCRYPTION"],
            "Countries": ["USA", "CANADA", "CHINA", "INDIA", "GERMANY", "FRANCE", "ITALY", "SPAIN", "JAPAN", "BRAZIL", "AUSTRALIA", "RUSSIA", "SOUTHAFRICA", "ARGENTINA", "NORWAY", "SWEDEN", "DENMARK", "POLAND", "GREECE", "TURKEY", "EGYPT", "NIGERIA", "KENYA", "VIETNAM", "THAILAND", "MEXICO", "COLOMBIA", "PERU", "CHILE", "MALAYSIA", "PHILIPPINES"]
        }

        self.selected_category = "Food"
        self.grid_size = 15
        self.grid = [['' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.custom_words = []

        self.selected_positions = []
        self.found_words = []

        self.create_widgets()
        self.generate_new_puzzle()

    def create_widgets(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        new_puzzle_button = tk.Button(button_frame, text="New Puzzle", command=self.generate_new_puzzle)
        new_puzzle_button.pack(side=tk.LEFT, padx=5)

        category_frame = tk.Frame(button_frame)
        category_frame.pack(side=tk.LEFT, padx=5)

        self.category_var = tk.StringVar(value=self.selected_category)
        self.category_menu = tk.OptionMenu(category_frame, self.category_var, *self.categories.keys(), command=self.change_category)
        self.category_menu.pack()

        custom_words_button = tk.Button(button_frame, text="Enter Custom Words", command=self.enter_custom_words)
        custom_words_button.pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.instructions = tk.Label(self.root, text="", font=("Arial", 12))
        self.instructions.pack(pady=5)

        self.buttons = []
        for row in range(self.grid_size):
            row_buttons = []
            for col in range(self.grid_size):
                btn = tk.Button(self.root, text='', width=3, height=1,
                                command=lambda r=row, c=col: self.on_letter_click(r, c))
                btn_window = self.canvas.create_window(col * 40 + 20, row * 40 + 20, window=btn)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)



    def change_category(self, new_category):
        self.selected_category = new_category
        self.custom_words.clear() 
        self.generate_new_puzzle()

    def enter_custom_words(self):
        custom_words = simpledialog.askstring("Custom Words", "Enter words separated by commas:").upper()
        if custom_words:
            self.custom_words = [word.strip() for word in custom_words.split(",") if word.strip()]
            self.fill_grid_with_custom_words()

    def fill_grid_with_custom_words(self):
        self.words = self.custom_words
        self.found_words = []
        self.selected_positions = []
        self.grid = [['' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.instructions.config(text="Find these words: " + ", ".join(self.words))

        self.place_words()
        self.fill_random_letters()

    def generate_new_puzzle(self):
        self.words = self.custom_words if self.custom_words else random.sample(self.categories[self.selected_category], 7)
        self.found_words = []
        self.selected_positions = []
        self.grid = [['' for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.instructions.config(text="Find these words: " + ", ".join(self.words))

        self.place_words()
        self.fill_random_letters()

        for row_buttons in self.buttons:
            for btn in row_buttons:
                btn.config(bg="SystemButtonFace", state="normal")

        self.category_menu.pack()

    def place_words(self):
        for word in self.words:
            placed = False
            while not placed:
                direction = random.choice(['H', 'V'])
                if direction == 'H':
                    row = random.randint(0, self.grid_size - 1)
                    col = random.randint(0, self.grid_size - len(word))
                    if all(self.grid[row][col + i] in ('', word[i]) for i in range(len(word))):
                        for i, letter in enumerate(word):
                            self.grid[row][col + i] = letter
                        placed = True
                elif direction == 'V':
                    row = random.randint(0, self.grid_size - len(word))
                    col = random.randint(0, self.grid_size - 1)
                    if all(self.grid[row + i][col] in ('', word[i]) for i in range(len(word))):
                        for i, letter in enumerate(word):
                            self.grid[row + i][col] = letter
                        placed = True

    def fill_random_letters(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col] == '':
                    self.grid[row][col] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                self.buttons[row][col].config(text=self.grid[row][col])

    def on_letter_click(self, row, col):
        if (row, col) in self.selected_positions:
            self.selected_positions.remove((row, col))
            self.buttons[row][col].config(bg="SystemButtonFace")
        else:
            self.selected_positions.append((row, col))
            self.buttons[row][col].config(bg="lightblue")

        selected_word = ''.join(self.grid[r][c] for r, c in self.selected_positions)
        if selected_word in self.words:
            self.mark_word_found(selected_word)
            self.clear_selection()
        elif len(selected_word) > max(len(word) for word in self.words):
            self.clear_selection()

    def mark_word_found(self, word):
        for row, col in self.selected_positions:
            self.buttons[row][col].config(bg="lightgreen", state="disabled")
        self.found_words.append(word)
        self.clear_selection()

        if len(self.found_words) == len(self.words):
            messagebox.showinfo("Congratulations!", "You've found all the words!")
            self.category_menu.pack()

    def clear_selection(self):
        for row, col in self.selected_positions:
            if (row, col) not in [(r, c) for word in self.found_words for r, c in self.selected_positions]:
                self.buttons[row][col].config(bg="SystemButtonFace")
        self.selected_positions.clear()


root = tk.Tk()
game = WordSearchGame(root)
root.mainloop()
