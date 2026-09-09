
import pyxel
from game import GameController

def main():
    pyxel.init(224, 288, title="Pac-Man")
    game = GameController()
    pyxel.run(game.update, game.draw)

if __name__ == "__main__":
    main()
