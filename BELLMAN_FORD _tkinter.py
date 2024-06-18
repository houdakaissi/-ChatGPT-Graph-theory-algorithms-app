# 0  1  0  1
# 1  0  1  0
# 0  1  0  1
# 1  0  1  0
# [[0,1,2,3,5],
         # [2,0,-1,1,-1],
          #[1,6,0,13,2],
         # [1,2,1,0,-1],
         # [3,3,2,4,0]]
         #numof columsrows

import tkinter as tk

def bellman_ford(graph, start_node):
    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    distances[start_node] = 0

    # Relax edges repeatedly
    for _ in range(num_nodes - 1):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if graph[i][j] != float('inf'):
                    if distances[j] > distances[i] + graph[i][j]:
                        distances[j] = distances[i] + graph[i][j]
    
    # Check for negative cycles
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph[i][j] != float('inf'):
                if distances[j] > distances[i] + graph[i][j]:
                    return "Negative cycle detected!"
    
    return distances

def submit():
    # Get the input values from the Entry widgets
    matrix_input = adjacency_matrix_entry.get('1.0', tk.END)
    start_node = int(start_node_entry.get())

    # Parse the adjacency matrix
    matrix_rows = matrix_input.split('\n')
    adjacency_matrix = []
    for row in matrix_rows:
        if row:
            row_values = [int(val) if val != 'inf' else float('inf') for val in row.split()]
            adjacency_matrix.append(row_values)

    # Run the Bellman-Ford algorithm and display the result
    result = bellman_ford(adjacency_matrix, start_node)
    result_label.config(text=result)

# Create the tkinter GUI
root = tk.Tk()
root.title("Bellman-Ford Algorithm")
root.geometry("400x300")

# Create the input widgets
adjacency_matrix_label = tk.Label(root, text="Adjacency Matrix")
adjacency_matrix_label.grid(row=0, column=0)
adjacency_matrix_entry = tk.Text(root, height=10, width=50)
adjacency_matrix_entry.grid(row=1, column=0)

start_node_label = tk.Label(root, text="Start Node")
start_node_label.grid(row=2, column=0)
start_node_entry = tk.Entry(root)
start_node_entry.grid(row=3, column=0)

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0)

# Create the result label
result_label = tk.Label(root)
result_label.grid(row=5, column=0)

root.mainloop()
