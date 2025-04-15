import numpy as np


def make_reversed_maze(maze: np.ndarray) -> np.ndarray:
    height, width = maze.shape

    reversed_maze = np.array([[0 for _ in range(height)] for _ in range(width)])
    # 上下反転
    for row in range(height):
        for col in range(width):
            reversed_maze[height - 1 - row][col] = maze[row][col]

    return reversed_maze
