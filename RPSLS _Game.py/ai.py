from player import Player
import random
import time

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = input("Enter a name for AI player: ")

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures_list)
        time.sleep(.5)
        print(f'{self.name} chose {self.chosen_gesture}')
        return self.chosen_gesture