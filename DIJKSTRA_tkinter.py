 #     0  1  2  3
 #  0  0  1  1  0
#   1  1  0  1  1
#   2  1  1  0  1
#   3  0  1  1  0
#0010213140
import tkinter as tk
from tkinter import ttk

def dijkstra_algorithm(adj_matrix, start_vertex):
    # Get the number of vertices in the graph
    num_vertices = len(adj_matrix)
    
    # Initialize the distance dictionary with infinity values for all vertices
    distances = {vertex: float('infinity') for vertex in range(num_vertices)}
    
    # Set the distance of the starting vertex to 0
    distances[start_vertex] = 0
    
    # Create a set to hold all unvisited vertices
    unvisited_vertices = set(range(num_vertices))
    
    while unvisited_vertices:
        # Get the vertex with the smallest distance
        current_vertex = min(unvisited_vertices, key=lambda vertex: distances[vertex])
        
        # Remove the current vertex from the set of unvisited vertices
        unvisited_vertices.remove(current_vertex)
        
        # Check all neighbors of the current vertex
        for neighbor_vertex in range(num_vertices):
            # If the neighbor is not unvisited, continue
            if neighbor_vertex not in unvisited_vertices:
                continue
            
            # Calculate the distance to the neighbor through the current vertex
            tentative_distance = distances[current_vertex] + adj_matrix[current_vertex][neighbor_vertex]
            
            # If the tentative distance is less than the current distance, update the distance
            if tentative_distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = tentative_distance
    
    return distances

def submit():
    # Get the adjacency matrix and start vertex from the user input
    adj_matrix_str = adj_matrix_entry.get("1.0", tk.END)
    start_vertex = int(start_vertex_entry.get())
    
    # Convert the adjacency matrix string to a list of lists
    adj_matrix = [list(map(int, row.split())) for row in adj_matrix_str.strip().split("\n")]
    
    # Run the Dijkstra algorithm and display the result
    result = dijkstra_algorithm(adj_matrix, start_vertex)
    result_label.config(text=str(result))

# Create the Tkinter window
window = tk.Tk()
window.geometry("400x300")
window.title("Dijkstra Algorithm")

# Create the adjacency matrix label and entry
adj_matrix_label = ttk.Label(window, text="Enter the adjacency matrix:")
adj_matrix_label.pack()
adj_matrix_entry = tk.Text(window, width=50, height=10)
adj_matrix_entry.pack()

# Create the start vertex label and entry
start_vertex_label = ttk.Label(window, text="Enter the start vertex:")
start_vertex_label.pack()
start_vertex_entry = ttk.Entry(window)
start_vertex_entry.pack()

# Create the submit button
submit_button = ttk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Create the result label
result_label = ttk.Label(window)
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
