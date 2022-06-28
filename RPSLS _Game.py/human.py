from player import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = input("Enter Player one's name: ")
        self.chosen_gesture = self.gestures_list[int(input())]
        
