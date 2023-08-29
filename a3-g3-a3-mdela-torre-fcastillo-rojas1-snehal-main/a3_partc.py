
import random
from a2d import Graph
from a3_partb import minimum_spanning_tree
from a3_maze import Maze

def generate_maze(number_of_rows, number_of_columns):
    cell_length = number_of_columns * number_of_rows
    walls = []

    # Generate all possible walls between cells
    for i in range(cell_length):
        # checking the right side of the cell if it exists.
        if (i + 1) % number_of_columns != 0:
            walls.append((i, i + 1))
        
        # checking the bottom cell if it exists.
        if (i + number_of_columns) < cell_length:
            walls.append((i, i + number_of_columns))

    maze_walls = walls[:]  # Copy the list of walls

    # Randomly shuffle the list of walls
    random.shuffle(maze_walls)

    return maze_walls

 def r_weight():
		return random.randrange(1,50)

	cell_length = number_of_columns * number_of_rows
	graph = Graph(cell_length)
	walls = []

	for i in range(cell_length):
		# checking the right side of the cell if it exist.
		if( i + 1 ) % number_of_columns != 0 :
			weight = r_weight()
			walls.append((i, i+1))
			graph.add_edge(i, i+1, weight)
			graph.add_edge(i+1, i, weight)
		
		#checking the bottom number exist.
		if( i + number_of_columns ) < cell_length:
			weight = r_weight()
			walls.append( (i, i + number_of_columns) )
			graph.add_edge( i, i + number_of_columns, weight )
			graph.add_edge( i + number_of_columns, i, weight )
	
	walls_to_remove = minimum_spanning_tree(graph)

	maze_walls = []
	for wall in walls:
		if wall not in walls_to_remove:
			maze_walls.append(wall)
	
	return maze_walls


	#  Code by Snehal for the maze, done afterwards 

# 	import random
# from a2d import Graph
# from a3_partb import minimum_spanning_tree

# def generate_maze(number_of_rows, number_of_columns):
#     def r_weight():
#         return random.randrange(1, 50)

#     cell_length = number_of_columns * number_of_rows
#     graph = Graph(cell_length)
#     walls = [(i, i+1) for i in range(cell_length) if (i+1) % number_of_columns != 0]
#     walls += [(i, i + number_of_columns) for i in range(cell_length) if (i + number_of_columns) < cell_length]

#     for wall in walls:
#         weight = r_weight()
#         graph.add_edge(wall[0], wall[1], weight)
#         graph.add_edge(wall[1], wall[0], weight)

#     walls_to_remove = minimum_spanning_tree(graph)

#     maze_walls = [wall for wall in walls if wall not in walls_to_remove]
#     return maze_walls
