import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class SettingsPage(tk.Frame):
    home_btn: tk.Button
    title_label: tk.Label
    hash_label: tk.Label
    log_label: tk.Label
    ssh_label: tk.Label
    ftp_label: tk.Label
    hash_btn: tk.Button
    log_btn: tk.Button
    ssh_btn: tk.Button
    ftp_btn: tk.Button

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=background_color)

        # Button to return to the main page
        self.home_btn = tk.Button(self, text="HOME", font=small_btn_font,
                                  fg=background_color, bg=grey)
        self.home_btn.config(command=lambda: controller.show_frame(controller.pages[0]))
        self.home_btn.place(x=20, y=30, width=110, height=30)

        # title of the page
        self.title_label = tk.Label(self, text="SETTINGS", font=subtitle_font,
                                    fg=secondary_color, bg=background_color)
        self.title_label.place(x=235, y=60, width=325, height=60)

        # All Labels
        self.hash_label = tk.Label(self, text="Update Hash signatures", font=normal_text,
                                   fg=white, bg=background_color, anchor='w')
        self.hash_label.place(x=30, y=170, width=460, height=25)

        self.log_label = tk.Label(self, text="Open LOG window", font=normal_text,
                                  fg=white, bg=background_color, anchor='w')
        self.log_label.place(x=30, y=240, width=460, height=25)

        self.ssh_label = tk.Label(self, text="Activate SSH", font=normal_text,
                                  fg=white, bg=background_color, anchor='w')
        self.ssh_label.place(x=30, y=310, width=460, height=25)

        self.ftp_label = tk.Label(self, text="Activate FTP", font=normal_text,
                                  fg=white, bg=background_color, anchor='w')
        self.ftp_label.place(x=30, y=380, width=460, height=25)

        # All Buttons
        self.hash_btn = tk.Button(self, text="Last updated 23.11.2022", font=normal_text,
                                  fg=background_color, bg=secondary_color)
        self.hash_btn.place(x=530, y=170, width=240, height=40)

        self.log_btn = tk.Button(self, text="Generated on 22.11.2022", font=normal_text,
                                 fg=background_color, bg=secondary_color)
        self.log_btn.place(x=530, y=240, width=240, height=40)

        self.ssh_btn = tk.Button(self, text="Status: active", font=normal_text,
                                 fg=background_color, bg=success_color)
        self.ssh_btn.place(x=530, y=310, width=240, height=40)

        self.ftp_btn = tk.Button(self, text="Status: deactivated", font=normal_text,
                                 fg=background_color, bg=failure_color)
        self.ftp_btn.place(x=530, y=380, width=240, height=40)

