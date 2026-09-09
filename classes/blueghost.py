
from ghost import Ghost
import random

class Inky(Ghost):
    def __init__(self, x, y, speed=1):
        """
        Initializes Inky (blue ghost) in the starting position.
        """
        super().__init__(x, y, "BLUE", speed)
        self.mode = "RANDOM"  # Inky starts in random mode
        self.mode_timer = random.randint(200,400)  # Timer to alternate modes
        self.path = []  # Current path towards Pac-Man in chase mode

    def switch_mode(self):
        """
            Switches between random mode and chase mode.
        """
        if self.mode == "RANDOM":
            self.mode = "CHASE"
        else:
            self.mode = "RANDOM"
        self.mode_timer = random.randint(200, 400)  # Reinicia el temporizador

    def move(self, maze, pacman):
        """
        Manages Inky's movement, ensuring he doesn't re-enter the box.
        """
        # Verify if Blinky is in the box
        if self.in_box:
            self.leave_box(maze)
        else:
            # prevents Blinky from reentering the box
            if not self.in_box:
                if 112>self.x<120:
                    directions = [(0, -1), (-1, 0),
                                  (1, 0)]  # Up, Left, Right
                else:

                    directions = [(0, -1), (0, 1), (-1, 0),
                              (1, 0)]  # Up, Down, Left, Right


            # Alternate between modes
            self.mode_timer -= 1
            if self.mode_timer <= 0:
                self.switch_mode()

            if self.mode == "RANDOM":
                self.timed_random_move(maze)
            elif self.mode == "CHASE":
                self.chase_pacman(maze, pacman)


    def chase_pacman(self, maze, pacman):
        """
        Chases Pac-Man
        """
        # Si no hay un camino o el objetivo cambia, recalcularlo
        if not self.path or (
        pacman.x // maze.cell_size, pacman.y // maze.cell_size) != (
        self.target_x, self.target_y):
            self.path = self.find_path_to_pacman(maze, pacman)

            if self.path:
                self.target_x, self.target_y = self.path.pop(
                    0)  # Siguiente celda del camino
                self.target_x *= maze.cell_size
                self.target_y *= maze.cell_size

        # Mover hacia el objetivo
        if self.target_x is not None and self.target_y is not None:
            if self.x < self.target_x:
                self.x += self.speed
            elif self.x > self.target_x:
                self.x -= self.speed

            if self.y < self.target_y:
                self.y += self.speed
            elif self.y > self.target_y:
                self.y -= self.speed

            # Si alcanzamos la celda objetivo, pasar a la siguiente
            if self.x == self.target_x and self.y == self.target_y:
                if self.path:
                    self.target_x, self.target_y = self.path.pop(0)
                    self.target_x *= maze.cell_size
                    self.target_y *= maze.cell_size