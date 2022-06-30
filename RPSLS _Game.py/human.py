from player import Player
import time

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = input("Enter Player one's name: ")
    
    def choose_gesture(self):
            print('(0)Rock', '(1)Paper', '(2)Scissors', '(3)Lizard', '(4)Spock')
            self.chosen_gesture = self.gestures_list[int(input(f"{self.name} enter a number between 0 and 4: "))]
            if self.chosen_gesture == -1:
                self.chosen_gesture = self.gestures_list[int(input(f"{self.name} enter a number between 0 and 4: "))]
            return self.chosen_gesture

