from player import Player
import random

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Computer'
        self.chosen_gesture = random.choice(self.gestures_list)
