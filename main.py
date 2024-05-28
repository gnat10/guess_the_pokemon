from guess_pokemon import Guess
from pokemon import Pokemon
import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image


root = tk.Tk()
root.title('Guess the Pokemon')
root.geometry("700x700")


def enter_cursor():
    menu_canvas.config(cursor="hand2")


def leave_cursor():
    menu_canvas.config(cursor="")


def main_menu():
    menu_canvas.pack(fill="both", expand=True)
    menu_canvas.create_image(0, 0, image=bg_path, anchor="nw")
    menu_canvas.create_image(350, 200, image=logo_path)

    play_button = menu_canvas.create_image(350, 450, image=play_path, tag=cursor)
    menu_canvas.tag_bind(cursor, "<Enter>", lambda event: enter_cursor())
    menu_canvas.tag_bind(cursor, "<Leave>", lambda event: leave_cursor())
    menu_canvas.tag_bind(play_button, "<Button-1>", game_menu)

    exit_button = menu_canvas.create_image(350, 600, image=exit_path, tag=cursor)
    menu_canvas.tag_bind(exit_button, "<Button-1>", exit_game)


def new_pokemon():
    pokemon_name = Pokemon.random_pokemon("data/pokemon_name.csv")
    return pokemon_name


answer_pokemon = ""


def get_pokemon():
    global answer_pokemon
    answer_pokemon = new_pokemon()
    pokemon_img(answer_pokemon)
    global hinter, hint_count
    hinter = ""
    hint_count = 0


new_image = ""


def pokemon_img(self):
    Pokemon.save_pokemon_image(str(self).lower())
    chosen_pokemon_image = Image.open(f'./data/pokemon_image/{(str(self).lower())}.gif')
    resized = chosen_pokemon_image.resize((int(chosen_pokemon_image.width * 4), int(chosen_pokemon_image.height * 4)))
    global new_image
    new_image = ImageTk.PhotoImage(resized)
    game_canvas.create_image(350, 225, image=new_image)


def get_attempt(event):
    answer = answer_input.get().capitalize()
    answer = answer.replace("'", "")
    answer = answer.replace(" ", "")
    guess = Guess(answer_pokemon)
    guess.attempt(answer)
    right_response = tk.Label(game_canvas, text=f"Correct, It's {answer}", font=("Helvetica", 24))
    incorrect_response = tk.Label(game_canvas, text='Incorrect, Try Again!', font=("Helvetica", 24))

    if guess.is_correct:
        answer_input.delete(0, 'end')
        Pokemon.delete_pokemon_image(f'./data/pokemon_image/{answer_pokemon}.gif')
        incorrect_response.config(text="")
        hint_label.config(text="Click for hint")
        right_response.place(x=200, y=500)
        get_pokemon()

    else:
        answer_input.delete(0, 'end')
        right_response.config(text="")
        incorrect_response.place(x=200, y=500)
        print(guess.secret)


def back_home(self):
    Pokemon.delete_pokemon_image(f'./data/pokemon_image/{answer_pokemon}.gif')
    game_canvas.forget()
    menu_canvas.pack(fill="both", expand=True)


def enter_game_cursor():
    game_canvas.config(cursor="hand2")


def leave_game_cursor():
    game_canvas.config(cursor="")


hinter = ""
hint_count = 0


def hint(self):
    global hinter
    global hint_count

    if hint_count < len(f"{answer_pokemon}"):
        hinter = hinter + f"{answer_pokemon}"[hint_count]
        hint_label.config(text=hinter)
        hint_count += 1


def game_menu(event):
    menu_canvas.forget()
    game_canvas.pack(fill="both", expand=True)
    game_canvas.create_image(0, 0, image=bg_path, anchor="nw")

    get_pokemon()

    answer_input.pack(side=tk.BOTTOM, pady=225)
    answer_input.bind("<Return>", get_attempt)

    return_button = game_canvas.create_image(625, 625, image=return_path, tag=cursor)
    game_canvas.tag_bind(cursor, "<Enter>", lambda event: enter_game_cursor())
    game_canvas.tag_bind(cursor, "<Leave>", lambda event: leave_game_cursor())
    game_canvas.tag_bind(return_button, "<Button-1>", back_home)

    hint_button = game_canvas.create_image(75, 625, image=hint_path, tag=cursor)
    game_canvas.tag_bind(hint_button, "<Button-1>", hint)
    hint_label.place(x=100, y=600)


def exit_game(event):
    root.destroy()


cursor = 'event'
# menu canvas
bg_path = PhotoImage(file="data/resources/bg_grass.png")
menu_canvas = tk.Canvas(root, width=1000, height=1000)

logo_path = PhotoImage(file="data/resources/guess_the_pokemon.png")

play_path = PhotoImage(file="data/resources/play_button.png")

exit_path = PhotoImage(file="data/resources/exit_button.png")

# game canvas
game_canvas = tk.Canvas(root, width=1000, height=1000)

chosen_pokemon = new_pokemon

answer_input = tk.Entry(game_canvas, font=("Helvetica", 24))

return_path = PhotoImage(file="data/resources/return_button.png")

hint_path = PhotoImage(file="data/resources/light_bulb.png")
hint_label = tk.Label(game_canvas, text='Click for hint', font=("Helvetica", 16))

if __name__ == "__main__":

    main_menu()
    root.mainloop()
