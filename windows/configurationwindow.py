import customtkinter as ctk
import tkinter as tk
from CTkToolTip import *

class ConfigurationWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.main_window = main_window
        self.recipe = main_window.recipe

        self.title("You Brewty! - Configuration")
        self.geometry("400x300")

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.efficiency_label = ctk.CTkLabel(self, text="Efficiency:", text_color="white")
        self.efficiency_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.efficiency = ctk.CTkEntry(self, placeholder_text="Efficiency")
        self.efficiency.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.efficiency.insert(0, self.recipe.efficiency)

        self.initial_volume_label = ctk.CTkLabel(self, text=f"Initial Volume ({'Litres' if self.recipe.metric else 'US gals'}):", text_color="white")
        self.initial_volume_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        tooltip = CTkToolTip(self.initial_volume, message="This is the initial volume of water or liquor you'll need, input as a whole number or a decimal.")

        self.initial_volume = ctk.CTkEntry(self, placeholder_text="Initial Volume")
        self.initial_volume.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.initial_volume.insert(0, self.recipe.initial_volume) 

        self.boil_time_label = ctk.CTkLabel(self, text="Boil Time (hours):", text_color="white")
        self.boil_time_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        tooltip = CTkToolTip(self.boil_time_label, message="This is how long you should boil your wort for, input as a whole number or a decimal.\nOne hour should be input as 1 or 1.0, whereas One hour and thirty minutes should be input as 1.5, for example.")

        self.boil_time = ctk.CTkEntry(self, placeholder_text="Boil Time")
        self.boil_time.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.boil_time.insert(0, self.recipe.boil_time)

        self.water_grist_ratio_label = ctk.CTkLabel(self, text="Grist ratio (ltrs/kg):", text_color="white")
        self.water_grist_ratio_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        tooltip = CTkToolTip(self.water_grist_ratio, message="This is your water-to-grist ratio, i.e. how much water you wish to include in the mash per kg of malt.\nThe most practical range for this is between 2-4 litres per kg, though 2.5-3.2 is most commonly used.")

        self.water_grist_ratio = ctk.CTkEntry(self, placeholder_text="Water Grist Ratio")
        self.water_grist_ratio.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.water_grist_ratio.insert(0, self.recipe.target_water_grist_ratio)

        self.units = tk.IntVar(value=0)
        if self.recipe.metric is True:
            self.units = tk.IntVar(value=1)
        else:
            self.units = tk.IntVar(value=2)
        self.metric = ctk.CTkRadioButton(self, text="Metric", variable=self.units, value=1, command=self.units_changed)
        self.metric.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.imperial = ctk.CTkRadioButton(self, text="Imperial", variable=self.units, value=2, command=self.units_changed)
        self.imperial.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

        self.protocol("WM_DELETE_WINDOW", self.closed)

    def units_changed(self):
        if self.recipe.metric is True and self.units.get() is 2: # from metric to imperial.
            self.recipe.convert_units()
        if self.recipe.metric is False and self.units.get() is 1: # from imperial to metric.
            self.recipe.convert_units()
        
        self.initial_volume_label.configure(text=f"Initial Volume ({'Litres' if self.recipe.metric else 'US gals'}):")      
        self.initial_volume.delete(0, 'end')
        self.initial_volume.insert(0, float(f"{self.recipe.initial_volume:.2f}"))
        self.main_window.update_ui()

    def closed(self):
        
        self.recipe.efficiency = float(self.efficiency.get())
        self.recipe.initial_volume = float(self.initial_volume.get())
        self.recipe.boil_time = int(self.boil_time.get())
        self.recipe.target_water_grist_ratio = float(self.water_grist_ratio.get())

        self.main_window.update_ui()

        self.destroy()