class Graph:
	def __init__(self,edges):
		self.edges = edges
		self.graph = {}
		for a,b in self.edges:
			if a in self.graph:
				self.graph[a].append(b)
			else:
				self.graph[a] = [b]
		print(self.graph)

	def path_(self,start,end):
			# a-c -> [b,c]
			# a-v -> [b,d,v]
		
			path = []
			for i in self.graph[start]:
				if i == end:
					path.append(i)
					return path
				else:
					if i in self.graph:
						for j in self.graph[i]:
							path += self.path_(j,end)
			return path



def main():
	routes = [
		('a','b'),
		('b','c'),
		('b','d'),
		('d','i'),
		('d','v'),
	]
	graph = Graph(routes)
	print(graph.path_(start='a',end='c'))

if __name__ == "__main__":
	main()
