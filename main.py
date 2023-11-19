from rkode.madlib_module import Madlib
from rkode.guessthenumber_module import GuessTheNumber
from rkode.rockpaperscissor_module import RockPaperScissor
from rkode.hangman_module import Hangman

def play_madlib():
    game_instance = Madlib()
    game_instance.get_new_madlib()

def play_guessthenumber():
    game_instance = GuessTheNumber()
    game_instance.start_game()

def play_rockpaperscissor():
    game_instance = RockPaperScissor()
    game_instance.start_game()

def play_hangman():
    game_instance = Hangman()
    game_instance.start_game()

if __name__ == "__main__":
    # play_madlib()
    # play_guessthenumber()
    # play_rockpaperscissor()
    play_hangman()