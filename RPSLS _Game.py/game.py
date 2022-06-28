import imp
from human import Human 
from ai import AI
import time 

class Game:
    def __init__(self) -> None:
        self.human_1 = Human()
        self.human_2 = Human()
        self.ai_1 = AI()
        self.ai_2 = AI()

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




    

