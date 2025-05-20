import tkinter as tk

from game import game_start

def start_and_difficulty(root):

    starting_window = tk.Frame(root,width=800,height=600)
    starting_window.pack()


    difficulty = ""

    def start_game():
        
        nonlocal difficulty
        if not difficulty:
            difficulty = "Easy"
        starting_window.pack_forget()
        game_start(root,difficulty,starting_window)

    
    def change_difficulty(*args):
        difficulty_label.config(text=f"Selected Difficulty: {difficulties.get()}")
        nonlocal difficulty
        difficulty = difficulties.get()


    start_button = tk.Button(starting_window, text = "   Start   ",font=("Helvtica",18,"bold"), bg="black",fg="white",command=start_game)
    start_button.place(rely= 0.4,relx=0.5,anchor="center")


    difficulties = tk.StringVar(starting_window)
    difficulties.set("Select Difficulty")

    difficulty_menu = tk.OptionMenu(starting_window, difficulties, "Easy", "Medium", "Hard")
    difficulty_menu.place(rely= 0.5,relx=0.5,anchor="center")

    difficulty_label = tk.Label(starting_window, text="", font=("Arial", 14),fg="white",bg="black")
    
    difficulties.trace_add("write", change_difficulty)