#      0  1  2  3
#     ___________
#  0 | 0  1  0  1
#  1 | 1  0  1  0
#  2 | 0  1  0  1
#  3 | 1  0  1  0
#0321
#465
#7
 
import tkinter as tk

def kosaraju(adj_matrix):
    # Perform first DFS to get finishing times
    visited = [False] * len(adj_matrix)
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor in range(len(adj_matrix[node])):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    for node in range(len(adj_matrix)):
        if not visited[node]:
            dfs(node)

    # Perform second DFS to get SCCs
    visited = [False] * len(adj_matrix)
    sccs = []

    def dfs_scc(node, scc):
        visited[node] = True
        scc.append(node)
        for neighbor in range(len(adj_matrix[node])):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs_scc(neighbor, scc)

    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs_scc(node, scc)
            sccs.append(scc)

    return sccs

def run_kosaraju():
    # Get adjacency matrix from user input
    matrix_str = input_matrix_entry.get('1.0', 'end-1c')
    adj_matrix = [[int(val) for val in row.split()] for row in matrix_str.split('\n')]

    # Run Kosaraju's algorithm
    sccs = kosaraju(adj_matrix)

    # Display SCCs in label
    scc_str = '\n'.join([' '.join([str(node) for node in scc]) for scc in sccs])
    result_label.config(text='Strongly Connected Components:\n' + scc_str)

# Create tkinter window
root = tk.Tk()
root.geometry("400x300")
root.title('Kosaraju Algorithm')

# Create entry for adjacency matrix
matrix_label = tk.Label(root, text='Enter adjacency matrix (separate values with space, rows with newline):')
matrix_label.pack()
input_matrix_entry = tk.Text(root, width=50, height=10)
input_matrix_entry.pack()

# Create button to run algorithm
run_button = tk.Button(root, text='Run', command=run_kosaraju)
run_button.pack()

# Create label to display result
result_label = tk.Label(root, text='')
result_label.pack()

root.mainloop()
