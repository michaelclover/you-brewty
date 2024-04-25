import customtkinter as ctk

class NotesWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.main_window = main_window
        self.recipe = main_window.recipe

        self.title("You Brewty! - Notes")
        self.geometry("400x300")

        self.notes_textbox = ctk.CTkTextbox(master=self, width=400, height=300)
        self.notes_textbox.pack(padx=10, pady=10)

        self.notes_textbox.insert(0.0, main_window.recipe.notes)

        self.protocol("WM_DELETE_WINDOW", self.closed)

    def closed(self):

        self.recipe.notes = self.notes_textbox.get("0.0", "end")
        self.main_window.update_ui()
        self.destroy()