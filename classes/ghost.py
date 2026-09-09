import random
import pyxel
from character import Character


class Ghost(Character):
    def __init__(self, x, y, color, speed=1):
        """
        Initialize a ghost with its starting position, color, and speed.
        """
        super().__init__(x, y, speed)
        self.frightened = False
        self.color = color
        self.frame = 0  # Animation frame counter
        self.aligned_to_exit = False  # Indicates alignment with the exit box
        self.in_box = True  # Indicates if the ghost is in the starting box
        self.target_x = None
        self.target_y = None
        self.timer = 100  # Timer for random movement
        self.direction = None

    def draw(self):
        """
        Draws the ghost. Changes appearance if frightened.
        """
        sprite_size = 16

        if self.frightened:
            sprite_x = (self.frame // 10 % 2) * sprite_size
            sprite_y = 128  # Y-coordinate for frightened sprites
        else:
            sprite_x = (self.frame // 10 % 2) * sprite_size
            sprite_y = {
                "RED": 80,
                "PINK": 64,
                "BLUE": 96,
                "ORANGE": 112,
            }[self.color]

        self.frame += 1  # Increment animation frame

        pyxel.blt(
            self.x - sprite_size // 2,
            self.y - sprite_size // 2,
            0,
            sprite_x,
            sprite_y,
            sprite_size,
            sprite_size,
            pyxel.COLOR_BLACK,
        )

    def leave_box(self, maze):
        """
        Hace que Pinky salga de la caja inicial respetando las paredes.
        """
        exit_y = 102 - 8
        exit_x_start = 104 + 8
        exit_x_end = 120 - 8

        if not self.aligned_to_exit:
            if self.x < exit_x_start:
                self.x += self.speed
            elif self.x > exit_x_end:
                self.x -= self.speed
            else:
                self.aligned_to_exit = True
        else:
            next_y = self.y - self.speed
            if maze.is_walkable(self.x // maze.cell_size, next_y // maze.cell_size):
                self.y = next_y
            if self.y <= exit_y:
                self.in_box = False

    def find_path_to_pacman(self, maze, pacman):
        """
        Finds the shortest path to Pac-Man using a basic BFS.
        """
        start = (self.x // maze.cell_size, self.y // maze.cell_size)
        goal = (pacman.x // maze.cell_size, pacman.y // maze.cell_size)

        if start == goal:
            return []  # Already at the target

        open_set = [start]
        came_from = {}
        g_score = {start: 0}
        f_score = {start: self.heuristic(start, goal)}

        while open_set:
            current = min(open_set, key=lambda node: f_score.get(node, float("inf")))

            if current == goal:
                return self._reconstruct_path(came_from, current)

            open_set.remove(current)

            neighbors = [
                (current[0] + dx, current[1] + dy)
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]
            ]

            for neighbor in neighbors:
                if not maze.is_walkable(*neighbor):
                    continue

                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)

                    if neighbor not in open_set:
                        open_set.append(neighbor)

        return []  # No path found

    def heuristic(self, a, b):
        """
        Calculates Manhattan distance between two points.
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _reconstruct_path(self, came_from, current):
        """
        Reconstructs the path from start to target.
        """
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    def calculate_ambush_target(self, pacman, maze, steps_ahead=10):
        """
        Calculates an ambush target position based on Pac-Man's direction.
        """
        pacman_x = pacman.x // maze.cell_size
        pacman_y = pacman.y // maze.cell_size
        direction = pacman.direction

        dx, dy = {
            "RIGHT": (steps_ahead, 0),
            "LEFT": (-steps_ahead, 0),
            "UP": (0, -steps_ahead),
            "DOWN": (0, steps_ahead),
        }.get(direction, (0, 0))

        target_x, target_y = pacman_x + dx, pacman_y + dy

        if not maze.is_walkable(target_x, target_y):
            return pacman_x, pacman_y
        return target_x, target_y

    def timed_random_move(self, maze):
        """
        Moves randomly for a set duration, respecting walls.
        """
        if self.timer <= 0 or self.direction is None:
            directions = [(0, -1), (0, 1), (-1, 0),
                          (1, 0)]  # Up, Down, Left, Right
            while self.x == 116:
                directions = [(0, -1), (-1, 0), (1, 0)]  # Up, Left, Right

            random.shuffle(directions)

            # Find the first valid direction
            valid_direction = None
            for dx, dy in directions:
                next_x = self.x + dx * self.speed
                next_y = self.y + dy * self.speed
                if maze.is_walkable(next_x // maze.cell_size,
                                    next_y // maze.cell_size):
                    valid_direction = (dx, dy)
                    self.timer = random.randint(60,
                                                120)  # Set timer for this direction
                    break  # Exit loop after finding valid direction

            # Update direction if a valid one is found
            self.direction = valid_direction

        if self.direction:
            dx, dy = self.direction
            next_x = self.x + dx * self.speed
            next_y = self.y + dy * self.speed

            if maze.is_walkable(next_x // maze.cell_size,
                                next_y // maze.cell_size):
                self.x = next_x
                self.y = next_y
            else:
                # Reset direction and timer if movement fails
                self.direction = None
                self.timer = 0

        self.timer -= 1


