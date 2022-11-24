import tkinter as tk
from Raspirus.frontend.utility import *  # For colors and fonts


class InfoPage(tk.Frame):
    home_btn: tk.Button
    title_label: tk.Label
    # r-prefix: right aligned text
    # l-prefix: left aligned text
    lname_label: tk.Label
    rname_label: tk.Label
    lversion_label: tk.Label
    rversion_label: tk.Label
    lcreator_label: tk.Label
    rcreator_label: tk.Label
    llicense_label: tk.Label
    rlicense_label: tk.Label
    lcontact_label: tk.Label
    rcontact_label: tk.Label

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=background_color)

        # Button to return to the main page
        self.home_btn = tk.Button(self, text="HOME", font=small_btn_font,
                                  fg=background_color, bg=grey)
        self.home_btn.config(command=lambda: controller.show_frame(controller.pages[0]))
        self.home_btn.place(x=20, y=30, width=110, height=30)

        self.title_label = tk.Label(self, text="APP INFO", font=subtitle_font,
                                    fg=secondary_color, bg=background_color)
        self.title_label.place(x=190, y=50, width=415, height=60)

        self.lname_label = tk.Label(self, text="Name:", font=normal_text,
                                    fg=white, bg=background_color, anchor='w')
        self.lname_label.place(x=45, y=170, width=360, height=50)

        self.rname_label = tk.Label(self, text="Raspirus", font=normal_text,
                                    fg=white, bg=background_color, anchor='w')
        self.rname_label.place(x=405, y=170, width=360, height=50)

        self.lversion_label = tk.Label(self, text="Version:", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.lversion_label.place(x=45, y=220, width=360, height=50)

        self.rversion_label = tk.Label(self, text="v1.0.0", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.rversion_label.place(x=405, y=220, width=360, height=50)

        self.lcreator_label = tk.Label(self, text="Creator:", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.lcreator_label.place(x=45, y=270, width=360, height=50)

        self.rcreator_label = tk.Label(self, text="Benjamin Demetz", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.rcreator_label.place(x=405, y=270, width=360, height=50)

        self.llicense_label = tk.Label(self, text="License", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.llicense_label.place(x=45, y=320, width=360, height=50)

        self.rlicense_label = tk.Label(self, text="Alperia AG", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.rlicense_label.place(x=405, y=320, width=360, height=50)

        self.lcontact_label = tk.Label(self, text="Contact", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.lcontact_label.place(x=45, y=370, width=360, height=50)

        self.rcontact_label = tk.Label(self, text="demetzbenjamin23@gmail.com", font=normal_text,
                                       fg=white, bg=background_color, anchor='w')
        self.rcontact_label.place(x=405, y=370, width=360, height=50)
