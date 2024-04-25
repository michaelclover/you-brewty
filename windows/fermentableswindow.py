import customtkinter as ctk

class FermentablesWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.main_window = main_window
        self.recipe = main_window.recipe

        self.rowno = 1 # 1 instead of 0, to account for the header.

        self.title("You Brewty! - Fermentables")
        self.geometry("400x300")

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.fermentables_name = ctk.CTkEntry(self, placeholder_text="Name")
        self.fermentables_name.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.fermentables_weight = ctk.CTkEntry(self, placeholder_text="Weight")
        self.fermentables_weight.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.fermentables_potential = ctk.CTkEntry(self, placeholder_text="Potential")
        self.fermentables_potential.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.fermentables_lovibond = ctk.CTkEntry(self, placeholder_text="Lovibond")
        self.fermentables_lovibond.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        self.fermentables_add = ctk.CTkButton(self, text="Add", command=self.button_add_fermentable)
        self.fermentables_add.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

        self.fermentables_frame = ctk.CTkScrollableFrame(self)
        self.fermentables_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.fermentables_frame.grid(row=1, column=0, columnspan=5, rowspan=3, sticky="nsew")

        self.name_header = ctk.CTkLabel(master=self.fermentables_frame, text="Name", text_color="white")
        self.name_header.grid(row=0, column=0, sticky="nsew")

        self.weight_header = ctk.CTkLabel(master=self.fermentables_frame, text=f"Weight ({'kgs' if self.recipe.metric else 'lbs'})", text_color="white")
        self.weight_header.grid(row=0, column=1, sticky="nsew")

        self.potential_header = ctk.CTkLabel(master=self.fermentables_frame, text="Potential", text_color="white")
        self.potential_header.grid(row=0, column=2, sticky="nsew")

        self.lovibond_header = ctk.CTkLabel(master=self.fermentables_frame, text="Lovibond", text_color="white")
        self.lovibond_header.grid(row=0, column=3, sticky="nsew")

        for fermentable in self.recipe.fermentables:
            self.button_add_fermentable(fermentable)

        self.protocol("WM_DELETE_WINDOW", self.closed)

    def button_delete_fermentable(self, name, weight, potential, lovibond, button):

        n = name.get()
        self.recipe.fermentables[:] = [d for d in self.recipe.fermentables if not d.get("name") == n]

        name.destroy()
        weight.destroy()
        potential.destroy()
        lovibond.destroy()
        button.destroy()

    def button_add_fermentable(self, fermentable=None):

        name_label = ctk.CTkEntry(master=self.fermentables_frame, text_color="white")
        name_label.insert(0, fermentable["name"] if fermentable else self.fermentables_name.get())
        name_label.grid(row=self.rowno, column=0, pady=10, sticky="nsew")

        weight_label = ctk.CTkEntry(master=self.fermentables_frame, text_color="white")
        weight_label.insert(0, fermentable["weight"] if fermentable else self.fermentables_weight.get())
        weight_label.grid(row=self.rowno, column=1, pady=10, sticky="nsew")

        potential_label = ctk.CTkEntry(master=self.fermentables_frame, text_color="white")
        potential_label.insert(0, fermentable["potential"] if fermentable else self.fermentables_potential.get())
        potential_label.grid(row=self.rowno, column=2, pady=10, sticky="nsew")

        lovibond_label = ctk.CTkEntry(master=self.fermentables_frame, text_color="white")
        lovibond_label.insert(0, fermentable["lovibond"] if fermentable else self.fermentables_lovibond.get())
        lovibond_label.grid(row=self.rowno, column=3, pady=10, sticky="nsew")

        button = ctk.CTkButton(master=self.fermentables_frame, text="Delete")
        button.grid(row=self.rowno, column=4, pady=10, sticky="nsew")
        button.configure(command=lambda: self.button_delete_fermentable(name_label, weight_label, potential_label, lovibond_label, button))

        self.rowno = self.rowno + 1

    def closed(self):

        n = 0
        name = weight = potential = lovibond = ""
        for widget in self.fermentables_frame.winfo_children()[4:]:
            if n == 0:
                name = widget.get()
            elif n == 1:
                weight = float(widget.get())
            elif n == 2:
                potential = int(widget.get())
            elif n == 3:
                lovibond = float(widget.get())
            elif n == 4 and type(widget) is ctk.CTkButton:
                e = {"name": name,
                     "weight": weight,
                     "potential": potential,
                     "lovibond": lovibond}
                updated = False
                for idx, f in enumerate(self.recipe.fermentables):
                    if f["name"] == name:
                        self.recipe.fermentables[idx] = e
                        updated = True
                
                if not updated:
                    self.recipe.fermentables.append(e)

                n = -1

            n = n + 1
            
        self.main_window.update_ui()

        self.destroy()