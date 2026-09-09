from ghost import Ghost

class Clyde(Ghost):
    def __init__(self, x, y, speed=1):
        """
        Initializes Clyde (orange ghost) at the starting position.
        """
        super().__init__(x, y, "ORANGE", speed)
        self.in_box = True  # Indicates if Clyde is still in the starting box
        self.aligned_to_exit = False  # Indicates if Clyde is aligned with the box exit

    def move(self, maze):
        """
        Manages Clyde's movement.
        """
        if self.in_box:
            # Initial movement to exit the box
            self.leave_box(maze)
        else:
            # Perform random movement controlled by a timer
            self.timed_random_move(maze)

