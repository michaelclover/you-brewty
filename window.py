import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class Window(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("You Brewty!")

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        configuration_frame = ctk.CTkScrollableFrame(self, fg_color=self.cget("bg"))
        configuration_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        configuration_label = ctk.CTkLabel(master=configuration_frame, text="Configuration")
        configuration_label.grid(row=0, column=0, pady=(0, 20))

        fermentables_frame = ctk.CTkScrollableFrame(self, fg_color=self.cget("bg"))
        fermentables_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        fermentables_label = ctk.CTkLabel(master=fermentables_frame, text="Fermentables")
        fermentables_label.grid(row=0, column=0, pady=(0, 20))

        fermentables_entry = ctk.CTkEntry(fermentables_frame, placeholder_text="fermentable")
        fermentables_entry.grid(row=1, column=0)

        fermentables_button = ctk.CTkButton(fermentables_frame, text="add")
        fermentables_button.grid(row=1, column=1, padx=10)

        hops_frame = ctk.CTkScrollableFrame(self, fg_color=self.cget("bg"))
        hops_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        hops_label = ctk.CTkLabel(master=hops_frame, text="Hops")
        hops_label.grid(row=0, column=0, pady=(0, 20))

        yeast_frame = ctk.CTkScrollableFrame(self, fg_color=self.cget("bg"))
        yeast_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        yeast_label = ctk.CTkLabel(master=yeast_frame, text="Yeast")
        yeast_label.grid(row=0, column=0, pady=(0, 20))     

    def button_function(self):
        pass