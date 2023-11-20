from rkode.game_base_module import GameBase
from random import choice

class RockPaperScissor(GameBase):
    win_condition = [
        ['r', 's'],
        ['s', 'p'],
        ['p', 'r']
    ]

    abbs = {
        "r" : "rock",
        "p" : "paper",
        "s" : "scissor"
    }

    def is_win(self, p1, p2):
        if [p1, p2] in self.win_condition:
            return True
        else:
            return False

    def start_game(self):
        system_choice = choice(['r', 'p', 's'])
        user_choice = input('Choose Rock(R), Paper(P), or Scissor(S) : ').lower()

        display_result = "null"
        if(user_choice == system_choice):
            display_result = "Match Draw"
        else:
            display_result = f"You {('Won' if(self.is_win(user_choice, system_choice)) else 'Lost')} by Me"

        print(f"{display_result}\n My choice : {self.abbs[system_choice]} \n Your choice : {self.abbs[user_choice]}")

        preference = input("Do you want to play again? (Y/N) : ").lower()
        if(preference == 'y'):
            self.start_game()