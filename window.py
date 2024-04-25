import tkinter as tk
import tkinter.messagebox as tkmb
import customtkinter as ctk

import recipe
from windows.hopswindow import *
from windows.fermentableswindow import *
from windows.configurationwindow import *
from windows.yeastwindow import *
from windows.noteswindow import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

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

        self.recipe_configuration_button = ctk.CTkButton(self.recipe_inner_frame, text="Configuration", command=self.button_configuration)
        self.recipe_configuration_button.pack(anchor=tk.CENTER, side=tk.LEFT, padx=10, pady=10)

        self.recipe_fermentables_button = ctk.CTkButton(self.recipe_inner_frame, text="Fermentables", command=self.button_fermentables)
        self.recipe_fermentables_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.recipe_hops_button = ctk.CTkButton(self.recipe_inner_frame, text="Hops", command=self.button_hops)
        self.recipe_hops_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.recipe_yeast_button = ctk.CTkButton(self.recipe_inner_frame, text="Yeast", command=self.button_yeast)
        self.recipe_yeast_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.recipe_notes_button = ctk.CTkButton(self.recipe_inner_frame, text="Notes", command=self.button_notes)
        self.recipe_notes_button.pack(side=tk.LEFT, padx=10, pady=10)

        ### IMPORTANT RECIPE INFORMATION ###

        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.grid(row=2, column=0, padx=10, pady=(10, 10), sticky="nsew")
        self.output_frame.rowconfigure((0), weight=1)
        self.output_frame.columnconfigure((0), weight=1)

        self.output_header = ctk.CTkLabel(self.output_frame, text="Output")
        self.output_header.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.output_inner_frame = ctk.CTkFrame(self.output_frame)
        self.output_inner_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.output_inner_frame.columnconfigure((0,1,2,3,4,5,6,7), weight=1)

        self.initial_volume = ctk.CTkLabel(self.output_inner_frame, text="Initial volume:")
        self.initial_volume.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.initial_volume_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.initial_volume_value.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.mash_volume = ctk.CTkLabel(self.output_inner_frame, text="Mash volume:")
        self.mash_volume.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.mash_volume_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.mash_volume_value.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.sparge_volume = ctk.CTkLabel(self.output_inner_frame, text="Sparge volume:")
        self.sparge_volume.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.sparge_volume_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.sparge_volume_value.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.pre_boil_volume = ctk.CTkLabel(self.output_inner_frame, text="Pre-boil volume:")
        self.pre_boil_volume.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.pre_boil_volume_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.pre_boil_volume_value.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

        self.output_batch_volume = ctk.CTkLabel(self.output_inner_frame, text="Final volume:")
        self.output_batch_volume.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.output_batch_volume_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.output_batch_volume_value.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

        self.post_mash_gravity = ctk.CTkLabel(self.output_inner_frame, text="Post-mash gravity:")
        self.post_mash_gravity.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        self.post_mash_gravity_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.post_mash_gravity_value.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

        self.post_boil_gravity = ctk.CTkLabel(self.output_inner_frame, text="Post-boil gravity:")
        self.post_boil_gravity.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
        self.post_boil_gravity_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.post_boil_gravity_value.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

        self.final_gravity = ctk.CTkLabel(self.output_inner_frame, text="Final gravity:")
        self.final_gravity.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
        self.final_gravity_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.final_gravity_value.grid(row=2, column=4, padx=10, pady=10, sticky="nsew")

        self.output_abv = ctk.CTkLabel(self.output_inner_frame, text="ABV:")
        self.output_abv.grid(row=4, column=6, padx=10, pady=10, sticky="nsew")
        self.output_abv_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.output_abv_value.grid(row=4, column=7, padx=10, pady=10, sticky="nsew")

        self.ibu = ctk.CTkLabel(self.output_inner_frame, text="IBU:")
        self.ibu.grid(row=0, column=6, padx=10, pady=10, sticky="nsew")
        self.ibu_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.ibu_value.grid(row=0, column=7, padx=10, pady=10, sticky="nsew")

        self.mcu = ctk.CTkLabel(self.output_inner_frame, text="MCU:")
        self.mcu.grid(row=1, column=6, padx=10, pady=10, sticky="nsew")
        self.mcu_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.mcu_value.grid(row=1, column=7, padx=10, pady=10, sticky="nsew")

        self.srm_table = {1: "#FFE699",
                          2: "#FFD878",
                          3: "#FFCA5A",
                          4: "#FFBF42",
                          5: "#FBB123",
                          6: "#F8A600",
                          7: "#F39C00",
                          8: "#EA8F00",
                          9: "#E58500",
                          10: "#DE7C00",
                          11: "#D77200",
                          12: "#CF6900",
                          13: "#CB6200",
                          14: "#C35900",
                          15: "#BB5100",
                          16: "#B54C00",
                          17: "#B04500",
                          18: "#A63E00",
                          19: "#A13700",
                          20: "#9B3200",
                          21: "#952D00",
                          22: "#8E2900",
                          23: "#882300",
                          24: "#821E00",
                          25: "#7B1A00",
                          26: "#771900",
                          27: "#701400",
                          28: "#6A0E00",
                          29: "#660D00",
                          30: "#5E0B00",
                          31: "#5A0A02",
                          32: "#600903",
                          33: "#520907",
                          34: "#4C0505",
                          35: "#470606",
                          36: "#420607",
                          37: "#3D0708",
                          38: "#370607",
                          39: "#2D0607",
                          40: "#1F0506"}

        self.srm = ctk.CTkLabel(self.output_inner_frame, text="SRM:")
        self.srm.grid(row=2, column=6, padx=10, pady=10, sticky="nsew")
        self.srm_value = ctk.CTkLabel(self.output_inner_frame, text="")
        self.srm_value.grid(row=2, column=7, padx=10, pady=10, sticky="nsew")

        ### POP-UP WINDOWS ###

        self.hops_window = None
        self.configuration_window = None
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

    def button_configuration(self):
        if self.configuration_window is None or not self.configuration_window.winfo_exists():
            self.configuration_window = ConfigurationWindow(self)
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
        # Get the recipe name.
        recipe_name = self.configuration_recipe_entry.get()
        if recipe_name is None or recipe_name == "":
            tkmb.showerror("Error", "Please enter a recipe name")
            return
        self.recipe.name = recipe_name

        # Spawn and present the save as dialog.
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

        self.initial_volume_value.configure(text=f"{self.recipe.initial_volume:.2f} {'Ltrs' if self.recipe.metric else 'US gals'}")
        self.mash_volume_value.configure(text=f"{self.recipe.mash_volume():.2f} {'Ltrs' if self.recipe.metric else 'US gals'}")
        self.sparge_volume_value.configure(text=f"{self.recipe.sparge_volume():.2f} {'Ltrs' if self.recipe.metric else 'US gals'}")
        self.pre_boil_volume_value.configure(text=f"{self.recipe.pre_boil_volume():.2f} {'Ltrs' if self.recipe.metric else 'US gals'}")
        self.output_batch_volume_value.configure(text=f"{self.recipe.post_boil_volume():.2f} {'Ltrs' if self.recipe.metric else 'US gals'}")

        self.post_mash_gravity_value.configure(text=f"{self.recipe.pre_boil_og():.3f}")
        self.post_boil_gravity_value.configure(text=f"{self.recipe.post_boil_og():.3f}")
        self.final_gravity_value.configure(text=f"{self.recipe.final_gravity():.3f}")
        self.output_abv_value.configure(text=f"{self.recipe.estimate_abv():.2f}%")

        self.ibu_value.configure(text=f"{self.recipe.tinseth_ibu():.2f}")
        self.mcu_value.configure(text=f"{self.recipe.malt_colour_units():.2f}")
        self.srm_value.configure(text=f"{self.recipe.morey_srm():.2f}")
        if round(self.recipe.morey_srm()) in self.srm_table:
            self.srm_value.configure(bg_color=self.srm_table[round(self.recipe.morey_srm())])
        else:
            self.srm_value.configure(bg_color="transparent")
