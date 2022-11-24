import tkinter as tk
from tkinter import ttk
from Raspirus.frontend.utility import *  # For colors and fonts


class LoadingPage(tk.Frame):
    progress_bar: ttk.Progressbar
    title_label: tk.Label
    scanned_label: tk.Label
    vfound_label: tk.Label
    quit_btn: tk.Button

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=background_color)

        self.title_label = tk.Label(self, text="Scanning... Please wait", font=subtitle_font,
                                    fg=secondary_color, bg=background_color)
        self.title_label.place(x=55, y=115, width=670, height=125)

        pstyle = ttk.Style()  # ProgressBar doesn't support coloring, so we need to create an external style and
        # apply it
        # ISSUE: Color defined here is not being used, only if you add pstyle.theme('clam')
        # Theme list: https://wiki.tcl-lang.org/page/List+of+ttk+Themes
        pstyle.configure("primary.Horizontal.TProgressbar", foreground=background_color, background=primary_color)
        self.progress_bar = ttk.Progressbar(self, orient='horizontal', mode='determinate',
                                            style="primary.Horizontal.TProgressbar",
                                            maximum=100, value=65)
        self.progress_bar.place(x=50, y=225, width=700, height=45)

        self.scanned_label = tk.Label(self, text="Scanned 12.345 files of 24.478 total", font=normal_text,
                                      fg=white, bg=background_color, anchor='w')
        self.scanned_label.place(x=50, y=275, width=280, height=30)

        self.vfound_label = tk.Label(self, text="Virus found: 0", font=normal_text,
                                     fg=white, bg=background_color, anchor='w')
        self.vfound_label.place(x=50, y=315, width=280, height=30)

        # TODO: Make this round
        self.quit_btn = tk.Button(self, fg=background_color, bg=failure_color)
        self.quit_btn.config(command=lambda: controller.show_frame(controller.pages[0]))
        self.quit_btn.place(x=375, y=375, width=50, height=50)
