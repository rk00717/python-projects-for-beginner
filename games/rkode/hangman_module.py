from rkode.game_base_module import GameBase
from rkode.constant import WORD_DICT_PATH as data_path

from json import load
from random import choice
from os import system

class Hangman(GameBase):
    hearts = 5
    delimeter = "_"

    def __init__(self):
        with open(data_path, mode = 'r', encoding = 'utf-8', errors = 'strict', buffering = 1) as file:
            self.wordlist = load(file)
            actual_length = len(self.wordlist)
            [self.wordlist.remove(word) for word in self.wordlist if "-" in word or ' ' in word]
            trim_length = len(self.wordlist)
            print(f"{actual_length} words loaded {trim_length} remained after trim...")
    
    def get_word(self):
        picked_word = choice(self.wordlist)
        return picked_word.upper()
    
    def check_game_over(self, letters):
        for value in letters:
            if value != self.delimeter:
                return False

        return True

    def start_game(self):
        super().start_game()
        self.hearts = 5

        word = self.get_word()
        letters = list(word)
        used_letters = list()
        
        display_word = [self.delimeter for _ in word]

        while True:
            system("cls")
            
            print("You are playing  -> HANGMAN \n")
            print(f"{self.hearts} ❤ hearts || {len(letters) - len(used_letters)} guesses left || Your Guesses : {' '.join(used_letters)}")
            print(f"\n{' '.join(display_word)}")

            user_guess = input("Guess the letter : ").upper()
            used_letters.append(user_guess)

            if user_guess in letters:
                index = letters.index(user_guess)
                display_word[index] = user_guess
                letters[index] = self.delimeter

                if self.check_game_over(letters):
                    system("cls")
                    print(f"Yah!!! You guessed the word : {word.upper()}... ")
                    print(f"You had {self.hearts} ❤ hearts \nYour guessed letter : {' '.join(used_letters)}")
                    break
            else:
                self.hearts -= 1
                if(self.hearts == 0):
                    system("cls")
                    print(f"Sad, but the person is no more...\nYou lost.\nCorrect word was {word}")
                    break

                print("Not a valid guess...")


        system("pause")