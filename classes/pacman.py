import pyxel
from character import Character

# PacMan class, inherits from Character
class PacMan(Character):
    def __init__(self, x, y, speed=2):
        super().__init__(x, y, speed)
        self._lives = 3
        self._score = 0
        self.frame = 0  # Frame counter for animation
        self.direction = None  # Current direction ('RIGHT', 'LEFT', 'UP', 'DOWN')

    def move(self, maze):
        """
        Moves Pac-Man based on the current direction and keyboard input.
        """
        # Detect pressed keys to update direction
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.direction = 'RIGHT'
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.direction = 'LEFT'
        elif pyxel.btn(pyxel.KEY_UP):
            self.direction = 'UP'
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.direction = 'DOWN'

        # Calculate the next position based on the current direction
        next_x, next_y = self.x, self.y
        if self.direction == 'RIGHT':
            next_x += self.speed
        elif self.direction == 'LEFT':
            next_x -= self.speed
        elif self.direction == 'UP':
            next_y -= self.speed
        elif self.direction == 'DOWN':
            next_y += self.speed

        # Convert the proposed coordinates to grid cells
        grid_x = next_x // maze.cell_size
        grid_y = next_y // maze.cell_size

        # Check if the cell is walkable
        if maze.is_walkable(grid_x, grid_y):
            self.x, self.y = next_x, next_y
        else:
            # Stop if hitting a wall
            self.direction = None

    def check_collision(self, obj, obj_size=8):
        """
        Checks if Pac-Man collides with another object.
        Parameters:
            obj: The object to check collision with (must have x and y attributes).
            obj_size: The size of the object. Default is 8.
        """
        pacman_size = 16  # Fixed size of Pac-Man
        return (
                abs(self.x - obj.x) < (pacman_size + obj_size) // 2 and
                abs(self.y - obj.y) < (pacman_size + obj_size) // 2
        )

    def draw(self):
        """
        Draws Pac-Man, animating between sprites based on the direction.
        """
        sprite_size = 16  # Size of each sprite

        # Determine the sprite row based on direction
        direction_map = {
            'RIGHT': 0,
            'LEFT': 16,
            'DOWN': 32,
            'UP': 48
        }
        sprite_y = direction_map.get(self.direction, 0)

        # Alternate between sprites (mouth open, half open, closed)
        sprite_x = (self.frame // 5 % 3) * sprite_size
        self.frame += 1  # Increment frame counter for animation

        # Draw the correct sprite
        pyxel.blt(
            self.x - sprite_size // 2,  # Center sprite on X
            self.y - sprite_size // 2,  # Center sprite on Y
            0,  # Image bank (0)
            sprite_x, sprite_y,  # Sprite coordinates in the bank
            sprite_size, sprite_size,  # Sprite size
            pyxel.COLOR_BLACK  # Transparency color
        )

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        self._lives = max(0, value)  # Ensure lives don't go below 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = max(0, value)  # Ensure score doesn't go below 0
