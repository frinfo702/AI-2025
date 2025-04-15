import matplotlib.pyplot as plt
import numpy as np


def make_reversed_maze(maze: np.ndarray) -> np.ndarray:
    height, width = maze.shape

    reversed_maze = np.array([[0 for _ in range(height)] for _ in range(width)])
    # 上下反転
    for row in range(height):
        for col in range(width):
            reversed_maze[height - 1 - row][col] = maze[row][col]

    return reversed_maze


def plot_maze(maze: np.ndarray, save_file=None):
    height, width = maze.shape
    plt.imshow(maze, cmap="binary")
    plt.gca().set_aspect("equal")
    plt.xticks(rotation=90)
    plt.xticks(np.arange(width), np.arange(width))
    plt.yticks(np.arange(height), np.arange(height))
    if save_file is not None:
        plt.savefig(save_file)
    plt.show()


if __name__ == "__main__":
    file = "sample_maze.txt"
    if input("この迷路を保存しますか? (y/n) >> ") == "y":
        base_name = file.split(".")[0]
        maze = np.loadtxt(file)
        name = f"reversed_{base_name}"
        reversed_maze = make_reversed_maze(maze)
        np.savetxt(f"{name}.txt", reversed_maze, fmt="%d")
        plot_maze(
            reversed_maze, save_file=f"{name}.png"
        )  # Save plot with .png extension
        print(f"作成した迷路を{name}.pngと{name}.txtに保存しました")
    print()
