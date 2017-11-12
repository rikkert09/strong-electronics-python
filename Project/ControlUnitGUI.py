import tkinter as tk

from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

from Project import ControlUnitProt as CUP

matplotlib.use("TkAgg")
style.use('ggplot')

''''
The class ControlUnit is the page that will pop-up if you press the button "overzicht"
from the class Mainpage. The class ControlUnit is used as a overview to see data of a particulair
Controlunit in which you can adjust settings about that particular Controlunit.
'''


class ControlUnit(tk.Frame):
    def __init__(self, parent, controller, control_unit):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.control_unit = control_unit
        self.status = control_unit.request_status()
        self.type = control_unit.request_sensor_type()
        self.x_Values = 60 * [0]
        self.y_Values = 60 * [control_unit.request_status()[1]]
        self.time = 0
        self.fig_Temp = Figure(figsize=(10, 4), dpi=75)
        self.a_Temp = self.fig_Temp.add_subplot(111)

        # generates a frame within the frame with padding set to 10
        margin_frame = ttk.Frame(self, padding=10)
        margin_frame.grid(row=1)
        # generates a labelframe within frame. padding set to 10
        border_frame = tk.Frame(margin_frame, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        border_frame.grid(row=1)

        name = "Besturingseenheid"
        new_name = Entry(border_frame)
        new_name.insert(0, name)

        # Shows the name of the specific ControlUnit
        name_label = tk.Label(border_frame, text=name)
        name_label.grid(row=0, column=0, sticky=tk.W)

        # Text for the option to set the minimum roll out value of the sunshade
        minroll_label = tk.Label(border_frame, text="Minimale Uitrol (in cm)", font=(None, 9, 'bold'))
        minroll_label.grid(row=1, column=0, sticky=tk.W)

        # Text for the option to set the maximum roll out value of the sunshade
        maxroll_label = tk.Label(border_frame, text="Maximale Uitrol (in cm)", font=(None, 9, 'bold'))
        maxroll_label.grid(row=3, column=0, sticky=tk.W)

        # Text for the option to set the trigger value of the sensor
        sensor_trig_label = tk.Label(border_frame, text="Sensor Trigger", font=(None, 9, 'bold'))
        sensor_trig_label.grid(row=5, column=0, sticky=tk.W)

        # Text for the option to set the custom value of the sunshade
        custom_roll_label = tk.Label(border_frame, text="Handmatig op/uitrollen (in cm)", font=(None, 9, 'bold'))
        custom_roll_label.grid(row=7, column=0, sticky=tk.W)

        # Scale is the slidebar to set the sensor trigger
        self.sensor_trig_scale = tk.Scale(border_frame, from_=0, to=100, length=200, tickinterval=25,
                                          orient=tk.HORIZONTAL)
        # sets value
        self.sensor_trig_scale.set(control_unit.request_setting(CUP.SETTING_SENSOR_TRIG_VAL))
        self.sensor_trig_scale.grid(row=6, column=0)

        ''''
        ALL SPINBOXES FOR CONTROLUNIT
        '''

        # Spinbox to set the minimal unrolling position of the sunshade
        self.min_roll_spinbox = tk.Spinbox(border_frame, from_=0, to=200, validate='all')
        # validates if int
        self.min_roll_spinbox["validatecommand"] = (self.min_roll_spinbox.register(self.validate), '%P', '%i', '%d')
        self.min_roll_spinbox.delete(0, "end")  # clears value
        self.min_roll_spinbox.insert(0, control_unit.request_setting(CUP.SETTING_MIN_EXTEND))  # sets value
        self.min_roll_spinbox.grid(row=2, column=0, sticky=tk.W)

        # Spinbox to set the maximum unrolling position of the sunshade
        self.max_roll_spinbox = tk.Spinbox(border_frame, from_=0, to=200, validate='all')
        # validates if int
        self.max_roll_spinbox["validatecommand"] = (self.max_roll_spinbox.register(self.validate), '%P', '%i', '%d')
        self.max_roll_spinbox.delete(0, "end")  # clears value
        self.max_roll_spinbox.insert(0, control_unit.request_setting(CUP.SETTING_MAX_EXTEND))  # sets value
        self.max_roll_spinbox.grid(row=4, column=0, sticky=tk.W)

        # Spinbox to set the custom unrolling position of the sunshade
        self.custom_roll_spinbox = tk.Spinbox(border_frame, from_=0, to=200, validate='all')
        # validates if int
        self.custom_roll_spinbox["validatecommand"] = (self.custom_roll_spinbox.register(self.validate), '%P', '%i', '%d')
        self.custom_roll_spinbox.delete(0, "end")  # clears value
        self.custom_roll_spinbox.insert(0, 50)  # sets value
        self.custom_roll_spinbox.grid(row=8, column=0, sticky=tk.W)

        # OK button applies the data and goes back to the mainpage
        ok_button = ttk.Button(border_frame, text="OK", width=10,
                           command=lambda: controller.show_frame("Mainpage"))
        ok_button.grid(row=9, column=0, sticky=tk.SW)

        # The Back button used to go back to the mainpage/frontpage
        cancel_button = ttk.Button(border_frame, text="Cancel", width=10,
                               command=lambda: controller.show_frame("Mainpage"))
        cancel_button.grid(row=9, column=0, sticky=tk.S)

        # Applies the values that are set in the spinboxes and scale
        # custom unrolling position of the sunshade
        apply_button = ttk.Button(border_frame, text="apply", width=10)
        apply_button.bind("<Button-1>", self.get_data)
        apply_button.grid(row=9, column=0, sticky=tk.SE)

        # Button to edit the control unit name
        edit_button = ttk.Button(border_frame, text="edit")
        edit_button.bind("<Button-1>", self.edit_name)
        edit_button.grid(row=0, column=0, sticky=tk.E)

        margin_frame2 = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
        margin_frame2.grid(row=1, column=5)
        # generates a labelframe within frame. padding set to 10
        border_frame2 = tk.Frame(margin_frame2, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        border_frame2.grid(row=0, column=5)

        margin_frame2 = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
        margin_frame2.grid(row=1, column=5)
        # generates a labelframe within frame. padding set to 10
        border_frame2 = tk.Frame(margin_frame2, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        border_frame2.grid(row=0, column=5)

        # Shows label of text
        graph_info = tk.Label(border_frame2, text="Informatie Besturingseenheid", font=(None, 9, 'bold'))
        graph_info.grid(row=0, column=0, sticky=tk.W)

        empty_block = tk.Label(border_frame2)
        empty_block.grid(row=1, column=0, sticky=tk.W)

        type_graph_text = tk.Label(border_frame2, text="Type Grafiek:", font=(None, 9, 'bold'))
        type_graph_text.grid(row=2, column=0, sticky=tk.W)

        graph2_text = tk.Label(border_frame2, text=self.type)
        graph2_text.grid(row=3, column=0, sticky=tk.W)

        empty_block2 = tk.Label(border_frame2)
        empty_block2.grid(row=4, column=0, sticky=tk.W)

        x_as_label = tk.Label(border_frame2, text="X-as : Tijd in seconden", font=(None, 9, 'bold'))
        x_as_label.grid(row=5, column=0, sticky=tk.W)

        y_as_label = tk.Label(border_frame2, text="Y-as : Lichtintensiteit in lx", font=(None, 9, 'bold'))
        y_as_label.grid(row=6, column=0, sticky=tk.W)

        empty_block3 = tk.Label(border_frame2)
        empty_block3.grid(row=7, column=0, sticky=tk.W)

        # Shows the label with the temperature
        self.lux_label = tk.Label(border_frame2, text="Lichtintensiteit in lux : ", font=(None, 9, 'bold'))
        self.lux_label.grid(row=8, column=0, sticky=tk.W)

        self.roll_out_text = tk.Label(border_frame2, text="Uitgerold (cm): ", font=(None, 9, 'bold'))
        self.roll_out_text.grid(row=9, column=0, sticky=tk.W)

        empty_block4 = tk.Label(border_frame2)
        empty_block4.grid(row=10, column=0, sticky=tk.W)

        back_button = ttk.Button(border_frame2, text="Terug naar de Hoofdpagina",
                                command=lambda: controller.show_frame("Mainpage"))
        back_button.grid(row=11, column=0, rowspan=4, sticky=tk.S)

        self.update_GUI()

    # validates if value is an integer
    def validate(self, instr, i, acttyp):  # validates if value is an integer
        ind = int(i)
        if acttyp == '1':  # insert
            if not instr[ind].isdigit():
                return False
        return True

    def edit_name(self):
        print("Not implemented yet")

    def to_main_page(self):
        self.controller.show_frame("Mainpage")

    def data_error(self):
        messagebox.showwarning("Foutmelding",
                               "De minimale uitrolwaarde mag niet hoger zijn dan de maximale uitrolwaarde.")

    def data_error2(self):
        messagebox.showwarning("Foutmelding",
                               "De handmatige uitrolwaarde valt niet binnen het minimum of maximum")

    def data_error3(self):
        messagebox.showwarning("Foutmelding",
                               "Waarde te hoog!")

    def get_data(self, a):
        # retrieves data from all spinboxes and converts them to ints
        min_roll = int(self.min_roll_spinbox.get())
        max_roll = int(self.max_roll_spinbox.get())
        custom_roll = int(self.custom_roll_spinbox.get())
        # the .get() function on a scale already retrieves an int
        sensor_trig = self.sensor_trig_scale.get()
        #   create list of all retrieved data
        data_dict = {CUP.SETTING_MIN_EXTEND: min_roll, CUP.SETTING_MAX_EXTEND: max_roll,
                     CUP.SETTING_EXTEND_TO_VAL: custom_roll, CUP.SETTING_SENSOR_TRIG_VAL: sensor_trig}

        # checks if maxroll is greater than minroll, otherwise throws an error
        if min_roll > max_roll:
            print("Throw an error")
            self.data_error()
        # throws error if customroll is not within minimum and max
        elif custom_roll > max_roll or custom_roll < min_roll:
            self.data_error2()
        # throws error when value is too high
        elif min_roll > 200 or max_roll > 200 or custom_roll > 200:
            self.data_error3()
        else:
            self.apply(data_dict)

    def apply(self, data_dict):
        for key, value in data_dict.items():
            self.control_unit.update_setting(key, value)
            print(self.control_unit.request_setting(key))

    def update_GUI(self):
        self.time = self.time + 1

        self.status = self.control_unit.request_status()
        self.x_Values.append((self.time))
        self.y_Values.append(self.status[1])
        self.x_Values = self.x_Values[1:]
        self.y_Values = self.y_Values[1:]
        self.a_Temp.clear()
        self.a_Temp.plot(self.x_Values, self.y_Values)
        self.a_Temp.set_ylim((0, 1000 if max(self.y_Values) < 1000 else max(self.y_Values) + 100))

        canvas_temp = FigureCanvasTkAgg(self.fig_Temp, self)
        canvas_temp.show()
        canvas_temp.get_tk_widget().grid(row=0, column=2, rowspan=10)

        self.lux_label.config(text="Lichtintensiteit in lux : " + str(self.status[1]))
        self.roll_out_text.config(text="Uitgerold (cm): " + str(self.status[0]))

        #self.update()
        self.after(1000, self.update_GUI)



