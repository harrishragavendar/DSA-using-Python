from collections import defaultdict


class UGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)
    
    def __str__(self):
        return str([f"{vertex} -> {neighbors}" for vertex, neighbors in self.adj_list.items()])
    
    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        try:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)

        except ValueError:
            print("Edge doesn't exist in graph")
    
ugraph = UGraph()
ugraph.add_edge(1, 2)
ugraph.add_edge(2, 3)
ugraph.add_edge(1, 4)

print(ugraph)

ugraph.remove_edge(4, 1)

print(ugraph)

ugraph.remove_edge(4, 1)