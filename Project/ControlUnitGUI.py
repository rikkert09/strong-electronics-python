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
import pylab

matplotlib.use("TkAgg")

''''
The class ControlUnit is the page that will pop-up if you press the button "overzicht"
from the class Mainpage. The class ControlUnit is used as a overview to see data of a particulair
Controlunit in which you can adjust settings about that particular Controlunit.
'''
style.use('ggplot')
fig_Light = Figure(figsize=(10,4), dpi = 75)
a_Light = fig_Light.add_subplot(111)
# a_Light.margins(0)

fig_Temp = Figure(figsize=(10,4), dpi = 75)
a_Temp = fig_Temp.add_subplot(111)

#Function of the graph for the light sensor
def animate_Light(i):
    graph_data = open('Light.txt', 'r').read()
    lines = graph_data.split('\n')
    x_Values = []
    y_Values = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x_Values.append(int(x))
            y_Values.append(int(y))
    a_Light.clear()
    a_Light.plot(x_Values, y_Values)

#Function of the graph for the Temp sensor
def animate_Temp(i):
    graph_data = open('Temp.txt', 'r').read()
    lines = graph_data.split('\n')
    x_Values = []
    y_Values = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x_Values.append(int(x))
            y_Values.append(int(y))
    a_Temp.clear()
    a_Temp.plot(x_Values, y_Values)

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

        name="Besturingseenheid"

        newname = Entry(borderframe)
        newname.insert(0, name)

        # def changename(event=None):
        #     # editname.newedit.grid_forget()
        #     newlabel = tk.Label(borderframe, text="Temperatuursensor", width=17)
        #     newlabel.grid(row=0, column=0, sticky=tk.W)

        def editname(event=None):
            print("Not implemented yet")
            # namelabel.grid_forget()
            # editbut.grid_forget()
            # newname = Entry(borderframe)
            # newname.insert(0, name)
            # newname.grid(row=0, column=0, sticky=tk.W)
            # newedit = ttk.Button(borderframe, text="OK")
            # newedit.bind("<Button-1>", changename)
            # newedit.grid(row=0, column=0, sticky=tk.E)

        # Shows the name of the specific ControlUnit
        namelabel = tk.Label(borderframe, text=name)
        namelabel.grid(row=0, column=0, sticky=tk.W)

        # Text for the option to set the minimum roll out value of the sunshade
        minrolllabel = tk.Label(borderframe, text="Minimale Uitrol (in cm)")
        minrolllabel.grid(row=1, column=0, sticky=tk.W)

        # Text for the option to set the maximum roll out value of the sunshade
        maxrolllabel = tk.Label(borderframe, text="Maximale Uitrol (in cm)")
        maxrolllabel.grid(row=3, column=0, sticky=tk.W)

        # Text for the option to set the trigger value of the sensor
        sensortriglabel = tk.Label(borderframe, text="Sensor Trigger")
        sensortriglabel.grid(row=5, column=0, sticky=tk.W)

        # Text for the option to set the custom value of the sunshade
        customrolllabel = tk.Label(borderframe, text="Handmatig op/uitrollen (in cm)")
        customrolllabel.grid(row=7, column=0, sticky=tk.W)

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


        # Applies the values that are set in the spinboxes and scale
        # custom unrolling position of the sunshade
        applybut = ttk.Button(borderframe, text="apply", width=10)
        applybut.bind("<Button-1>", getdata)
        applybut.grid(row=9, column=0, sticky=tk.SE)

        # Button to edit the control unit name
        editbut = ttk.Button(borderframe, text="edit")
        editbut.bind("<Button-1>", editname)
        editbut.grid(row=0, column=0, sticky=tk.E)

        '''
        Second block of Unit Data
        '''

        marginframe2 = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
        marginframe2.grid(row=1, column=5)
        # generates a labelframe within frame. padding set to 10
        borderframe2 = tk.Frame(marginframe2, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        borderframe2.grid(row=0, column=5)

        # Shows label of text
        Graphinfo = tk.Label(borderframe2, text="Informatie Besturingseenheid")
        Graphinfo.grid(row=0, column=0, sticky=tk.W)

        Empty_Block = tk.Label(borderframe2)
        Empty_Block.grid(row=1, column=0, sticky=tk.W)

        Type_Graph_Text = tk.Label(borderframe2, text="Type Grafiek:")
        Type_Graph_Text.grid(row=2, column=0, sticky=tk.W)

        Graph2_Text = tk.Label(borderframe2, text="Temperatuur")
        Graph2_Text.grid(row=3, column=0, sticky=tk.W)

        Empty_Block2 = tk.Label(borderframe2)
        Empty_Block2.grid(row=4, column=0, sticky=tk.W)

        X_as_label = tk.Label(borderframe2, text="X-as : Tijd in seconden")
        X_as_label.grid(row=5, column=0, sticky=tk.W)

        Y_as_label = tk.Label(borderframe2, text="Y-as : Temperatuur in °C")
        Y_as_label.grid(row=6, column=0, sticky=tk.W)

        Empty_Block3 = tk.Label(borderframe2)
        Empty_Block3.grid(row=7, column=0, sticky=tk.W)

        # Shows the label with the temperature
        TempText = tk.Label(borderframe2, text="Huidige temperatuur(°C) : ")
        TempText.grid(row=8, column=0, sticky=tk.W)

        Rollout_Text = tk.Label(borderframe2, text="Percentage uitgerold : ")
        Rollout_Text.grid(row=9, column=0, sticky=tk.W)

        Empty_Block4 = tk.Label(borderframe2)
        Empty_Block4.grid(row=10, column=0, sticky=tk.W)

        BackButton = ttk.Button(borderframe2, text="Terug naar de Hoofdpagina",
                                command=lambda: controller.show_frame("Mainpage"))
        BackButton.grid(row=11, column=0, rowspan=4, sticky=tk.S)

        #drawing of the light sensor graph into the frame
        canvas_Light = FigureCanvasTkAgg(fig_Light, self)
        canvas_Light.show()
        canvas_Light.get_tk_widget().grid(row=0, column=2, rowspan=10)
        # print(grid_info())

        #drawing of the Temp sensor graph into the frame
        canvas_Temp = FigureCanvasTkAgg(fig_Temp, self)
        canvas_Temp.show()
        canvas_Temp.get_tk_widget().grid(row=300, column=2, rowspan=4)

        # fig_Light.set_ylim([0, 1000])