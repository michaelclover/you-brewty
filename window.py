import tkinter as tk
import tkinter.messagebox as tkmb
import customtkinter as ctk

import recipe

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class HopsWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.title("You Brewty! - Hops")
        self.geometry("400x300")

class FermentablesWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.title("You Brewty! - Fermentables")
        self.geometry("400x300")

    def button_add_fermentable(self):
        label = ctk.CTkLabel(master=self.fermentables_frame_scroll, text=self.fermentables_entry.get(), text_color="white")
        label.grid(row=self.rowno, column=0, sticky="nsew")
        self.rowno = self.rowno + 1

class WaterConfigurationWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.title("You Brewty! - Water Configuration")
        self.geometry("400x300")

class YeastWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.title("You Brewty! - Yeast")
        self.geometry("400x300")

class NotesWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.title("You Brewty! - Notes")
        self.geometry("400x300")

class Window(ctk.CTk):

    def __init__(self, recipe):

        super().__init__()

        self.recipe = recipe

        self.title("You Brewty!")

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure((0), weight=1)

        ### CONFIGURATION WIDGETS ###

        self.configuration_frame = ctk.CTkFrame(self)
        self.configuration_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.configuration_frame.rowconfigure((0), weight=1)
        self.configuration_frame.columnconfigure((0), weight=1)

        self.configuration_header = ctk.CTkLabel(self.configuration_frame, text="Configuration")
        self.configuration_header.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.configuration_recipe_frame = ctk.CTkFrame(self.configuration_frame)
        self.configuration_recipe_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.configuration_recipe_label = ctk.CTkLabel(self.configuration_recipe_frame, text="Recipe name:")
        self.configuration_recipe_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.configuration_recipe_entry = ctk.CTkEntry(self.configuration_recipe_frame)
        self.configuration_recipe_entry.pack(side=tk.LEFT, padx=10, pady=10)

        self.configuration_new_button = ctk.CTkButton(self.configuration_recipe_frame, text="New", command=self.button_new)
        self.configuration_new_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.configuration_load_button = ctk.CTkButton(self.configuration_recipe_frame, text="Load", command=self.button_file_load)
        self.configuration_load_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.configuration_save_button = ctk.CTkButton(self.configuration_recipe_frame, text="Save", command=self.button_file_save)
        self.configuration_save_button.pack(side=tk.LEFT, padx=10, pady=10)

        ### RECIPE WIDGETS ###

        self.recipe_frame = ctk.CTkFrame(self)
        self.recipe_frame.grid(row=1, column=0, padx=10, pady=(10, 10), sticky="nsew")
        self.recipe_frame.rowconfigure((0), weight=1)
        self.recipe_frame.columnconfigure((0), weight=1)

        self.recipe_header = ctk.CTkLabel(self.recipe_frame, text="Recipe")
        self.recipe_header.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.recipe_inner_frame = ctk.CTkFrame(self.recipe_frame)
        self.recipe_inner_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.recipe_water_configuration_button = ctk.CTkButton(self.recipe_inner_frame, text="Water Configuration", command=self.button_water_configuration)
        self.recipe_water_configuration_button.pack(anchor=tk.CENTER, side=tk.LEFT, padx=10, pady=10)

        self.recipe_fermentables_button = ctk.CTkButton(self.recipe_inner_frame, text="Fermentables", command=self.button_fermentables)
        self.recipe_fermentables_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.recipe_hops_button = ctk.CTkButton(self.recipe_inner_frame, text="Hops", command=self.button_hops)
        self.recipe_hops_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.recipe_yeast_button = ctk.CTkButton(self.recipe_inner_frame, text="Yeast", command=self.button_yeast)
        self.recipe_yeast_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.recipe_notes_button = ctk.CTkButton(self.recipe_inner_frame, text="Notes", command=self.button_notes)
        self.recipe_notes_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="nsew")
        self.output_frame.rowconfigure((0), weight=1)
        self.output_frame.columnconfigure((0), weight=1)

        self.output_header = ctk.CTkLabel(self.output_frame, text="Output")
        self.output_header.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.output_inner_frame = ctk.CTkFrame(self.output_frame)
        self.output_inner_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.output_batch_volume = ctk.CTkLabel(self.output_inner_frame, text="Final volume: ")
        self.output_batch_volume.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.output_batch_volume_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.output_batch_volume_value.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.output_abv = ctk.CTkLabel(self.output_inner_frame, text="ABV: ")
        self.output_abv.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.output_abv_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.output_abv_value.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        ### POP-UP WINDOWS ###

        self.hops_window = None
        self.water_configuration_window = None
        self.fermentables_window = None
        self.yeast_window = None
        self.notes_window = None

        self.button_new()

    ### RECIPE BUTTON HANDLERS ### 

    def button_yeast(self):
        if self.yeast_window is None or not self.yeast_window.winfo_exists():
            self.yeast_window = YeastWindow(self)
        else:
            self.yeast_window.deiconify()
            self.yeast_window.focus()
            self.yeast_window.attributes("-topmost", True)

    def button_hops(self):
        if self.hops_window is None or not self.hops_window.winfo_exists():
            self.hops_window = HopsWindow(self)
        else:
            self.hops_window.deiconify()
            self.hops_window.focus()
            self.hops_window.attributes("-topmost", True)

    def button_water_configuration(self):
        if self.water_configuration_window is None or not self.water_configuration_window.winfo_exists():
            self.water_configuration_window = WaterConfigurationWindow(self)
        else:
            self.water_configuration_window.deiconify()
            self.water_configuration_window.focus()
            self.water_configuration_window.attributes("-topmost", True)   

    def button_fermentables(self):
        if self.fermentables_window is None or not self.fermentables_window.winfo_exists():
            self.fermentables_window = FermentablesWindow(self)
        else:
            self.fermentables_window.deiconify()
            self.fermentables_window.focus()
            self.fermentables_window.attributes("-topmost", True)     

    def button_notes(self):
        if self.notes_window is None or not self.notes_window.winfo_exists():
            self.notes_window = NotesWindow(self)
        else:
            self.notes_window.deiconify()
            self.notes_window.focus()
            self.notes_window.attributes("-topmost", True)    

    ### CONFIGURATION BUTTON HANDLERS ###

    def button_new(self):
        self.recipe = recipe.Recipe()
        self.update_ui()

    def button_file_save(self):
        recipe_name = self.configuration_recipe_entry.get()
        if recipe_name is None or recipe_name == "":
            tkmb.showerror("Error", "Please enter a recipe name")
            return
        self.recipe.name = recipe_name
        returned = tk.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not returned:
            return
        self.recipe.save_file(returned)

    def button_file_load(self):
        returned = tk.filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not returned: 
            return
        self.recipe.load_file(returned)
        self.update_ui()

    ### UI UPDATE FUNCTIONS AND UI HANDLERS ###

    def update_ui(self):
        self.configuration_recipe_entry.delete(0, tk.END)
        self.configuration_recipe_entry.insert(0, self.recipe.name)

        self.output_batch_volume_value.configure(text=f"{self.recipe.post_boil_volume():.2f} US gals")
        self.output_abv_value.configure(text=f"{self.recipe.estimate_abv():.2f}%")
