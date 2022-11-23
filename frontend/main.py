from pages.MainPage import MainPage
from pages.SettingsPage import SettingsPage
from pages.LoadingPage import LoadingPage
from pages.InfoPage import InfoPage
from pages.VirusPage import VirusPage
from pages.ClearPage import ClearPage
# Importing the tkinter module
import tkinter as tk


class windows(tk.Tk):
    # Items have a fixed order! -> Contains all pages as a reference
    pages = (MainPage, SettingsPage, LoadingPage, InfoPage, VirusPage, ClearPage)

    def __init__(self):
        # Adding a title to the window
        tk.Tk.__init__(self)
        self.wm_title("Raspirus")
        self.wm_geometry("800x480")
        self.wm_resizable(width=False, height=False)

        # creating a frame and assigning it to container
        container = tk.Frame(self)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in self.pages:
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


if __name__ == "__main__":
    app = windows()
    app.mainloop()
