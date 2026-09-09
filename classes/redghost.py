from ghost import Ghost

class Blinky(Ghost):
    def __init__(self, x, y, speed=1):
        """
        Initializes Blinky (red ghost) at the starting position.
        """
        super().__init__(x, y, "RED", speed)
        self.path = []  # Current path to follow

    def move(self, maze, pacman):
        """
        Updates Blinky's movement towards Pac-Man in a smooth manner.
        """
        # Recalculate the path if there's no path or the target has changed
        if not self.path or (pacman.x // maze.cell_size, pacman.y // maze.cell_size) != (self.target_x, self.target_y):
            self.path = self.find_path_to_pacman(maze, pacman)

            if self.path:
                self.target_x, self.target_y = self.path.pop(0)  # Next cell in the path
                self.target_x *= maze.cell_size
                self.target_y *= maze.cell_size

        # Move towards the target
        if self.target_x is not None and self.target_y is not None:
            if self.x < self.target_x:
                self.x += self.speed
            elif self.x > self.target_x:
                self.x -= self.speed

            if self.y < self.target_y:
                self.y += self.speed
            elif self.y > self.target_y:
                self.y -= self.speed

            # If the target cell is reached, move to the next one
            if self.x == self.target_x and self.y == self.target_y:
                if self.path:
                    self.target_x, self.target_y = self.path.pop(0)
                    self.target_x *= maze.cell_size
                    self.target_y *= maze.cell_size
