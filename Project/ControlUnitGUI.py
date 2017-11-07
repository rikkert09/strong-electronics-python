import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt

''''
The class ControlUnit is the page that will pop-up if you press the button "overzicht"
from the class Mainpage. The class ControlUnit is used as a overview to see data of a particulair
Controlunit in which you can adjust settings about that particulair Controlunit.
'''


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
        
        f = Figure(figsize=(16, 8), dpi=60) #plt.figure()
        a = f.add_subplot(1,1,1)

        def animate(i):
            graph_data = open('graphdata.txt', 'r').read() #kan weg we gebruiken geen txt
            lines = graph_data.split('\n')              #dit moet var = ingelezen data
            xValues = []
            yValues = []
            for line in lines:
                if len(line) > 1:
                    x, y = line.split(',')
                    xValues.append(x) # moet de seconden er aanplakken
                    yValues.append(y) # drukt de waarde voor de tijd af
                a.clear()
                a.plot(xValues, yValues)

        canvas = FigureCanvasTkAgg(f, self)
        ani = animation.FuncAnimation(f, animate, interval=1000)
        canvas.show()
        canvas.get_tk_widget().grid(row=0, column=2, rowspan=10)