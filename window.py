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

        Window.root.geometry(f"{self.window_width}x{self.window_height}+{centre_x}+{centre_y}")

    def icon(self, path):
        Window.root.iconbitmap(path)

    def title(self, title):
        Window.root.title(title)

    def mainloop(self):
        Window.root.mainloop()