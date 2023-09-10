import customtkinter as ctk
import tkinter.filedialog as tkfd

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def file_save(recipe):
    returned = tkfd.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if not returned:
        return
    recipe.save_file(returned)

class HopsWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.geometry("400x300")

        self.button_ok = ctk.CTkButton(self, text="close", command=self.close_window)
        self.button_ok.pack(padx=20, pady=20)

    def close_window(self):  
        self.withdraw()

class Window(ctk.CTk):

    def __init__(self, recipe):

        super().__init__()

        self.recipe = recipe

        self.title("You Brewty!")
        self.attributes('-zoomed', True)

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0), weight=1)
        
        self.configuration_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_color="white", border_width=1)
        self.configuration_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.configuration_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        configuration_label = ctk.CTkLabel(master=self.configuration_frame, text="Configuration")
        configuration_label.grid(row=0, column=3, sticky="nsew", pady=5)

        self.fermentables_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_color="white", border_width=1)
        self.fermentables_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.fermentables_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        fermentables_label = ctk.CTkLabel(master=self.fermentables_frame, text="Fermentables", anchor="w")
        fermentables_label.grid(row=0, column=2, sticky="nsew", pady=5)

        self.fermentables_entry = ctk.CTkEntry(self.fermentables_frame, placeholder_text="fermentable")
        self.fermentables_entry.grid(row=1, column=0, sticky="nsew", padx=10)

        self.fermentables_frame_scroll = ctk.CTkScrollableFrame(master=self.fermentables_frame, border_color="white", border_width=1)
        self.fermentables_frame_scroll.grid(row=2, column=0, sticky="nsew", padx=10, pady=(5, 0))
        self.fermentables_frame_scroll.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.rowno = 0

        fermentables_button = ctk.CTkButton(self.fermentables_frame, text="add", command=self.button_add_fermentable)
        fermentables_button.grid(row=1, column=1, sticky="nsew")

        self.hops_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_color="white", border_width=1)
        self.hops_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.hops_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        hops_label = ctk.CTkLabel(master=self.hops_frame, text="Hops")
        hops_label.grid(row=0, column=3, sticky="nsew", pady=5)

        self.hops_button = ctk.CTkButton(self.hops_frame, text="add", command=self.button_add_hop)
        self.hops_button.grid(row=1, column=0, sticky="nsew", padx=10)

        self.yeast_frame = ctk.CTkFrame(self, fg_color=self.cget("bg"), border_color="white", border_width=1)
        self.yeast_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.yeast_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        yeast_label = ctk.CTkLabel(master=self.yeast_frame, text="Yeast")
        yeast_label.grid(row=0, column=3, sticky="nsew", pady=5)    

        self.yeast_button = ctk.CTkButton(self.yeast_frame, text="save", command=self.button_file_save)
        self.yeast_button.grid(row=1, column=0, padx=10, sticky="nsew")

        self.hops_window = None 

    def button_add_fermentable(self):
        label = ctk.CTkLabel(master=self.fermentables_frame_scroll, text=self.fermentables_entry.get(), text_color="white")
        label.grid(row=self.rowno, column=0, sticky="nsew")
        self.rowno = self.rowno + 1

    def button_add_yeast(self):
        pass

    def button_add_hop(self):
        if self.hops_window is None or not self.hops_window.winfo_exists():
            self.hops_window = HopsWindow(self)
        else:
            self.hops_window.deiconify()
            self.hops_window.focus()
            self.hops_window.attributes("-topmost", True)

    def button_file_save(self):
        file_save(self.recipe)

