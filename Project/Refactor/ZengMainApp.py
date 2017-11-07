import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import ControlUnitGUI as C
import MainPage as M
#
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt

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
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(111)


def animate(i):
    graph_data = open('graphdata.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(int(x))
            ys.append(int(y))
    ax1.clear()
    ax1.plot(xs, ys)

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
        for F in (M.Mainpage, ControlUnit):
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

class ControlUnit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ''''
        ALL LABELS FOR CONTROLUNIT
        '''

        marginframe = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
        marginframe.grid(row=1)
        borderframe = ttk.LabelFrame(marginframe,
                                     padding=10)  # generates a labelframe within frame. padding set to 10
        borderframe.grid(row=1)

        # Shows the name of the specific ControlUnit
        label = tk.Label(borderframe, text="Besturingseenheid")
        label.grid(row=0, column=0, sticky=tk.W)

        # Text for the option to set the minimum roll out value of the sunshade
        label1 = tk.Label(borderframe, text="Minimale Uitrol (in cm)")
        label1.grid(row=1, column=0, sticky=tk.W)

        # Text for the option to set the maximum roll out value of the sunshade
        label2 = tk.Label(borderframe, text="Maximale Uitrol (in cm)")
        label2.grid(row=3, column=0, sticky=tk.W)

        # Text for the option to set the trigger value of the sensor
        label3 = tk.Label(borderframe, text="Sensor Trigger")
        label3.grid(row=5, column=0, sticky=tk.W)

        # Text for the option to set the custom value of the sunshade
        label4 = tk.Label(borderframe, text="Handmatig op/uitrollen (in cm)")
        label4.grid(row=7, column=0, sticky=tk.W)

        ''''
        ALL SCALES FOR CONTROLUNIT
        '''

        # Scale is the slidebar to set the sensor trigger
        scale1 = tk.Scale(borderframe, from_=0, to=100, length=200, tickinterval=25, orient=tk.HORIZONTAL)
        scale1.set(0)
        scale1.grid(row=6, column=0)

        ''''
        ALL SPINBOXES FOR CONTROLUNIT
        '''

        # Spinbox to set the minimal unrolling position of the sunshade
        spinbox1 = tk.Spinbox(borderframe, from_=0, to=100)
        spinbox1.grid(row=2, column=0, sticky=tk.W)

        # Spinbox to set the maximum unrolling position of the sunshade
        spinbox2 = tk.Spinbox(borderframe, from_=0, to=100)
        spinbox2.grid(row=4, column=0, sticky=tk.W)

        # Spinbox to set the custom unrolling position of the sunshade
        spinbox3 = tk.Spinbox(borderframe, from_=0, to=100)
        spinbox3.grid(row=8, column=0, sticky=tk.W)

        ''''
        ALL BUTTONS FOR CONTROLUNIT
        '''

        #OK button applies the data and goes back to the mainpage
        okbut = ttk.Button(borderframe, text="OK", width=10,
                          command=lambda: controller.show_frame("Mainpage"))
        okbut.grid(row=9, column=0, sticky=tk.SW)

        # The Back button used to go back to the mainpage/frontpage
        cancelbut = ttk.Button(borderframe, text="Cancel", width=10,
                          command=lambda: controller.show_frame("Mainpage"))
        cancelbut.grid(row=9, column=0, sticky=tk.S)



        # A apply button to apply the value that is set for
        # custom unrolling position of the sunshade
        applybut = ttk.Button(borderframe, text="apply", width=10)
        applybut.grid(row=9, column=0, sticky=tk.SE)

        # Edit settings button
        editbut = ttk.Button(borderframe, text="edit")
        editbut.grid(row=0, column=0, sticky=tk.E)


        #GRAPH EDIT
        #style.use('fivethirtyeight')
        #fig = plt.figure()
        #ax1 = fig.add_subplot(111)



        canvas = FigureCanvasTkAgg(fig, self)
        #ani = animation.FuncAnimation(fig, animate, interval=1000)
        canvas.show()
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=10)

if __name__ == "__main__":
    root = ZengApp()
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    root.geometry("1280x720")           # pixelsize application
    root.title("Zeng Ltd Controller")   # GUI Title
    root.iconbitmap('Z.ico')            # GUI icon
    root.mainloop()
