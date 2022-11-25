import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class VirusPage(tk.Frame):
    title_label: tk.Label
    confirm_btn: tk.Button
    virus_list: tk.Listbox

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BACKGROUND_COLOR)

        self.title_label = tk.Label(self, text="VIRUS FOUND", font=SUBTITLE_FONT,
                                    fg=FAILURE_COLOR, bg=BACKGROUND_COLOR)
        self.title_label.place(x=190, y=50, width=415, height=60)

        self.virus_list = tk.Listbox(self, font=NORMAL_TEXT_FONT,
                                     fg=BACKGROUND_COLOR, bg=WHITE_COLOR)
        self.virus_list.place(x=100, y=160, width=600, height=150)

        self.confirm_btn = tk.Button(self, text="CONFIRM", font=NORMAL_TEXT_FONT,
                                     fg=BACKGROUND_COLOR, bg=FAILURE_COLOR)
        self.confirm_btn.config(command=lambda: controller.show_frame(controller.pages[0]))
        self.confirm_btn.place(x=315, y=375, width=170, height=50)
