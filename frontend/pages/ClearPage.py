import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class ClearPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.title = tk.Label(self, text="RASPIRUS",
                              font=TITLE_FONT, fg=PRIMARY_COLOR,
                              width=10, height=5)
        self.title.place(x=250, y=110)