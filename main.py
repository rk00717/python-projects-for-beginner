from rkode.madlib_module import madlib

def play_madlib():
    madlib_instance = madlib()
    madlib_instance.get_new_madlib()

if __name__ == "__main__":
    play_madlib()