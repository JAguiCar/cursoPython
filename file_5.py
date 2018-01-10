import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.label = tk.Label(self, text="Hello world", padx=200, pady=10)
        self.label. pack()


if __name__ == "__main__":
    root = Root()
    root.mainloop()
"""Esta es para que la ventana se mantenga abierta (interfaces gráficas)"""
