import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.title = tk.Label(self, text="RASPIRUS",
                              font=title_font, fg=primary_color,
                              width=10, height=5)
        self.title.place(x=250, y=110)