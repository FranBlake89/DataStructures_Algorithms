from a2d import Graph
# add imports for your DisjointSet or MinHeap as you see fit
from a3_parta import MinHeap

def minimum_spanning_tree(graph):
    # Helper function to add neighboring edges to the min heap
    def add_edges_to_heap(node, visited, heap):
        visited[node] = True
        connected_vertices = graph.get_connected(node)
        for neighbor, weight in connected_vertices:
            if not visited[neighbor]:
                heap.insert((weight, node, neighbor))

    # Initialize data structures
    num_vertices = graph.num_verts()
    visited = [False] * num_vertices
    mst_edges = []

    # Start from vertex 0
    start_vertex = 0
    min_heap = MinHeap()
    add_edges_to_heap(start_vertex, visited, min_heap)

    while not min_heap.is_empty():
        weight, src, dest = min_heap.extract_min()
        if not visited[dest]:
            # Add the edge to the MST
            mst_edges.append( (min(src, dest), max(src, dest)) )
            # Add neighboring edges of the destination to the min heap
            add_edges_to_heap(dest, visited, min_heap)

    return mst_edges
