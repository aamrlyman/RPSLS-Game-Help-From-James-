from human import Human 
from ai import AI
import time 

class Game:
    def __init__(self) -> None:
        self.player_1 = {}
        self.player_2 = {}

    
    def display_welcome_rules(self):
        
        print('')
        print('Welcome to Rock-Paper-Scissors-Lizard-Spock!', 'Each match will be best out of three.')
        print('')
        for key, value in what_beats_what.items():
            for loser in value:
                time.sleep(.5)
                print(f'{key} {loser[0]} {loser[1]}')
    
    def choose_players(self):
        print('')
        selector = int(input("How many human players?(0, 1, 2): "))
        while selector < 0 or selector > 2:
            print('Invalid Entry')
            selector = int(input("How many human players?(0, 1, 2): "))
        if selector == 0:
            self.player_1 = AI()
            self.player_2 = AI()
        elif selector == 1:
            self.player_1 = Human()
            self.player_2 = AI()
        elif selector == 2:
            self.player_1 = Human()
            self.player_2 = Human()
        print('')



    def game_phase(self):
        while self.player_1.num_of_wins < 2 and self.player_2.num_of_wins < 2:
            self.player_1.chosen_gesture = self.player_1.choose_gesture()
            self.player_2.chosen_gesture = self.player_2.choose_gesture()
            print('')
            print(f'{self.player_1.name} chose {self.player_1.chosen_gesture}.')
            print(f'{self.player_2.name} chose {self.player_2.chosen_gesture}.')
            print('')
            time.sleep(.5)
            
            gesture_1 = self.player_1.chosen_gesture
            gesture_2 = self.player_2.chosen_gesture

            if gesture_1 == gesture_2:
                print("Its a tie. Try again!")
            elif beats(gesture_1, gesture_2):
                    self.player_1.num_of_wins += 1
                    print(f' That is {self.player_1.num_of_wins} wins for {self.player_1.name}!')
            else:
                self.player_2.num_of_wins += 1
                print(f' That is {self.player_2.num_of_wins} wins for {self.player_2.name}!')
            print('')

    def display_winner(self):
        print('')
        time.sleep(.5)
        winner = self.player_1 if self.player_1.num_of_wins > self.player_2.num_of_wins else self.player_2
        print(f'{winner.name} is the WINNER! Way to go!!!')
            
    def play_again(self): 
        time.sleep(.5)
        print('')
        play_again = input('Do you want to play again? y or n:')
        if play_again == 'y':
            self.run_game()
        else:
            time.sleep(.5)
            print("Thanks for playing!")

    def run_game(self):
        self.display_welcome_rules()
        self.choose_players()
        self.game_phase()
        self.display_winner()
        self.play_again()




what_beats_what = {
    'Rock': [
        ('crushes', 'Scissors'),
        ('crushes', 'Lizard')
    ],
    'Scissors': [
        ('cuts', 'Paper'),
        ('decapitates', 'Lizard')
    ],
    'Paper': [
        ('covers', 'Rock'),
        ('disproves', 'Spock')
    ],
    'Lizard': [
        ('poisons', 'Spock'),
        ('eats', 'Paper')
    ],
    'Spock': [
        ('smashes', 'Scissors'), 
        ('vaporizes', 'Rock')
    ]
}

def beats(a, b):
    what_a_beats = what_beats_what[a]
    b_matches_what_a_beats = map(lambda x: x[1] == b, what_a_beats)
    return any(b_matches_what_a_beats)