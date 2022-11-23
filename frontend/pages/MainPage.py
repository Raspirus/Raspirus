import tkinter as tk
import TKinterModernThemes as TKMT
from Raspirus.frontend.utility import *  # For colors and fonts


class MainPage(tk.Frame):
    title_label: tk.Label = None

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=background_color)

        self.title_label = tk.Label(self, text="RASPIRUS",
                                    font=title_font, fg=primary_color, bg=background_color)
        self.title_label.place(x=140, y=60, width=510, height=120)

        # highlightbackground / highlightcolor sets a border to the component
        self.drive_selector = tk.Listbox(self, highlightbackground=primary_color, highlightcolor=primary_color)
        self.drive_selector.place(x=90, y=215, width=620, height=48)

        self.start_btn = tk.Button(self, text="START", font=button_font, fg=background_color, bg=primary_color)
        self.start_btn.place(x=185, y=315, width=170, height=50)