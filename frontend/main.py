from pages.MainPage import MainPage
# Importing the tkinter module
import tkinter as tk

# Used for styling the GUI
from tkinter import ttk

# FOLLOW THIS: https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Test Application")

        # creating a frame and assigning it to container
        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (MainPage, SidePage, CompletionScreen):
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
    app = MainPage(str("sun-valley"), str("dark"))
    app.run()

# root = Tk()
# root.geometry("800x480")
# frame = Frame(root)
# app = MainPage()
# theme = str("sun-valley")

# if __name__ == "__main__":
#   app.root.mainloop()
