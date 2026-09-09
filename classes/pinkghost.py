from ghost import Ghost

class Pinky(Ghost):
    def __init__(self, x, y, speed=1):
        """
        Initializes Pinky (pink ghost) at the starting position.
        """
        super().__init__(x, y, "PINK", speed)
        self.recalculation_timer = 0  # Timer to recalculate the target
        self.in_box = True  # Indicates if Pinky is in the starting box
        self.aligned_to_exit = False  # Indicates if Pinky is aligned with the exit

    def move(self, maze, pacman):
        """
        Updates Pinky's movement toward the ambush position.
        """
        if self.in_box:
            self.leave_box(maze)
        else:
            # Avoid moving downward after leaving the box
            if not self.in_box:
                if 112 > self.x < 120:
                    directions = [(0, -1), (-1, 0),
                                  (1, 0)]  # Up, Left, Right
                else:

                    directions = [(0, -1), (0, 1), (-1, 0),
                                  (1, 0)]  # Up, Down, Left, Right

            # Recalculate target every few frames
            self.recalculation_timer -= 1
            if self.recalculation_timer <= 0:
                self.target_x, self.target_y = self.calculate_ambush_target(
                    pacman, maze)
                self.recalculation_timer = 15  # Recalculate every 15 frames

            # Convert the target to pixel coordinates
            target_pixel_x = self.target_x * maze.cell_size
            target_pixel_y = self.target_y * maze.cell_size

            # Incremental movement toward the target
            dx, dy = 0, 0
            if self.x < target_pixel_x:
                dx = self.speed
            elif self.x > target_pixel_x:
                dx = -self.speed
            if self.y < target_pixel_y:
                dy = self.speed
            elif self.y > target_pixel_y:
                dy = -self.speed

            # Check valid movement
            next_x = self.x + dx
            next_y = self.y + dy

            # Try primary direction
            if maze.is_walkable(next_x // maze.cell_size,
                                self.y // maze.cell_size):
                self.x = next_x
            elif maze.is_walkable(self.x // maze.cell_size,
                                  next_y // maze.cell_size):
                self.y = next_y
            else:
                # Attempt alternative directions without using break
                alternative_direction = next(
                    ((alt_dx, alt_dy) for alt_dx, alt_dy in
                     [(self.speed, 0), (-self.speed, 0), (0, self.speed),
                      (0, -self.speed)]
                     if maze.is_walkable((self.x + alt_dx) // maze.cell_size,
                                         (self.y + alt_dy) // maze.cell_size)),
                    (0, 0)
                )
                self.x += alternative_direction[0]
                self.y += alternative_direction[1]
