import pyxel
from pacman import PacMan
from dot import PowerPellet
from dot import Dot
# GameController class

from blueghost import Inky
from orangeghost import Clyde
from pinkghost import Pinky
from redghost import Blinky
from maze import Maze

class GameController:
    def __init__(self):
        """
        Initialize the game controller with the maze layout, ghosts, dots, and pellets.
        """
        pyxel.load("my_resource.pyxres")
        self.game_state = "playing"  # Possible states: "playing", "game_over", "win"
        self.final_message = ""  # Final screen message
        self.power_mode_timer = 0  # Power mode duration in frames (10 seconds at 60 FPS)
        self.level_number = 1

        maze_layout = [
            "############################",
            "#............##............#",
            "#.####.#####.##.#####.####.#",
            "#.####.#####.##.#####.####.#",
            "#.####.#####.##.#####.####.#",
            "#..........................#",
            "#.####.##.########.##.####.#",
            "#.####.##.########.##.####.#",
            "#......##....##....##......#",
            "######.##### ## #####.######",
            "######.##### ## #####.######",
            "######.##          ##.######",
            "######.## ###  ### ##.######",
            "######.## #      # ##.######",
            "      .   #      #   .      ",
            "######.## #      # ##.######",
            "######.## ######## ##.######",
            "######.##          ##.######",
            "######.## ######## ##.######",
            "######.## ######## ##.######",
            "#............##............#",
            "#.####.#####.##.#####.####.#",
            "#.####.#####.##.#####.####.#",
            "#...##.......  .......##...#",
            "###.##.##.########.##.##.###",
            "###.##.##.########.##.##.###",
            "#......##....##....##......#",
            "#.##########.##.##########.#",
            "#.##########.##.##########.#",
            "#..........................#",
            "############################"
        ]

        self.ghosts = [
            Blinky(125, 112),
            Pinky(115, 112),
            Inky(100, 112),
            Clyde(120, 112),
        ]

        self.pellets = [
            PowerPellet(11, 28),
            PowerPellet(11, 189),
            PowerPellet(211, 28),
            PowerPellet(211, 189),
        ]

        self.dots = [
            Dot(10, 11),
            Dot(10, 19),
            Dot(10, 35),
            Dot(10, 43),
            Dot(10, 51),
            Dot(10, 59),
            Dot(10, 67),
            Dot(10, 163),
            Dot(10, 171),
            Dot(10, 179),
            Dot(10, 211),
            Dot(10, 219),
            Dot(10, 227),
            Dot(10, 235),
            #
            Dot(18, 11),
            Dot(18, 43),
            Dot(18, 67),
            Dot(18, 163),
            Dot(18, 187),
            Dot(18, 211),
            Dot(18, 235),
            #
            Dot(26, 11),
            Dot(26, 43),
            Dot(26, 67),
            Dot(26, 163),
            Dot(26, 187),
            Dot(26, 195),
            Dot(26, 203),
            Dot(26, 211),
            Dot(26, 235),
            #
            Dot(34, 11),
            Dot(34, 43),
            Dot(34, 67),
            Dot(34, 163),
            Dot(34, 211),
            Dot(34, 235),
            #
            Dot(42, 11),
            Dot(42, 43),
            Dot(42, 67),
            Dot(42, 163),
            Dot(42, 211),
            Dot(42, 235),
            #
            Dot(50, 11),
            Dot(50, 19),
            Dot(50, 27),
            Dot(50, 35),
            Dot(50, 43),
            Dot(50, 51),
            Dot(50, 59),
            Dot(50, 67),
            Dot(50, 75),
            Dot(50, 83),
            Dot(50, 91),
            Dot(50, 99),
            Dot(50, 107),
            Dot(50, 115),
            Dot(50, 123),
            Dot(50, 131),
            Dot(50, 139),
            Dot(50, 147),
            Dot(50, 155),
            Dot(50, 163),
            Dot(50, 171),
            Dot(50, 179),
            Dot(50, 187),
            Dot(50, 195),
            Dot(50, 203),
            Dot(50, 211),
            Dot(50, 235),
            #
            Dot(58, 11),
            Dot(58, 43),
            Dot(58, 163),
            Dot(58, 187),
            Dot(58, 235),
            #
            Dot(66, 11),
            Dot(66, 43),
            Dot(66, 163),
            Dot(66, 187),
            Dot(66, 235),
            #
            Dot(74, 11),
            Dot(74, 43),
            Dot(74, 51),
            Dot(74, 59),
            Dot(74, 67),
            Dot(74, 163),
            Dot(74, 187),
            Dot(74, 195),
            Dot(74, 203),
            Dot(74, 211),
            Dot(74, 235),
            #
            Dot(82, 11),
            Dot(82, 43),
            Dot(82, 67),
            Dot(82, 163),
            Dot(82, 187),
            Dot(82, 211),
            Dot(82, 235),
            #
            Dot(90, 11),
            Dot(90, 43),
            Dot(90, 67),
            Dot(90, 163),
            Dot(90, 187),
            Dot(90, 211),
            Dot(90, 235),
            #
            Dot(98, 11),
            Dot(98, 19),
            Dot(98, 27),
            Dot(98, 35),
            Dot(98, 43),
            Dot(98, 67),
            Dot(98, 163),
            Dot(98, 171),
            Dot(98, 179),
            Dot(98, 187),
            Dot(98, 211),
            Dot(98, 219),
            Dot(98, 227),
            Dot(98, 235),
            #
            Dot(122, 11),
            Dot(122, 19),
            Dot(122, 27),
            Dot(122, 35),
            Dot(122, 43),
            Dot(122, 67),
            Dot(122, 163),
            Dot(122, 171),
            Dot(122, 179),
            Dot(122, 187),
            Dot(122, 211),
            Dot(122, 219),
            Dot(122, 227),
            Dot(122, 235),
            #
            Dot(130, 11),
            Dot(130, 43),
            Dot(130, 67),
            Dot(130, 163),
            Dot(130, 187),
            Dot(130, 211),
            Dot(130, 235),
            #
            Dot(138, 11),
            Dot(138, 43),
            Dot(138, 67),
            Dot(138, 163),
            Dot(138, 187),
            Dot(138, 211),
            Dot(138, 235),
            #
            Dot(146, 11),
            Dot(146, 43),
            Dot(146, 51),
            Dot(146, 59),
            Dot(146, 67),
            Dot(146, 163),
            Dot(146, 187),
            Dot(146, 195),
            Dot(146, 203),
            Dot(146, 211),
            Dot(146, 235),
            #
            Dot(154, 11),
            Dot(154, 43),
            Dot(154, 163),
            Dot(154, 187),
            Dot(154, 235),
            #
            Dot(162, 11),
            Dot(162, 43),
            Dot(162, 163),
            Dot(162, 187),
            Dot(162, 235),
            #
            Dot(170, 11),
            Dot(170, 19),
            Dot(170, 27),
            Dot(170, 35),
            Dot(170, 43),
            Dot(170, 51),
            Dot(170, 59),
            Dot(170, 67),
            Dot(170, 75),
            Dot(170, 83),
            Dot(170, 91),
            Dot(170, 99),
            Dot(170, 107),
            Dot(170, 115),
            Dot(170, 123),
            Dot(170, 131),
            Dot(170, 139),
            Dot(170, 147),
            Dot(170, 155),
            Dot(170, 163),
            Dot(170, 171),
            Dot(170, 179),
            Dot(170, 187),
            Dot(170, 195),
            Dot(170, 203),
            Dot(170, 211),
            Dot(170, 235),
            #
            Dot(178, 11),
            Dot(178, 43),
            Dot(178, 67),
            Dot(178, 163),
            Dot(178, 211),
            Dot(178, 235),
            #
            Dot(186, 11),
            Dot(186, 43),
            Dot(186, 67),
            Dot(186, 163),
            Dot(186, 211),
            Dot(186, 235),
            #
            Dot(194, 11),
            Dot(194, 43),
            Dot(194, 67),
            Dot(194, 163),
            Dot(194, 187),
            Dot(194, 195),
            Dot(194, 203),
            Dot(194, 211),
            Dot(194, 235),
            #
            Dot(202, 11),
            Dot(202, 43),
            Dot(202, 67),
            Dot(202, 163),
            Dot(202, 187),
            Dot(202, 211),
            Dot(202, 235),
            #
            Dot(210, 11),
            Dot(210, 19),
            Dot(210, 35),
            Dot(210, 43),
            Dot(210, 51),
            Dot(210, 59),
            Dot(210, 67),
            Dot(210, 163),
            Dot(210, 171),
            Dot(210, 179),
            Dot(210, 211),
            Dot(210, 219),
            Dot(210, 227),
            Dot(210, 235)]

        self.maze = Maze(maze_layout, cell_size=8)
        self.pacman = PacMan(110, 187)
        # Reproducir música al inicio del juego
        pyxel.playm(0,
                    loop=True)  # Reproduce la música en el canal 0, en bucle

    def create_level(self, level_number):
        """
        Sets up the elements for a given level.
        """
        self.pacman.speed -= 1  # Increase Pac-Man's speed with each level

        # Reset dots and pellets
        for dot in self.dots:
            dot.eaten = False
        for pellet in self.pellets:
            pellet.eaten = False

        # Reset positions of Pac-Man and ghosts
        self.pacman.reset_position()
        for ghost in self.ghosts:
            ghost.reset_position()
            ghost.in_box = True
            ghost.aligned_to_exit = False
            ghost.direction = None

        self.power_mode_timer = 0
        self.game_state = "playing"
        self.final_message = ""

    def start_level(self):
        """
        Starts the current level after completing the previous one.
        """
        self.create_level(self.level_number)
        self.game_state = "playing"

    def update(self):
        """
        Main game logic.
        """
        if self.game_state == "playing":
            self.pacman.move(self.maze)

            for pellet in self.pellets: #check collisions with dots and pellets
                if not pellet.eaten and self.pacman.check_collision(pellet, 8):
                    pellet.eaten = True
                    self.activate_power_mode()

            for dot in self.dots:
                if not dot.eaten and self.pacman.check_collision(dot, 8):
                    dot.eaten = True
                    self.pacman.score += 10

            for ghost in self.ghosts:#move ghosts
                if self.pacman.check_collision(ghost, 16):
                    if self.power_mode_timer > 0:
                        ghost.frightened = True
                        self.pacman.score += 200
                        ghost.reset_position()
                        ghost.in_box = True
                        ghost.aligned_to_exit = False
                        ghost.direction = None
                    else:
                        ghost.frightened = False
                        self.pacman.lives -= 1
                        self.pacman.reset_position()
                        if self.pacman.lives <= 0:
                            self.game_over()
                else:
                    if type(ghost) == Blinky:
                        ghost.move(self.maze, self.pacman)
                    elif type(ghost) == Pinky:
                        ghost.move(self.maze, self.pacman)
                    elif type(ghost) == Inky:
                        ghost.move(self.maze, self.pacman)
                    elif type(ghost) == Clyde:
                        ghost.move(self.maze)
            #power mode
            if self.power_mode_timer > 0:
                self.power_mode_timer -= 1
            elif self.power_mode_timer == 0:
                for ghost in self.ghosts:
                    ghost.frightened = False
            #winning game
            if all(dot.eaten for dot in self.dots):
                self.win_game()

        elif self.game_state in ["level_complete", "game_over", "win"]:
            self.handle_game_state()

    def handle_game_state(self):
        """
        Handles transitions for level complete, game over, and win states.
        """
        if pyxel.btnp(pyxel.KEY_RETURN):
            if self.game_state == "level_complete":
                self.start_level()
            else:
                pyxel.quit()

    def activate_power_mode(self):
        """
        Activates power mode for 10 seconds.
        """
        self.power_mode_timer = 500
        for ghost in self.ghosts:
            ghost.frightened = True

    def game_over(self):
        """
        Handles game over state.
        """
        print("Game Over!")
        self.game_state = "game_over"
        self.final_message = f"YOU HAVE LOST\nTotal score: {self.pacman.score}\nLives left: 0\nMaybe next time!"

    def win_game(self):
        """
        Handles winning a level or completing the game.
        """
        if self.level_number < 2:
            self.level_number += 1
            self.game_state = "level_complete"
            self.final_message = f"YOU HAVE WON LEVEL {self.level_number - 1}!\nScore: {self.pacman.score}\nLives left: {self.pacman.lives}\nPress Enter to continue"
        else:
            self.game_state = "win"
            self.final_message = f"CONGRATULATIONS!\nFinal Score: {self.pacman.score}\nLives left: {self.pacman.lives}\nYOU HAVE COMPLETED THE GAME!"

    def draw(self):
        """
        Draws all game elements.
        """
        pyxel.cls(0)

        if self.game_state == "playing":
            self.maze.draw()
            self.pacman.draw()

            for ghost in self.ghosts:
                ghost.draw()

            for dot in self.dots:
                if not dot.eaten:
                    dot.draw()

            for pellet in self.pellets:
                if not pellet.eaten:
                    pellet.draw()

            self.draw_score()
            self.draw_lives()

        elif self.game_state in ["level_complete", "game_over", "win"]:
            self.draw_final_screen()

    def draw_score(self):
        """
        Draws the score and level at the top center.
        """
        score_text = f"SCORE: {self.pacman.score} LEVEL: {self.level_number}"
        text_x = 110 - len(score_text)
        text_y = 5
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                pyxel.text(text_x + dx, text_y + dy, score_text, 0)
        pyxel.text(text_x, text_y, score_text, 7)

    def draw_lives(self):
        """
        Draws remaining lives at the top left.
        """
        for i in range(self.pacman.lives):
            pyxel.blt(
                10 + i * 10, 1, 2, 0, 16, 8, 8, pyxel.COLOR_BLACK,
            )

    def draw_final_screen(self):
        """
        Draws the final screen based on the game state.
        """
        pyxel.cls(0)
        lines = self.final_message.split("\n")

        screen_height = pyxel.height
        total_text_height = len(lines) * 10 + 20
        y_offset = (screen_height - total_text_height) // 2

        for line in lines:
            text_width = len(line) * pyxel.FONT_WIDTH
            x_offset = (pyxel.width - text_width) // 2
            pyxel.text(x_offset, y_offset, line, pyxel.frame_count % 16)
            y_offset += 10

        next_message = "Press Enter to continue" if self.game_state == "level_complete" else "Press Enter to quit"
        text_width = len(next_message) * pyxel.FONT_WIDTH
        x_offset = (pyxel.width - text_width) // 2
        pyxel.text(x_offset, y_offset + 20, next_message, 7)
