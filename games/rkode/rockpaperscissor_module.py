from rkode.game_base_module import GameBase

from random import choice
from os import system

class RockPaperScissor(GameBase):
    valid_gesture = ['r', 'p', 's']

    win_condition = [
        ['r', 's'],
        ['s', 'p'],
        ['p', 'r']
    ]

    abbs = {
        "r" : "rock ✊",
        "p" : "paper 🤚",
        "s" : "scissor ✌"
    }

    def is_win(self, p1, p2):
        if [p1, p2] in self.win_condition:
            return True
        else:
            return False

    def start_game(self):
        super.start_game()
        system("cls")

        print("You are playing -> Rock✊ Paper🤚 Scissor✌\n")

        system_choice = choice(self.valid_gesture)
        valid_input = False
        while not valid_input:
            user_choice = input('Choose Rock(R), Paper(P), or Scissor(S) : ').lower()
            if user_choice in self.valid_gesture:
                valid_input = True
            else:
                print("Invalid choice!! please be fair to me 😢...")

        print(f"\nMy choice : {self.abbs[system_choice]} \nYour choice : {self.abbs[user_choice]}")
        display_result = "null"
        if(user_choice == system_choice):
            display_result = "Match Draw"
        else:
            display_result = f"You {('Won' if(self.is_win(user_choice, system_choice)) else 'Lost')} by Me"

        print(f"\n{display_result}") 

        system("pause")