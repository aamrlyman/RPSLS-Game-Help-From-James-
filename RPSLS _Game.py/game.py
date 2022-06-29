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
            time.sleep(.5)
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

    def game_phase(self):
        while self.player_1.num_of_wins < 2 and self.player_2.num_of_wins < 2:
            self.player_1.chosen_gesture = self.player_1.choose_gesture()
            self.player_2.chosen_gesture = self.player_2.choose_gesture()

            if self.player_1.chosen_gesture == self.player_2.chosen_gesture:
                print("Its a tie. Try again!")
            elif self.player_1.chosen_gesture == 'Rock': 
                if self.player_2.chosen_gesture == 'Scissors' or self.player_2.chosen_gesture == 'Lizard':
                    print(f'{self.player_1.name} is the winner!')
                    self.player_1.num_of_wins += 1

            
        





    

