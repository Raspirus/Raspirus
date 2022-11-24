import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class VirusPage(tk.Frame):
    title_label: tk.Label
    confirm_btn: tk.Button
    virus_list: tk.Listbox

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=background_color)

        self.title_label = tk.Label(self, text="VIRUS FOUND", font=subtitle_font,
                                    fg=failure_color, bg=background_color)
        self.title_label.place(x=190, y=50, width=415, height=60)

        self.virus_list = tk.Listbox(self, font=normal_text,
                                     fg=background_color, bg=white)
        self.virus_list.place(x=100, y=160, width=600, height=150)

        self.confirm_btn = tk.Button(self, text="CONFIRM", font=normal_text,
                                     fg=background_color, bg=failure_color)
        self.confirm_btn.config(command=lambda: controller.show_frame(controller.pages[0]))
        self.confirm_btn.place(x=315, y=375, width=170, height=50)
