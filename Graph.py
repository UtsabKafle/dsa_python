class Graph:
    def __init__(self, edges):
        """
        Initialize the graph with edges.
        """
        self.edges = edges
        self.graph = {}
        for source, destination in self.edges:
            if source in self.graph:
                self.graph[source].append(destination)
            else:
                self.graph[source] = [destination]

    def find_path(self, start, end):
        """
        Find a path from start to end in the graph using depth-first search.
        """
        if start not in self.graph or end not in self.graph:
            print("Start or end node not found in the graph.")
            return []

        return self._dfs(start, end, [])

    def _dfs(self, current, end, visited):
        """
        Perform depth-first search to find a path from current node to the end node.
        """
        visited.append(current)

        if current == end:
            return visited

        if current in self.graph:
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    path = self._dfs(neighbor, end, visited.copy())
                    if path:
                        return path

        return []


def main():
    routes = [
        ('a', 'b'),
        ('b', 'c'),
        ('b', 'd'),
        ('d', 'i'),
        ('d', 'v'),
    ]
    graph = Graph(routes)

    start_node = 'a'
    end_node = 'c'
    print(f"Path from {start_node} to {end_node}: {graph.find_path(start_node, end_node)}")


if __name__ == "__main__":
    main()
