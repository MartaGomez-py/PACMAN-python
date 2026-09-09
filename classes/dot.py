# Dot class (Normal dots)
import pyxel

class Dot:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._eaten = False

    def draw(self):
        """
        Draws the dot if it has not been eaten.
        """
        if not self.eaten:
            sprite_size = 2  # Dot size
            pyxel.blt(
                self.x, self.y,
                2,  # Image bank index (2)
                0, 0,  # Coordinates in the image bank
                sprite_size, sprite_size,  # Sprite size
                pyxel.COLOR_BLACK  # Transparency color
            )

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def eaten(self):
        return self._eaten

    @eaten.setter
    def eaten(self, value):
        self._eaten = value


# PowerPellet class (Special dots)
class PowerPellet(Dot):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._eaten = False

    def draw(self):
        """
        Draws the PowerPellet if it has not been eaten.
        """
        if not self.eaten:
            sprite_size = 8  # PowerPellet size
            pyxel.blt(
                self.x - sprite_size // 2,  # Center horizontally
                self.y - sprite_size // 2,  # Center vertically
                2,  # Image bank index (2)
                0,  # X coordinate in the sprite sheet
                8,  # Y coordinate in the sprite sheet (row for PowerPellets)
                sprite_size, sprite_size,  # Sprite size
                pyxel.COLOR_BLACK  # Transparency color
            )
