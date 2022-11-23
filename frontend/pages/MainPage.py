import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class MainPage(tk.Frame):
    title_label: tk.Label
    drive_selector: tk.Listbox
    start_btn: tk.Button
    info_btn: tk.Button
    settings_btn: tk.Button

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=background_color)

        self.title_label = tk.Label(self, text="RASPIRUS",
                                    font=title_font, fg=primary_color, bg=background_color)
        self.title_label.place(x=140, y=60, width=510, height=120)

        # highlightbackground / highlightcolor sets a border to the component
        self.drive_selector = tk.Listbox(self, highlightbackground=primary_color, highlightcolor=primary_color,
                                         highlightthickness=2, bg=white)
        self.drive_selector.place(x=90, y=215, width=620, height=48)

        self.start_btn = tk.Button(self, text="START", font=button_font, fg=background_color, bg=primary_color)
        self.start_btn.place(x=185, y=315, width=170, height=50)

        self.info_btn = tk.Button(self, text="INFO", font=button_font, fg=background_color, bg=white)
        self.info_btn.place(x=420, y=315, width=170, height=50)

        self.settings_btn = tk.Button(self, text="SETTINGS", font=settings_font, fg=secondary_color,
                                      bg=white)
        self.settings_btn.config(command=lambda: controller.show_frame(controller.pages[1]))
        self.settings_btn.place(x=670, y=15, width=110, height=40)
