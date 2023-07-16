import tkinter

class Window:

    root = tkinter.Tk()

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        Window.root.geometry(f"{self.window_width}x{self.window_height}")

    def centre(self):
        screen_width = Window.root.winfo_screenwidth()
        screen_height = Window.root.winfo_screenheight()

        centre_x = int(screen_width / 2 - self.window_width / 2)
        centre_y = int(screen_height / 2 - self.window_height / 2)

        self.root.geometry(f"{self.window_width}x{self.window_height}+{centre_x}+{centre_y}")

    def mainloop(self):
        Window.root.mainloop()