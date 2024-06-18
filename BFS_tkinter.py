#{
 #   'A': ['B', 'C'],
 #   'B': ['A', 'D'],
  #  'C': ['A', 'D'],
   # 'D': ['B', 'C', 'E'],
    #'E': ['D', 'F'],
    #'F': ['E']
#}
#edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("C", "F"), ("E", "G")]

import tkinter as tk
from queue import Queue



def bfs(graph, start):
    visited = {node: False for node in graph}
    queue = Queue()
    queue.put(start)
    visited[start] = True
    traversal=[]
    while not queue.empty():
        node = queue.get()
        traversal.append(node)
        print(node, end=" ")

        for adjacent in graph[node]:
            if not visited[adjacent]:
                visited[adjacent] = True
                queue.put(adjacent)
    return traversal

def start_bfs():
    graph_input = text_area.get("1.0", tk.END).strip()
    graph = eval(graph_input)
    start_node = start_node_entry.get()  
   # start_node = list(graph.keys())[0]
    bfs_result = bfs(graph, start_node)

    result_label.config(text="BFS traversal: " + str(bfs_result))
    
window = tk.Tk()
window.title("BFS Algorithm")
window.geometry("500x400")

label = tk.Label(window, text="Enter graph as adjacency list:")
label.pack()
start_node_label = tk.Label(window, text="Start Node")
start_node_label.pack()

start_node_entry = tk.Entry(window)
start_node_entry.pack()

text_area = tk.Text(window, height=10)
text_area.pack()

start_button = tk.Button(window, text="Start BFS", command=start_bfs)
start_button.pack()

result_label = tk.Label(window)
result_label.pack()



window.mainloop()