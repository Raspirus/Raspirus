import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class SettingsLogPage(tk.Frame):
    home_btn: tk.Button
    logs_textbox: tk.Text

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BACKGROUND_COLOR)

        # Button to return to the main page
        self.home_btn = tk.Button(self, text="BACK", font=SMALL_BUTTON_TEXT_FONT,
                                  fg=BACKGROUND_COLOR, bg=GREY_COLOR)
        self.home_btn.config(command=lambda: controller.show_frame(controller.pages[1]))
        self.home_btn.place(x=20, y=30, width=110, height=30)

        self.logs_textbox = tk.Text(self)
        self.logs_textbox.place(x=25, y=80, width=750, height=370)

