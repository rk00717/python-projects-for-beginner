from rkode.madlib_module import Madlib
from rkode.guessthenumber_module import GuessTheNumber

def play_madlib():
    madlib_instance = Madlib()
    madlib_instance.get_new_madlib()

def play_guessthenumber():
    guessthenumber_instance = GuessTheNumber()
    guessthenumber_instance.start_game()

if __name__ == "__main__":
    # play_madlib()
    play_guessthenumber()