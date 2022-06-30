import imp
from human import Human 
from ai import AI
import time 

class Game:
    def __init__(self) -> None:
        self.player_1 = {}
        self.player_2 = {}

    
    def display_welcome_rules(self):
        game_rules = ['Rock crushes Scissors', 'Scissors cuts Paper', 'Paper covers Rock', 
                      'Rock crushes Lizard', 'Lizard poisons Spock', 'Spock smashes Scissors', 
                      'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 
                      'Spock vaporizes Rock']

        print('')
        print('Welcome to Rock-Paper-Scissors-Lizard-Spock!')
        print('')
        for message in game_rules: 
            time.sleep(.5)
            print(message)
    
    def choose_players(self):
        print('')
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
        print('')

    def game_phase(self):
        while self.player_1.num_of_wins < 2 and self.player_2.num_of_wins < 2:
            self.player_1.chosen_gesture = self.player_1.choose_gesture()
            self.player_2.chosen_gesture = self.player_2.choose_gesture()

            if self.player_1.chosen_gesture == self.player_2.chosen_gesture:
                time.sleep(.5)
                print("Its a tie. Try again!")
                print('')
            elif self.player_1.chosen_gesture == 'Rock' and (self.player_2.chosen_gesture == 'Scissors' or self.player_2.chosen_gesture == 'Lizard'):
                    self.player_1.num_of_wins += 1
                    time.sleep(.5)
                    print(f' That is {self.player_1.num_of_wins} wins for {self.player_1.name}!')
                    print('')
            elif self.player_1.chosen_gesture == 'Paper' and (self.player_2.chosen_gesture == 'Rock' or self.player_2.chosen_gesture == 'Paper'):
                    self.player_1.num_of_wins += 1
                    time.sleep(.5)
                    print(f' That is {self.player_1.num_of_wins} wins for {self.player_1.name}!')
                    print('')
            elif self.player_1.chosen_gesture == 'Scissors' and (self.player_2.chosen_gesture == 'Paper' or self.player_2.chosen_gesture == 'Lizard'):
                    self.player_1.num_of_wins += 1
                    time.sleep(.5)
                    print(f' That is {self.player_1.num_of_wins} wins for {self.player_1.name}!')
                    print('')
            elif self.player_1.chosen_gesture == 'Lizard' and (self.player_2.chosen_gesture == 'Spock' or self.player_2.chosen_gesture == 'Paper'):
                    self.player_1.num_of_wins += 1
                    time.sleep(.5)
                    print(f' That is {self.player_1.num_of_wins} wins for {self.player_1.name}!')
                    print('')
            elif self.player_1.chosen_gesture == 'Spock' and (self.player_2.chosen_gesture == 'Scissors' or self.player_2.chosen_gesture == 'Rock'):
                    self.player_1.num_of_wins += 1
                    time.sleep(.5)
                    print(f' That is {self.player_1.num_of_wins} wins for {self.player_1.name}!')
                    print('')
            else:
                self.player_2.num_of_wins += 1
                time.sleep(.5)
                print(f' That is {self.player_2.num_of_wins} wins for {self.player_2.name}!')
                print('')

    def display_winner(self):
        if self.player_1.num_of_wins > self.player_2.num_of_wins:
            print('')
            time.sleep(.5)
            print(f'{self.player_1.name} won best of out of 3 games! Way to go!')        
        else:
            print('')
            time.sleep(.5)
            print(f'{self.player_2.name} won best of out of 3 games! Way to go!')
            
    def play_again(self): 
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






    

