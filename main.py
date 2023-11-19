from os import system

from rkode.madlib_module import Madlib
from rkode.guessthenumber_module import GuessTheNumber
from rkode.rockpaperscissor_module import RockPaperScissor
from rkode.hangman_module import Hangman

playlist = {
    "1": ["Madlib 🎓", Madlib()],
    "2": ["Guess The Number 🔢", GuessTheNumber()],
    "3": ["Rock Paper Scissor 🤞", RockPaperScissor()],
    "4": ["Hangman 💔", Hangman()]
}

def display_playlist():
    counter = 0
    for k in playlist.keys():
        counter += 1
        print(f"{counter}. {playlist[k][0]}")

    print(f"0. Exit to desktop 😢")

    selection = input("Enter your choice : ")
    if selection == "0":
        exit()

    game_instance = playlist[selection][1]
    game_instance.start_game()

if __name__ == "__main__":
    while True:
        system("cls")
        print("Fun with python 🐍!")
        display_playlist()