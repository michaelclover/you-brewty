import customtkinter as ctk

class YeastWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.main_window = main_window
        self.recipe = main_window.recipe

        self.title("You Brewty! - Yeast")
        self.geometry("400x300")

        self.yeast_attenuation_label = ctk.CTkLabel(self, text="Attenuation", text_color="white")
        self.yeast_attenuation_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.yeast_attenuation = ctk.CTkEntry(self, placeholder_text="Yeast Attenuation")
        self.yeast_attenuation.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.yeast_attenuation.insert(0, self.recipe.yeast_attenuation)

        self.protocol("WM_DELETE_WINDOW", self.closed)

    def closed(self):

        self.recipe.yeast_attenuation = float(self.yeast_attenuation.get())

        self.main_window.update_ui()

        self.destroy()