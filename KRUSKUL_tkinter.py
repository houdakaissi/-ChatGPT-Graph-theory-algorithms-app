#not sure
import tkinter as tk

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edge_weights = {}
        self.vertices = set()

    def add_edge(self, start, end, weight):
        if start not in self.adj_list:
            self.adj_list[start] = []
        if end not in self.adj_list:
            self.adj_list[end] = []

        self.adj_list[start].append(end)
        self.adj_list[end].append(start)

        self.edge_weights[(start, end)] = weight
        self.edge_weights[(end, start)] = weight

        self.vertices.add(start)
        self.vertices.add(end)

    def find(self, parent, vertex):
        if parent[vertex] == vertex:
            return vertex
        return self.find(parent, parent[vertex])

    def union(self, parent, rank, vertex1, vertex2):
        root1 = self.find(parent, vertex1)
        root2 = self.find(parent, vertex2)

        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal(self):
        parent = {}
        rank = {}
        minimum_spanning_tree = []

        for vertex in self.vertices:
            parent[vertex] = vertex
            rank[vertex] = 0

        sorted_edges = sorted(self.edge_weights.keys(), key=lambda x: self.edge_weights[x])  # Sort edges by weight

        for edge in sorted_edges:
            vertex1, vertex2 = edge
            weight = self.edge_weights[edge]
            root1 = self.find(parent, vertex1)
            root2 = self.find(parent, vertex2)

            if root1 != root2:
                self.union(parent, rank, root1, root2)
                minimum_spanning_tree.append((vertex1, vertex2, weight))

        return minimum_spanning_tree

class App:
    def __init__(self, master):
        self.graph = Graph()

        self.label = tk.Label(master, text="Enter edges (start end weight):")
        self.label.pack()

        self.input_entry = tk.Entry(master, width=50)
        self.input_entry.pack()

        self.submit_button = tk.Button(master, text="Add Edge", command=self.add_edge)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="", width=500, height=10)
        self.result_label.pack()

        self.compute_button = tk.Button(master, text="Run Kruskal's Algorithm", command=self.run_kruskal)
        self.compute_button.pack()

    def add_edge(self):
        edge_input = self.input_entry.get().split()
        if len(edge_input) == 3:
            start, end, weight = edge_input
            self.graph.add_edge(start, end, int(weight))
            self.input_entry.delete(0, tk.END)

    def run_kruskal(self):
        minimum_spanning_tree = self.graph.kruskal()
        result = "Minimum Spanning Tree:\n"
        for edge in minimum_spanning_tree:
            result += f"{edge[0]} -- {edge[1]} : {edge[2]}\n"
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Kruskal's Algorithm")
    app = App(root)
    root.mainloop()
