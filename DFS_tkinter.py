#problem
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self, edges):
        self.adj_list = {}
        for start, end in edges:
            if start not in self.adj_list:
                self.adj_list[start] = []
            self.adj_list[start].append(end)

    def dfs(self, start):
        visited = set()
        stack = [start]
        traversal = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                if vertex in self.adj_list:
                    stack.extend(reversed(self.adj_list[vertex]))

        return traversal


class App:
    def __init__(self, master, edges):
        self.graph = Graph(edges)

        self.label = tk.Label(master, text="Select a node:", font=("Arial", 8), height=3)
        self.label.pack()

        self.selected_node = tk.StringVar()
        self.selected_node.set(list(self.graph.adj_list.keys())[0])

        self.nodes_menu = tk.OptionMenu(master, self.selected_node, *self.graph.adj_list.keys())
        self.nodes_menu.pack()

        self.result_label = tk.Label(master, text="", width=500, height=3)
        self.result_label.pack()

        self.submit_button = tk.Button(master, text="Run DFS", command=self.run_dfs)
        self.submit_button.pack()

        self.graph_figure = plt.figure(figsize=(6, 4))
        self.graph_canvas = FigureCanvasTkAgg(self.graph_figure, master=master)
        self.graph_canvas.get_tk_widget().pack()

    def run_dfs(self):
        start_node = self.selected_node.get()
        dfs_result = self.graph.dfs(start_node)
        self.result_label.config(text=f"DFS result: {' '.join(dfs_result)}")

        # Create a graph visualization
        G = nx.DiGraph()
        G.add_edges_from(edges)

        # Clear previous graph
        self.graph_figure.clear()

        # Draw the graph
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrowsize=12, font_size=10)

        # Update the canvas
        self.graph_canvas.draw()


if __name__ == "__main__":
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("C", "F"), ("E", "G")]
    root = tk.Tk()
    root.title("DFS Algorithm")
    root.geometry("600x500")
    app = App(root, edges)
    root.mainloop()