from rkode.game_base_module import GameBase

from random import randrange
from os import system

class GuessTheNumber(GameBase):
    def user_guess(self, min_guess_limit, max_guess_limit):
        guess_count = 0
        guess = randrange(min_guess_limit, max_guess_limit)
        while(True):
            my_guess = int(input("guess : "))
            guess_count +=1
            if(my_guess > guess):
                print("Sry. Your guess is too high to compare.\n")
            elif(my_guess == guess):
                print(f"Yea!! you{(' finally ' if guess_count >=2 else ' ')}guess the word.")
                system("pause")
                break
                # self.ask_choice()
            elif(my_guess < guess):
                print("Sry. Your guess is too low to compare.\n")

    def system_guess(self, min_guess_limit, max_guess_limit):
        guess_count = 0
        guess = randrange(min_guess_limit, max_guess_limit)
        while True:
            guess = randrange(min_guess_limit, max_guess_limit) if(min_guess_limit != max_guess_limit) else guess
            my_answer = input(f"Is {guess} is to High(H), to Low(L), or Correct(C) : ").lower()
            guess_count += 1
            if(my_answer == 'h'):
                guess -= 1
                max_guess_limit = guess
            elif(my_answer == 'c'):
                print(f"Yeepy! I guessed the word correct in {guess_count} tries")
                system("pause")
                break
                # self.ask_choice()
            elif(my_answer == 'l'):
                guess += 1
                min_guess_limit = guess

    # def ask_choice(self):
    #     system("cls")
    #     print("1. Replay")
    #     print("2. Restart")
    #     print("3. Quit")
    #     preference = input("Enter your choice : ")
    #     if preference.isdigit:
    #         preference = int(preference)
    #         if preference == 1:
    #             self.play_game()
    #         elif preference == 2:
    #             self.start_game()
    #     else:
    #         print("Sorry, Invalid choices were made..")
    #         self.ask_choice()

    def play_game(self):
        preference = input("\nWho do you want to guess the number?\n System(S) or You(Y) : ").lower()

        print("")

        if(preference == 'y'):
            self.user_guess(self.min_guess_limit, self.max_guess_limit)
        elif(preference == 's'):
            self.system_guess(self.min_guess_limit, self.max_guess_limit)
        else:
            self.play_game()

    def normalize_limit(self, min_guess_limit, max_guess_limit):
        if(min_guess_limit>max_guess_limit):
            min_guess_limit, max_guess_limit = max_guess_limit, min_guess_limit

    def start_game(self):
        super().start_game()
        system("cls")
        print("You are playing  -> GUESS THE NUMBER \n")

        self.min_guess_limit = int(input("Minimum guess value : "))
        self.max_guess_limit = int(input("Maximum guess value : "))

        self.normalize_limit(self.min_guess_limit, self.max_guess_limit)
        self.play_game()
