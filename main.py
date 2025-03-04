from player import Player
from game import Game
from options import Options
from optionrndm import randomize_classes_and_options

if __name__ == "__main__":
    randomize_classes_and_options()

    player = Player.create_player()
    options = Options()
    game = Game(player, options.answer)

    game.start()
    game.run_day()
