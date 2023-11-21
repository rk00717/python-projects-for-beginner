from os import path
import sys

if getattr(sys, 'frozen', False):
    DEFAULT_DATA_PATH = sys._MEIPASS
else:
    DEFAULT_DATA_PATH = path.dirname(path.abspath(__file__))

# DEFAULT_DATA_PATH = "./rkode/jsonData/"

WORD_DICT_PATH = path.join(DEFAULT_DATA_PATH, "word_dict.json")
MADLIB_DICT_PATH = path.join(DEFAULT_DATA_PATH, "madlib_dict.json")