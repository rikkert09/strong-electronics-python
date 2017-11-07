import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

''''
The class ControlUnit is the page that will pop-up if you press the button "overzicht"
from the class Mainpage. The class ControlUnit is used as a overview to see data of a particulair
Controlunit in which you can adjust settings about that particulair Controlunit.
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

class ControlUnit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ''''
        ALL LABELS FOR CONTROLUNIT
        '''

        marginframe = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
        marginframe.grid(row=1)
        borderframe = tk.Frame(marginframe, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)  # generates a labelframe within frame. padding set to 10
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
        sensortrigscale = tk.Scale(borderframe, from_=0, to=100, length=200, tickinterval=25,
                                   orient=tk.HORIZONTAL)
        sensortrigscale.set(0)
        sensortrigscale.grid(row=6, column=0)

        ''''
        ALL SPINBOXES FOR CONTROLUNIT
        '''

        # Spinbox to set the minimal unrolling position of the sunshade
        minrollspinbox = tk.Spinbox(borderframe, from_=0, to=100)
        minrollspinbox.grid(row=2, column=0, sticky=tk.W)

        # Spinbox to set the maximum unrolling position of the sunshade
        maxrollspinbox = tk.Spinbox(borderframe, from_=0, to=100)
        maxrollspinbox.grid(row=4, column=0, sticky=tk.W)

        # Spinbox to set the custom unrolling position of the sunshade
        customrollspinbox = tk.Spinbox(borderframe, from_=0, to=100)
        customrollspinbox.grid(row=8, column=0, sticky=tk.W)

        ''''
        ALL BUTTONS FOR CONTROLUNIT
        '''



        def getdata(event=None):
            minroll = int(minrollspinbox.get()) # retrieves data from all spinboxes and converts them to ints
            maxroll = int(maxrollspinbox.get())
            customroll = int(customrollspinbox.get())
            sensortrig = sensortrigscale.get() # the .get() function on a scale already retrieves an int
            datalist = [minroll, maxroll, customroll, sensortrig] # create list of all retrieved data

            print(datalist)

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
        applybut.bind("<Button-1>", getdata)
        applybut.grid(row=9, column=0, sticky=tk.SE)

        # Edit settings button
        editbut = ttk.Button(borderframe, text="edit")
        editbut.grid(row=0, column=0, sticky=tk.E)

        canvas = FigureCanvasTkAgg(fig, self)
        #ani = animation.FuncAnimation(fig, animate, interval=1000)
        canvas.show()
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=10)