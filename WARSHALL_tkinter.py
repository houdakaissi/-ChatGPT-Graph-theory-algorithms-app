# 0  1  0  1
# 0  0  1  0
# 0  0  0  1
# 0  0  0  0
#make sure  

import tkinter as tk

def warshall_algorithm(adj_matrix):
    n = len(adj_matrix)
    transitive_closure = adj_matrix.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                transitive_closure[i][j] = transitive_closure[i][j] or (transitive_closure[i][k] and transitive_closure[k][j])
    return transitive_closure

def show_result():
    # Get input values from user
    adjacency_list = input_entry.get('1.0', tk.END).split('\n')
    adjacency_list = [row.split() for row in adjacency_list if row]

    # Convert input to adjacency matrix
    n = len(adjacency_list)
    adj_matrix = [[0] * n for _ in range(n)]
    for i, row in enumerate(adjacency_list):
        for j, val in enumerate(row):
            adj_matrix[i][j] = int(val)

    # Compute transitive closure using Warshall algorithm
    transitive_closure = warshall_algorithm(adj_matrix)

    # Display result
    result_label.configure(text=str(transitive_closure))

# Create tkinter window
root = tk.Tk()
root.geometry("400x300")
root.title('Warshall Algorithm')

# Create label and entry for input
input_label = tk.Label(root, text='Enter adjacency matrix:')
input_label.pack()
input_entry = tk.Text(root, height=10, width=50)
input_entry.pack()

# Create button to compute and display transitive closure
compute_button = tk.Button(root, text='Compute', command=show_result)
compute_button.pack()

# Create label to display result
result_label = tk.Label(root, text='')
result_label.pack()

# Run tkinter event loop
root.mainloop()
