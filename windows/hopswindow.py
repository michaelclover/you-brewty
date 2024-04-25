import customtkinter as ctk
from CTkToolTip import *

class HopsWindow(ctk.CTkToplevel):

    def __init__(self, main_window):

        super().__init__()

        self.main_window = main_window
        self.recipe = main_window.recipe

        self.rowno = 1 # 1 instead of 0, to account for the header.

        self.title("You Brewty! - Hops")
        self.geometry("400x300")

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.hops_name = ctk.CTkEntry(self, placeholder_text="Name")
        self.hops_name.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.hops_ounces = ctk.CTkEntry(self, placeholder_text="Weight")
        self.hops_ounces.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.hops_aau = ctk.CTkEntry(self, placeholder_text="AAU")
        self.hops_aau.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        tooltip = CTkToolTip(self.hops_aau, message="This is the alpha acid unit rating of your hop. As a general rule, hops with a higher AAU tend to be better for, and used for, adding bitterness.\nHops with a low AAU tend to be ideal and used for flavouring. This is a general rule though, and not always the case.\nThis value should be supplied with your purchased hops, however you should be able to find it online easily.")

        self.hops_boil_time = ctk.CTkEntry(self, placeholder_text="Boil Time")
        self.hops_boil_time.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        tooltip = CTkToolTip(self.hops_boil_time, message="This is the time during the boil these hops should be introduced.\nFor example, if you have a boil duration of 1 hour and this value is 60, the hops should be introduced immediately.")

        self.hops_add = ctk.CTkButton(self, text="Add", command=self.button_add_hop)
        self.hops_add.grid(row=0, column=4, padx=10, pady=10, sticky="nsew")

        self.hops_frame = ctk.CTkScrollableFrame(self)
        self.hops_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.hops_frame.grid(row=1, column=0, columnspan=5, rowspan=3, sticky="nsew")

        self.name_header = ctk.CTkLabel(master=self.hops_frame, text="Name", text_color="white")
        self.name_header.grid(row=0, column=0, sticky="nsew")

        self.ounces_header = ctk.CTkLabel(master=self.hops_frame, text=f"Weight ({'gs' if self.recipe.metric else 'oz'})", text_color="white")
        self.ounces_header.grid(row=0, column=1, sticky="nsew")

        self.aau_header = ctk.CTkLabel(master=self.hops_frame, text="AAU", text_color="white")
        self.aau_header.grid(row=0, column=2, sticky="nsew")

        self.boil_time_header = ctk.CTkLabel(master=self.hops_frame, text="Boil Time", text_color="white")
        self.boil_time_header.grid(row=0, column=3, sticky="nsew")

        for hop in self.recipe.hops:
            self.button_add_hop(hop)

        self.protocol("WM_DELETE_WINDOW", self.closed)

    def button_delete_hop(self, name, ounces, aau, boil_time, button):

        n = name.get()
        self.recipe.hops[:] = [d for d in self.recipe.hops if not d.get("name") == n]

        name.destroy()
        ounces.destroy()
        aau.destroy()
        boil_time.destroy()
        button.destroy()

    def button_add_hop(self, hop=None):

        name_label = ctk.CTkEntry(master=self.hops_frame, text_color="white")
        name_label.insert(0, hop["name"] if hop else self.hops_name.get())
        name_label.grid(row=self.rowno, column=0, pady=10, sticky="nsew")

        ounces_label = ctk.CTkEntry(master=self.hops_frame, text_color="white")
        ounces_label.insert(0, hop["weight"] if hop else self.hops_ounces.get())
        ounces_label.grid(row=self.rowno, column=1, pady=10, sticky="nsew")

        aau_label = ctk.CTkEntry(master=self.hops_frame, text_color="white")
        aau_label.insert(0, hop["aau"] if hop else self.hops_aau.get())
        aau_label.grid(row=self.rowno, column=2, pady=10, sticky="nsew")

        boil_time_label = ctk.CTkEntry(master=self.hops_frame, text_color="white")
        boil_time_label.insert(0, hop["boil_time"] if hop else self.hops_boil_time.get())
        boil_time_label.grid(row=self.rowno, column=3, pady=10, sticky="nsew")

        button = ctk.CTkButton(master=self.hops_frame, text="Delete")
        button.grid(row=self.rowno, column=4, pady=10, sticky="nsew")
        button.configure(command=lambda: self.button_delete_hop(name_label, ounces_label, aau_label, boil_time_label, button))

        self.rowno = self.rowno + 1

    def closed(self):

        n = 0
        name = ounces = aau = boil_time = ""
        for widget in self.hops_frame.winfo_children()[4:]:
            if n == 0:
                name = widget.get()
            elif n == 1:
                ounces = float(widget.get())
            elif n == 2:
                aau = float(widget.get())
            elif n == 3:
                boil_time = int(widget.get())
            elif n == 4 and type(widget) is ctk.CTkButton:
                e = {"name": name,
                     "weight": ounces,
                     "aau": aau,
                     "boil_time": boil_time}
                updated = False
                for idx, h in enumerate(self.recipe.hops):
                    if h["name"] == name and h["boil_time"] == boil_time:
                        self.recipe.hops[idx] = e
                        updated = True

                if not updated:
                    self.recipe.hops.append(e)

                n = -1

            n = n + 1

        self.main_window.update_ui()
            
        self.destroy()