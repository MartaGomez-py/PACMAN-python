# Maze class

import pyxel

class Maze:
    def __init__(self, layout, cell_size=8):
        """
        layout: A list of strings defining the maze.
        cell_size: Size of each cell in pixels.
        """
        self.layout = layout
        self.cell_size = cell_size
        self.width = len(layout[0]) * cell_size
        self.height = len(layout) * cell_size

    def is_walkable(self, grid_x, grid_y):
        """
        Returns True if the cell at (grid_x, grid_y) is not a wall.
        """
        if 0 <= grid_y < len(self.layout) and 0 <= grid_x < len(
                self.layout[0]):
            return self.layout[grid_y][grid_x] != "#"
        return False

    def draw(self):
        """
        Draws the maze background from sheet 2 in the image bank.
        """
        # Draw the entire image sheet (sheet 2 is bank 1)
        pyxel.blt(0, 0, 1, 0, 0, pyxel.width, pyxel.height)
