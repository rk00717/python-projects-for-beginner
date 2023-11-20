from rkode.game_base_module import GameBase
from rkode.constant import MADLIB_DICT_PATH as data_path

from json import load
from random import randrange

class Madlib(GameBase):
    def __init__(self):
        with open(data_path, mode = 'r', encoding = 'utf-8', errors = 'strict', buffering = 1) as file:
            self.content = load(file)
            print(f"{len(self.content)} madlibs found.")

    def pick_any_madlib(self):
        range = len(self.content)
        pickedValue = randrange(1, range)
        print(f"{pickedValue} number is selected.")
        return str(pickedValue)

    def take_inputs(self, inputlist):
        formating_values = list()
        counter=0
        
        print(f'Number of inputs to be taken : {len(inputlist)}')

        for op in inputlist:
            counter+=1
            formating_values.append(input(f"{counter}. {op}"))

        return formating_values

    def display_madlib(self):
        formated_string = (self.content[self.selected_madlib]["paragraph"]).format(*self.input_values)
        print(formated_string)

    def get_new_madlib(self):
        self.selected_madlib = self.pick_any_madlib()

        content = self.content
        self.input_values = self.take_inputs(content[self.selected_madlib]["inputs"])
        self.display_madlib()

    def start_game(self):
        self.get_new_madlib()