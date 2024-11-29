import tkinter as tk
import random

def jokes_file():
    jokes = []
    try:
        with open('Assessment 1/Exercise 2/Jokes.txt', 'r') as file:
            for line in file:
                if '?' in line:
                    setup, punchline = line.strip().split("?", 1)
                    jokes.append((setup + "?", punchline))
    except FileNotFoundError:
        jokes = [("Error: File not found!", "Please check the file path and try again.")]
    return jokes

root = tk.Tk()
root.title('Random Joke Generator')
root.geometry('400x400')

current_joke = None
random_jokes = jokes_file()

setup_label = tk.Label(root, text="Click here to start!", wraplength=350, font=("Ariel", 13))
setup_label.pack(pady=20)

punchline_label = tk.Label(root, text="", wraplength=350, font=("Arial", 13, "italic"))
punchline_label.pack(pady=20)

def say_joke():
    global current_joke, random_jokes
    if random_jokes:
        current_joke = random.choice(random_jokes)
        random_jokes.remove(current_joke)
        setup_label.config(text=current_joke[0])
        punchline_label.config(text="")
    else:
        setup_label.config(text="No more jokes available")
        punchline_label.config(text="")


def show_punchline():
    if current_joke:
        punchline_label.config(text=current_joke[1]) 
    else:
        punchline_label.config(text="Click 'Tell me a joke' first")

tell_joke_button = tk.Button(root, text="Tell me a joke", command=say_joke, width=20, height=2)
tell_joke_button.pack(padx=20, pady=15)

show_punchline_button = tk.Button(root, text="Show punchline", command=show_punchline, width=20, height=2)
show_punchline_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.quit, width=20, height=2)
quit_button.pack(pady=10)

root.mainloop()