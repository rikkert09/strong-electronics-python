import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import ControlUnitGUI as C
import MainPage as M

'''
THIS PYTHON FILE IS MADE BY STRONGELECTRONICS.
MEMBERS :   Joep Buruma,
            Rick Lenes,
            Mark van der Molen,
            Vincent Leertouwer
MOST OF THE CODE IS WRITTEN BY US.
BUT NOT ALL SO HERE'S A LIST OF CODE THAT IS NOT BUILT BY US.

Sources:
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
Sentdex : https://www.youtube.com/watch?v=JQ7QP5rPvjU

'''

class ZengApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        # uses ttk.Frame with padding set to 10
        container = ttk.Frame(self, padding=10)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (M.Mainpage, C.ControlUnit):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Mainpage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    root = ZengApp()
    root.geometry("1280x720")           # pixelsize application
    root.title("Zeng Ltd Controller")   # GUI Title
    root.iconbitmap('Z.ico')            # GUI icon
    root.mainloop()
