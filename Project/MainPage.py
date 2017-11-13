import tkinter as tk
from tkinter import ttk

import time

from controlunit import ControlUnit, get_COM_ports
from Project import ControlUnitGUI
from Project import ControlUnitProt as CUP

''''
The class Mainpage is the front page of the application
It's a frame that shows which controlunit(s) are connected
'''

class Mainpage(tk.Frame):



    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.control_units = []
        self.build_screen()

    def build_screen(self):
        for control_unit in self.control_units:
            control_unit.request_disconnect()

        self.control_units = []

        ports = get_COM_ports()

        for port in ports:
            self.control_units.append(ControlUnit(port.device))

        time.sleep(2)
        refresh = ttk.Button(self, text="refresh", command=self.refresh_screen)
        refresh.grid(row=0, column=0, sticky="w")

        if len(self.control_units) == 0:
            no_devices = tk.Label(self, text="Geen apparaten aangesloten", width=50, font=(None, 20, 'bold'))
            no_devices.grid()
        else:
            for index, control_unit in enumerate(self.control_units):
                control_unit.request_connection()
                if (control_unit.connected):
                    control_unit_detail = ControlUnitGUI.ControlUnit(parent=self.parent, controller=self.controller,
                                                                     control_unit=control_unit)
                    control_unit_detail.grid(row=0, column=0, sticky="nsew")
                    self.controller.frames[control_unit.request_device_name()] = control_unit_detail
                    frame = ControlUnitFrame(self, control_unit_detail, index)

    def refresh_screen(self):
        for control_unit in self.control_units:
            self.controller.frames[control_unit.device_name].destroy()
            self.controller.frames.pop(control_unit.device_name, None)
            control_unit.request_disconnect()

        for child in self.winfo_children():
            child.destroy()

        self.controller.refresh()


class ControlUnitFrame(tk.Frame):
    def __init__(self, parent, control_unit_detail, col):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.control_unit_detail = control_unit_detail
        self.device_name = control_unit_detail.control_unit.request_device_name()
        self.name_label = tk.Label()

        margin_frame = tk.Frame(self.parent, padx=10, pady=10, width=300)  # generates a frame within the frame with padding set to 10
        margin_frame.grid(row=1, column=col)
        border_frame = tk.Frame(margin_frame, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        # generates a tk.frame within another frame, to get the padding/margin right. padx/pady set to 10
        border_frame.grid(row=1)

        # print(borderframe.grid_info())

        # a line of text
        name_label = tk.Label(border_frame, text=self.device_name, width=15, font=(None, 15, 'bold'))
        name_label.grid(row=0, column=0)

        type_label = tk.Label(border_frame, text=self.control_unit_detail.type[0], height=0, font=(None, 10, 'italic'))
        type_label.grid(row=1, column=0)

        empty_label = tk.Label(border_frame)
        empty_label.grid(row=2, column=0)

        # shows rollout status
        roll_out_label = tk.Label(border_frame, text="Uiterold: ", font=(None, 10, 'bold'))
        roll_out_label.grid(row=3, column=0, sticky=tk.N)

        # a row of white space
        self.roll_out_value = tk.Label(border_frame, text="10 cm")
        self.roll_out_value.grid(row=4, column=0, sticky=tk.N)

        # shows sensor value
        sensor_value_label = tk.Label(border_frame, text="Sensorwaarde: ", font=(None, 10, 'bold'))
        sensor_value_label.grid(row=5, column=0, sticky=tk.N)

        # a row of white space
        self.sensor_value = tk.Label(border_frame, text="1 ")
        self.sensor_value.grid(row=6, column=0, sticky=tk.N)


        # a row of white space
        empty_label = tk.Label(border_frame)
        empty_label.grid(row=7, column=0)

        ''''
        ALL BUTTONS FOR MAINPAGE
        '''
        # Button to roll up the sunshade
        roll_up_button = ttk.Button(border_frame, text="Oprollen", width=20, command=self.control_unit_detail.roll_up)
        roll_up_button.grid(row=8, column=0)

        # Button to roll out the sunshade
        roll_out_button = ttk.Button(border_frame, text="Uitrollen", width=20, command=self.control_unit_detail.roll_out)
        roll_out_button.grid(row=9, column=0)

        # Button to go to detailed information about a particulair Controlunit

        overview_button = ttk.Button(border_frame, text="Overzicht", width=20,
                          command=lambda: self.parent.controller.show_frame(self.device_name))
        overview_button.grid(row=10, column=0)

        self.update_GUI()

    def update_GUI(self):
        status = self.control_unit_detail.status
        self.roll_out_value.config(text=str(status[0])+" cm")
        self.sensor_value.config(text=str(status[1]) + " " + self.control_unit_detail.type[1])
        self.after(2000, self.update_GUI)
