#changed not sure
import tkinter as tk
from tkinter import messagebox

def prim_algorithm():
    n = int(n_entry.get())
    # Convert the incidence matrix from the user input to a 2D list
    incidence_matrix = [[int(x) for x in row.split()] for row in matrix_entry.get("1.0", "end-1c").split("\n")]
    # Initialize the minimum weight spanning tree and set of unvisited vertices
    mst = []
    unvisited = set(range(n))
    # Choose an arbitrary vertex to start from
    start_vertex = 0
    unvisited.remove(start_vertex)
    while unvisited:
        # Find the edge with the minimum weight between a visited and an unvisited vertex
        min_weight = float("inf")
        for i in range(n):
            if i not in unvisited:
                continue
            for j in range(n):
                if j in unvisited and incidence_matrix[i][j] < min_weight:
                    min_weight = incidence_matrix[i][j]
                    edge = (i, j, min_weight)
        # Add the edge to the minimum weight spanning tree and mark the end vertex as visited
        mst.append(edge)
        unvisited.remove(edge[1])
    # Calculate the total weight of the minimum weight spanning tree
    mst_weight = sum(edge[2] for edge in mst)
    # Display the minimum weight spanning tree and its total weight
    mst_output.config(state="normal")
    mst_output.delete("1.0", "end")
    mst_output.insert("1.0", f"Minimum Weight Spanning Tree:\n")
    for edge in mst:
        mst_output.insert("end", f"{edge[0]+1} - {edge[1]+1}: {edge[2]}\n")  # Add 1 to the vertices for display
    mst_output.insert("end", f"Total weight: {mst_weight}")
    mst_output.config(state="disabled")

# Create the Tkinter GUI
root = tk.Tk()
root.title("Prim's Algorithm")

# Create the input widgets
n_label = tk.Label(root, text="Number of vertices:")
n_label.pack()
n_entry = tk.Entry(root)
n_entry.pack()

matrix_label = tk.Label(root, text="Incidence matrix (space separated):")
matrix_label.pack()
matrix_entry = tk.Text(root, height=10)
matrix_entry.pack()

submit_button = tk.Button(root, text="Submit", command=prim_algorithm)
submit_button.pack()

# Create the output widgets
mst_output = tk.Text(root, height=10, state="disabled")
mst_output.pack()

root.mainloop()