import subprocess
import tkinter as tk
from tkinter import ttk


class MainPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Configure main frame
        self.configure(bg="#f0f0f0")

        # Create a label
        self.label = tk.Label(self, text="Pick an algorithm to continue", font=("Arial", 20), bg="#f0f0f0", fg="#333333")
        self.label.pack(pady=30)

        # Create a frame for the radiobuttons
        self.radio_frame = tk.Frame(self, bg="#f0f0f0")
        self.radio_frame.pack(pady=20)

        # Create radiobuttons for each page
        algorithms = [
            ("BFS", "./BFS_tkinter.py"),
            ("DFS", "DFS_tkinter.py"),
            ("WARSHALL", "WARSHALL_tkinter.py"),
            ("PRIM", "PRIM_tkinter.py"),
            ("KRUSKAL", "KRUSKUL_tkinter.py"),
            ("KUSURAJU", "KUSARAJU_tkinter.py"),
            ("DIJKSTRA", "DIJKSTRA_tkinter.py"),
            ("BELLMAN-FORD", "BELLMAN_FORD_tkinter.py")
        ]

        for algorithm in algorithms:
            algo_name, filename = algorithm
            radio_button = ttk.Radiobutton(self.radio_frame, text=algo_name, value=algo_name,
                                           command=lambda f=filename: self.open_page(f))
            radio_button.pack(side="left", padx=10)

    def open_page(self, filename):
        # Run the file in a subprocess
        subprocess.run(["python3", filename])
         

root = tk.Tk()
root.title("Graph Algorithms")
root.configure(bg="#f0f0f0")
app = MainPage(master=root)
app.mainloop()