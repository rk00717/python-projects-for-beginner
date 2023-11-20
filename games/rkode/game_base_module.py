from abc import ABC, abstractmethod

class GameBase(ABC):
    @abstractmethod
    def start_game(self):
        ...