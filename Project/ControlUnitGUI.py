import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style

matplotlib.use("TkAgg")

''''
The class ControlUnit is the page that will pop-up if you press the button "overzicht"
from the class Mainpage. The class ControlUnit is used as a overview to see data of a particulair
Controlunit in which you can adjust settings about that particular Controlunit.
'''
style.use('ggplot')
fig_light = Figure(figsize=(10,4), dpi = 75)
a_light = fig_light.add_subplot(111)
# a_Light.margins(0)

fig_temp = Figure(figsize=(10,4), dpi = 75)
a_temp = fig_temp.add_subplot(111)


#   Function of the graph for the light sensor
def animate_light(i):
    graph_data = open('Light.txt', 'r').read()
    lines = graph_data.split('\n')
    x_values = []
    y_values = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x_values.append(int(x))
            y_values.append(int(y))
    a_light.clear()
    a_light.plot(x_values, y_values)


#   Function of the graph for the Temp sensor
def animate_temp(i):
    graph_data = open('Temp.txt', 'r').read()
    lines = graph_data.split('\n')
    x_values = []
    y_values = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x_values.append(int(x))
            y_values.append(int(y))
    a_temp.clear()
    a_temp.plot(x_values, y_values)


class ControlUnit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # generates a frame within the frame with padding set to 10
        marginframe = ttk.Frame(self, padding=10)
        marginframe.grid(row=1)
        # generates a labelframe within frame. padding set to 10
        borderframe = tk.Frame(marginframe, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        borderframe.grid(row=1)

        name = "Besturingseenheid"
        newname = Entry(borderframe)
        newname.insert(0, name)

        def editname():
            print("Not implemented yet")

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

        # Scale is the slidebar to set the sensor trigger
        sensortrigscale = tk.Scale(borderframe, from_=0, to=100, length=200, tickinterval=25,
                                   orient=tk.HORIZONTAL)
        # sets value
        sensortrigscale.set(25)
        sensortrigscale.grid(row=6, column=0)

        ''''
        ALL SPINBOXES FOR CONTROLUNIT
        '''

        # validates if value is an integer
        def validate(instr, i, acttyp): # validates if value is an integer
            ind = int(i)
            if acttyp == '1':  # insert
                if not instr[ind].isdigit():
                    return False
            return True

        # Spinbox to set the minimal unrolling position of the sunshade
        minrollspinbox = tk.Spinbox(borderframe, from_=0, to= 200, validate='all')
        # validates if int
        minrollspinbox["validatecommand"] = (minrollspinbox.register(validate),'%P','%i','%d')
        minrollspinbox.delete(0, "end") # clears value
        minrollspinbox.insert(0, 0)    # sets value
        minrollspinbox.grid(row=2, column=0, sticky=tk.W)

        # Spinbox to set the maximum unrolling position of the sunshade
        maxrollspinbox = tk.Spinbox(borderframe, from_=0, to=200, validate='all')
        # validates if int
        maxrollspinbox["validatecommand"] = (maxrollspinbox.register(validate),'%P','%i','%d')
        maxrollspinbox.delete(0, "end") # clears value
        maxrollspinbox.insert(0, 200)    # sets value
        maxrollspinbox.grid(row=4, column=0, sticky=tk.W)

        # Spinbox to set the custom unrolling position of the sunshade
        customrollspinbox = tk.Spinbox(borderframe, from_=0, to=200, validate='all')
        # validates if int
        customrollspinbox["validatecommand"] = (customrollspinbox.register(validate),'%P','%i','%d')
        customrollspinbox.delete(0, "end")  # clears value
        customrollspinbox.insert(0, 30)     # sets value
        customrollspinbox.grid(row=8, column=0, sticky=tk.W)

        def dataerror():
            messagebox.showwarning("Foutmelding",
                                   "De minimale uitrolwaarde mag niet hoger zijn dan de maximale uitrolwaarde.")
        def dataerror2():
            messagebox.showwarning("Foutmelding",
                                   "De handmatige uitrolwaarde valt niet binnen het minimum of maximum")
        def dataerror3():
            messagebox.showwarning("Foutmelding",
                                   "Waarde te hoog!")
        def getdata():
            # retrieves data from all spinboxes and converts them to ints
            minroll = int(minrollspinbox.get())
            maxroll = int(maxrollspinbox.get())
            customroll = int(customrollspinbox.get())
            # the .get() function on a scale already retrieves an int
            sensortrig = sensortrigscale.get()
            #   create list of all retrieved data
            datalist = [minroll, maxroll, customroll, sensortrig]

            # checks if maxroll is greater than minroll, otherwise throws an error
            if minroll > maxroll:
                print("Throw an error")
                dataerror()
            # throws error if customroll is not within minimum and max
            elif customroll > maxroll or customroll < minroll:
                dataerror2()
            # throws error when value is too high
            elif minroll > 200 or maxroll > 200 or customroll > 200:
                dataerror3()
            else:
                print(datalist)

        def okbut():
            controller.show_frame("Mainpage")

        # OK button applies the data and goes back to the mainpage
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
        This is the legend its build in a loop so depending on the value of test1
        1 = currently Temp
        2 = currently Light
        '''

        test1 = 2

        if test1 == 1:

            marginframe2 = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
            marginframe2.grid(row=1, column=5)
            # generates a labelframe within frame. padding set to 10
            borderframe2 = tk.Frame(marginframe2, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
            borderframe2.grid(row=0, column=5)

            # Shows label of text
            graphinfo = tk.Label(borderframe2, text="Informatie Besturingseenheid")
            graphinfo.grid(row=0, column=0, sticky=tk.W)

            empty_block = tk.Label(borderframe2)
            empty_block.grid(row=1, column=0, sticky=tk.W)

            type_graph_text = tk.Label(borderframe2, text="Type Grafiek:")
            type_graph_text.grid(row=2, column=0, sticky=tk.W)

            graph2_text = tk.Label(borderframe2, text="Temperatuur")
            graph2_text.grid(row=3, column=0, sticky=tk.W)

            empty_block2 = tk.Label(borderframe2)
            empty_block2.grid(row=4, column=0, sticky=tk.W)

            x_as_label = tk.Label(borderframe2, text="X-as : Tijd in seconden")
            x_as_label.grid(row=5, column=0, sticky=tk.W)

            y_as_label = tk.Label(borderframe2, text="Y-as : Temperatuur in °C")
            y_as_label.grid(row=6, column=0, sticky=tk.W)

            empty_block3 = tk.Label(borderframe2)
            empty_block3.grid(row=7, column=0, sticky=tk.W)

            # Shows the label with the temperature
            temptext = tk.Label(borderframe2, text="Huidige temperatuur(°C) : ")
            temptext.grid(row=8, column=0, sticky=tk.W)

            rollout_text = tk.Label(borderframe2, text="Percentage uitgerold : ")
            rollout_text.grid(row=9, column=0, sticky=tk.W)

            empty_block4 = tk.Label(borderframe2)
            empty_block4.grid(row=10, column=0, sticky=tk.W)

            backbutton = ttk.Button(borderframe2, text="Terug naar de Hoofdpagina",
                                    command=lambda: controller.show_frame("Mainpage"))
            backbutton.grid(row=11, column=0, rowspan=4, sticky=tk.S)

        elif test1 == 2:

            marginframe2 = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
            marginframe2.grid(row=1, column=5)
            # generates a labelframe within frame. padding set to 10
            borderframe2 = tk.Frame(marginframe2, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
            borderframe2.grid(row=0, column=5)

            # Shows label of text
            graphinfo = tk.Label(borderframe2, text="Informatie Besturingseenheid")
            graphinfo.grid(row=0, column=0, sticky=tk.W)

            empty_block = tk.Label(borderframe2)
            empty_block.grid(row=1, column=0, sticky=tk.W)

            type_graph_text = tk.Label(borderframe2, text="Type Grafiek:")
            type_graph_text.grid(row=2, column=0, sticky=tk.W)

            graph2_text = tk.Label(borderframe2, text="Licht")
            graph2_text.grid(row=3, column=0, sticky=tk.W)

            empty_block2 = tk.Label(borderframe2)
            empty_block2.grid(row=4, column=0, sticky=tk.W)

            x_as_label = tk.Label(borderframe2, text="X-as : Tijd in seconden")
            x_as_label.grid(row=5, column=0, sticky=tk.W)

            y_as_label = tk.Label(borderframe2, text="Y-as : Lichtintensiteit in lx")
            y_as_label.grid(row=6, column=0, sticky=tk.W)

            empty_block3 = tk.Label(borderframe2)
            empty_block3.grid(row=7, column=0, sticky=tk.W)

            # Shows the label with the temperature
            luxtext = tk.Label(borderframe2, text="Lichtintensiteit in lux : ")
            luxtext.grid(row=8, column=0, sticky=tk.W)

            rollout_text = tk.Label(borderframe2, text="Percentage uitgerold : ")
            rollout_text.grid(row=9, column=0, sticky=tk.W)

            empty_block4 = tk.Label(borderframe2)
            empty_block4.grid(row=10, column=0, sticky=tk.W)

            backbutton = ttk.Button(borderframe2, text="Terug naar de Hoofdpagina",
                                    command=lambda: controller.show_frame("Mainpage"))
            backbutton.grid(row=11, column=0, rowspan=4, sticky=tk.S)

        '''
        Drawing of the graph and its position (NOT the animation!)
        '''

        #   drawing of the light sensor graph into the frame
        canvas_light = FigureCanvasTkAgg(fig_light, self)
        canvas_light.show()
        canvas_light.get_tk_widget().grid(row=0, column=2, rowspan=10)

        #   drawing of the Temp sensor graph into the frame
        canvas_temp = FigureCanvasTkAgg(fig_temp, self)
        canvas_temp.show()
        canvas_temp.get_tk_widget().grid(row=0, column=2, rowspan=10)
