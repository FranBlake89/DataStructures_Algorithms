
from a3_maze import Maze


def find_path(maze, from_cell, to_cell):
    if from_cell == to_cell:
        return [from_cell]

    maze.mark_cell(from_cell)

    shortest_path = None

    # Check left direction
    next_cell = maze.get_left(from_cell)
    if next_cell != -1 and not maze.get_is_marked(next_cell):
        current_path = find_path(maze, next_cell, to_cell)
        if current_path:
            shortest_path = current_path

    # Check right direction
    next_cell = maze.get_right(from_cell)
    if next_cell != -1 and not maze.get_is_marked(next_cell):
        current_path = find_path(maze, next_cell, to_cell)
        if current_path and (shortest_path is None or len(current_path) < len(shortest_path)):
            shortest_path = current_path

    # Check up direction
    next_cell = maze.get_up(from_cell)
    if next_cell != -1 and not maze.get_is_marked(next_cell):
        current_path = find_path(maze, next_cell, to_cell)
        if current_path and (shortest_path is None or len(current_path) < len(shortest_path)):
            shortest_path = current_path

    # Check down direction
    next_cell = maze.get_down(from_cell)
    if next_cell != -1 and not maze.get_is_marked(next_cell):
        current_path = find_path(maze, next_cell, to_cell)
        if current_path and (shortest_path is None or len(current_path) < len(shortest_path)):
            shortest_path = current_path

    if shortest_path is not None:
        return [from_cell] + shortest_path

    return []
