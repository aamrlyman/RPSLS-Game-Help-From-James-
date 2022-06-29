from ai import AI
from human import Human
from game import Game

# player_1 = Human()
# Player_2 = AI()

# print(Player_2.chosen_gesture)
# print(player_1.chosen_gesture)

game = Game()

game.display_welcome_rules()

game.choose_players()
game.game_phase()

