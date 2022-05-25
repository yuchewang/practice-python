from collections import defaultdict

class DirectedGraph:
    def __init__(self, adj_list = defaultdict(set)):
        self.adjacency_list = adj_list

    def add_edge(self, source, destination):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = set()

        self.adjacency_list[source].add(destination)

    def get_neighbor(self, vertex):
        if vertex in self.adjacency_list:
            for v in self.adjacency_list[vertex]:
                yield v
    
    def get_vertex(self):
        for v in self.adjacency_list:
            yield v
    
    def print_graph(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(vertex, end=": ")
            for neighbor in neighbors:
                print(neighbor, end =", ")
            print("")
    
    def dfs_iteration(self, vertex, visited = set()):
        stack = []
        stack.append(vertex)
        while stack:
            vertex = stack.pop()
            visited.add(vertex)
            print(vertex, end = "->")
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    def dfs_recursion(self, vertex, visited = set()):
        if vertex in visited:
            return
        visited.add(vertex)
        print(vertex, end = "->")
        for neighbor in self.adjacency_list[vertex]:
            self.dfs_recursion(neighbor, visited)
        
    def bfs(self, vertex, visited = set()):
        queue = []
        queue.append(vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end= "->")
            for neighbor in self.adjacency_list[vertex]:
                queue.append(neighbor)

def get_test_graph_1():
    dg = DirectedGraph()
    dg.add_edge(0, 1)
    dg.add_edge(0, 2)
    dg.add_edge(1, 3)
    dg.add_edge(1, 4)
    dg.add_edge(2, 5)
    dg.add_edge(2, 6)
    dg.add_edge(3, 7)
    dg.add_edge(3, 8)
    dg.add_edge(4, 9)
    dg.add_edge(4, 10)

    return dg

if __name__ == "__main__":
    g = get_test_graph_1()
    g.print_graph()
    g.dfs_iteration(0)
    print("")
    g.dfs_recursion(0)
    print("")
    g.bfs(0)