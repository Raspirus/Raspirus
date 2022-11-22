from tkinter import *
from TKinterModernThemes import ThemedTKinterFrame  # For the themes
from Raspirus.frontend.utility import *  # For colors and fonts


class MainPage(ThemedTKinterFrame):
    settings_btn = Button()
    tile_label = Label()
    drive_selector = Listbox()
    start_btn = Button()
    info_btn = Button()

    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__(str("TITLE"), theme, mode, usecommandlineargs, usethemeconfigfile)

        self.root.geometry("800x480")
        self.title = Label(self.root, text="RASPIRUS",
                           font=title_font, fg=primary_color,
                           width=10, height=5)
        self.title.place(x=250, y=110)
