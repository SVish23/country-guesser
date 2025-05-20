import tkinter as tk
import pandas as pd
import sys
import random


def game_start(root, difficulty,menu_frame):
    
    if not root:
        sys.exit(1)
        
    if not difficulty:
        sys.exit(2)
    
    if not menu_frame:
        sys.exit(3)

    country_data = pd.read_csv('country_list.csv')

    game_frame = tk.Frame(root,width=800,height=600)
    game_frame.pack()

    country_label = tk.Label(game_frame,text="BLANK",font=("Helvtica",24,"bold"))
    country_label.place(rely=0.4,relx=0.5,anchor="center")

    score = 0
    
    score_label = tk.Label(game_frame,text=f"{score}", font=("Helvetica",20,"bold"))
    score_label.place(rely=0.2,relx=0.5,anchor="center")


    scores_df = pd.read_csv("scores.csv")

    def gen_country():

        country = country_data.sample().iloc[0]
        country_name = country['Country']
        country_label.config(text=f"{country_name}")

        return country, country_name

    buttons = []
    for i in range(4):
        button = tk.Button(game_frame, text = "Button",font=("Helvtica",14,"bold"),width=12,height=2,bg="#f0f0f0",state='normal')
        if difficulty != "Hard":
            button.place(rely=0.55,relx=0.1+i*0.2)
        buttons.append(button)

    def check_answer(selected_answer="", correct_answer="",user_input="",correct_button=""):

        nonlocal score
        continue_playing = True

        if selected_answer == correct_answer:
            
            user_input.config(bg="green")
            score += 1
        else:
            continue_playing = False

            if scores_df.at[0,difficulty] < score:
                scores_df.at[0,difficulty] = score
                scores_df.to_csv("scores.csv",index=False)

            lose_canvas = tk.Canvas(game_frame,height=300,width=400,bg='black')
            lose_canvas.place(rely=0.5,relx=0.5,anchor='center')

            def restart():
                nonlocal score
                score = 0
                user_input.config(state="disabled")
                score_label.config(text=f"{score}")
                lose_canvas.place_forget()
                continue_game()

            def back_to_main_menu():
                game_frame.pack_forget()
                menu_frame.pack()

            highscore_label = tk.Label(lose_canvas,text=f"HIGHSCORE: {scores_df.at[0,difficulty]}",font=("Helvetica",18,"bold"),fg="white",bg="black")
            highscore_label.place(rely=0.3,relx=0.5,anchor="center")
            
            play_again_button = tk.Button(lose_canvas, text = "Play again", font=("Helvtica",12,"bold"),width=12,height=1,bg="#f0f0f0",state='normal',command=restart)
            play_again_button.place(rely=0.6,relx=0.5,anchor='center')

            back_to_menu_button = tk.Button(lose_canvas, text = "Back to menu", font=("Helvtica",12,"bold"),width=12,height=1,bg="#f0f0f0",state='normal',command=back_to_main_menu)
            back_to_menu_button.place(rely=0.8,relx=0.5,anchor="center")
            
            user_input.config(bg="red")
        if difficulty != "Hard":
            correct_button.config(bg="green")
        score_label.config(text=f"{score}")

        
        for b in buttons:
            b.config(state='disabled')
                    

        if continue_playing == True:
            game_frame.after(1000,continue_game)


    def easy_game():

        country, country_name = gen_country()

        correct_continent = country['Continent']
        
        contintents = set([correct_continent])
        while len(contintents) < 4:
            random_continent = random.choice(country_data["Continent"].tolist())
            contintents.add(random_continent)
        
        continent_options = list(contintents)
        random.shuffle(continent_options)
        
        
        for i, button in enumerate(buttons):
            continent = continent_options[i]
            if continent == correct_continent:
                correct_button = button
            button.config(text=continent,bg="#f0f0f0",state="normal",command=lambda b=button, c= continent: check_answer(c, correct_continent, b, correct_button))

    def medium_game():

        country, country_name = gen_country()

        correct_capital = country['Capital']
        
        capitals = set([correct_capital])
        while len(capitals) < 4:
            random_capital = random.choice(country_data["Capital"].tolist())
            capitals.add(random_capital)
        
        capital_options = list(capitals)
        random.shuffle(capital_options)
        
        for i, button in enumerate(buttons):
            capital = capital_options[i]
            if capital == correct_capital:
                correct_button = button
            button.config(text=capital,bg="#f0f0f0",state="normal",command=lambda b=button, c= capital: check_answer(c, correct_capital, b, correct_button))

    def hard_game():
        
        country, country_name = gen_country()
        correct_capital = country['Capital']

        entry = tk.Entry(game_frame,font=("Helvetica",16),state="normal")
        entry.place(rely=0.6,relx=0.5,anchor="center")
        entry.focus_set()
        
        submit_button = tk.Button(game_frame,text="Submit",bg='#f0f0f0', state="normal",command = lambda: check_answer(entry.get(), correct_capital, entry))
        submit_button.place(rely=0.6,relx=0.625,anchor="center")

        entry.bind("<Return>", lambda event: check_answer(entry.get(), correct_capital, entry) )
    
    def continue_game():
        if difficulty == "Easy":
            easy_game()
            return "Easy"
        elif difficulty == "Medium":
            medium_game()
            return "Medium"
        else:
            hard_game()
            return "Hard"
    continue_game()
    
    