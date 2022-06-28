import imp
from human import Human 
from ai import AI
import time 

class Game:
    def __init__(self) -> None:
        self.player_1 = {}
        self.player_2 = {}

    def run_game():
        pass
    
    def display_welcome_rules(self):
        game_rules = ['Rock crushes Scissors', 'Scissors cuts Paper', 'Paper covers Rock', 
                      'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors', 
                      'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 
                      'Spock vaporizes Rock']

        print('')
        print('Welcome to Rock-Paper-Scissors-Lizard-Spok!')
        print('')
        for message in game_rules: 
            time.sleep(1)
            print(message)
    
    def choose_players(self):
        selector = int(input("How many human players?(0, 1, 2): "))
        if selector == 0:
            self.player_1 = AI()
            self.player_2 = AI()
        elif selector == 1:
            self.player_1 = Human()
            self.player_2 = AI()
        else:
            self.player_1 = Human()
            self.player_2 = Human()
        





    

