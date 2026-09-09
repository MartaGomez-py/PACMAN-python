# Base class for characters
class Character:
    def __init__(self, x, y, speed):
        self.initial_position = (x, y)
        self._x = x
        self._y = y
        self._speed = speed

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        """
        Updates the x position and checks if the character should cross a tunnel.
        """
        tunnel_x_left = 1  # Coordinate for the left tunnel
        tunnel_x_right = 222  # Coordinate for the right tunnel
        tunnel_y_range = (108, 123)  # Y-coordinate range for the tunnel

        # Check if the character is within the Y range of the tunnel
        if tunnel_y_range[0] <= self.y <= tunnel_y_range[1]:
            if value <= tunnel_x_left:  # Exiting through the left tunnel
                self._x = tunnel_x_right
            elif value >= tunnel_x_right:  # Exiting through the right tunnel
                self._x = tunnel_x_left
            else:
                self._x = value
        else:
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    def reset_position(self):
        """
        Resets the character to its initial position.
        """
        self.x, self.y = self.initial_position  # Return to the initial position
