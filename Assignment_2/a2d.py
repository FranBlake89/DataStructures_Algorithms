class Graph:

	def __init__(self,number_of_verts):
		self.vertices = tuple([] for _ in range(number_of_verts))
		self.edges = []
		self.edge_weights = []


	def add_vertex(self):
		self.vertices = self.vertices + ([], )

	def add_edge(self,from_idx, to_idx, weight = 1 ):
		if not (self.is_valid_vertex(from_idx)) or not(self.is_valid_vertex(to_idx)):
			return False
		
		if self.has_edge(from_idx, to_idx):
			return False

		self.edges.append((from_idx, to_idx))
		self.edge_weights.append(weight)
		return True

	def num_edges(self):
		return len(self.edges)

	def num_verts(self):
		return len(self.vertices)

	def has_edge(self, from_idx,to_idx):
		#Vertices are invalid
		if not (self.is_valid_vertex(from_idx)) or not (self.is_valid_vertex(from_idx)):
			return False

		return (from_idx, to_idx) in self.edges


	def edge_weight(self, from_idx,to_idx):
		if (self.is_valid_vertex(from_idx)) and (self.is_valid_vertex(to_idx)) and (self.has_edge(from_idx, to_idx)):
			for i in range(len(self.edges)):
				if self.edges[i][0] == from_idx and self.edges[i][1] == to_idx:
					return self.edge_weights[i]

	def get_connected(self, v):
		if not (self.is_valid_vertex(v)):
			return None
		
		for i in range(len(self.edges)):
			if self.edges[i][0] == v:
				self.vertices[v].append((self.edges[i][1], self.edge_weights[i]))
		return self.vertices[v]

	def is_valid_vertex(self, vertex_idx):
		return 0 <= vertex_idx < len(self.vertices)