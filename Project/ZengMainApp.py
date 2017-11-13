#Import for all used libraries
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import ControlUnitGUI as C
import MainPage as M
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from tkinter import messagebox

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
        self.container = ttk.Frame(self, padding=10)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # for #F in (M.Mainpage, C.ControlUnit):
        # page_name = F.__name__
        # frame = F(parent=container, controller=self)
        # self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        # frame.grid(row=0, column=0, sticky="nsew")

        self.frame = M.Mainpage(parent=self.container, controller=self)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frames[M.Mainpage.__name__] = self.frame
        self.show_frame("Mainpage")

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit)

        def show_about():
            messagebox.showwarning(
                "About",
                "This application was made by StrongElectronics!"
            )

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About",
                              accelerator="Ctrl-A",
                              command=show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.config(menu=menubar)

    def refresh(self):
        self.frame.destroy()
        frame = M.Mainpage(parent=self.container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        self.frames[M.Mainpage.__name__] = frame
        self.show_frame("Mainpage")

    def show_frame(self, page_name):
        # Shows a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    root = ZengApp()
#    ani_Light = animation.FuncAnimation(C.fig_Light, C.animate_Light, interval=1000) # 30000 ms = 30
    root.geometry("1280x350")           # pixelsize application
    root.title("Zeng Ltd Controller")   # GUI Title
    root.iconbitmap('Z.ico')            # GUI icon
    root.mainloop()




