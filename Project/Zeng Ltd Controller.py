import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

'''

THIS PYTHON FILE IS MADE BY STRONGELECTRONICS.
MEMBERS :   Joep Buruma,
            Rick Lenes,
            Mark van der Molen,
            Vincent Leertouwer
MOST OF THE CODE IS WRITTEN BY US.
BUT NOT ALL SO HERE'S A LIST OFF CODE THAT IS NOT BUILD BY US.

Sources:
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
Sentdex : https://www.youtube.com/watch?v=JQ7QP5rPvjU

'''


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Mainpage, ControlUnit):
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


''''
The class Mainpage is the front page of the application
Its a frame that shows whitch controlunit(s) are connected
'''


class Mainpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ''''
        ALL LABELS FOR MAINPAGE
        '''
        # a line of text
        label1 = tk.Label(self, text="Besturingseenheid")
        label1.grid(row=1, column=0)

        # a row of white space
        label2 = tk.Label(self)
        label2.grid(row=2, column=0, sticky="E")

        # a line of text
        label2 = tk.Label(self, text="Uitgerold:")
        label2.grid(row=3, column=0)

        # a line of text
        label3 = tk.Label(self, text="Sensorwaarde:")
        label3.grid(row=4, column=0)

        ''''
        ALL BUTTONS FOR MAINPAGE
        '''
        # Button to roll up the sunshade
        but1 = ttk.Button(self, text="Oprollen", width=10)
        but1.grid(row=5, column=0)

        # Button to roll out the sunshade
        but2 = ttk.Button(self, text="Uitrollen", width=10)
        but2.grid(row=6, column=0)

        # Button to go to detailed information about a particulair Controlunit
        but3 = ttk.Button(self, text="Overzicht", width=10,
                          command=lambda: controller.show_frame("ControlUnit"))
        but3.grid(row=7, column=0)


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

        # Shows the name of the specific ControlUnit
        tk.Label(self, text="Besturingseenheid").grid(row=0, column=0, sticky=tk.W)

        # Text for the option to set the minimum roll out value of the sunshade
        label1 = tk.Label(self, text="Minimale Uitrol (in cm)")
        label1.grid(row=1, column=0, sticky=tk.W)

        # Text for the option to set the maximum roll out value of the sunshade
        label2 = tk.Label(self, text="Maximale Uitrol (in cm)")
        label2.grid(row=3, column=0, sticky=tk.W)

        # Text for the option to set the trigger value of the sensor
        label3 = tk.Label(self, text="Sensor Trigger")
        label3.grid(row=5, column=0, sticky=tk.W)

        # Text for the option to set the custom value of the sunshade
        label4 = tk.Label(self, text="Handmatig op/uitrollen (in cm)")
        label4.grid(row=7, column=0, sticky=tk.W)

        ''''
        ALL SCALES FOR CONTROLUNIT
        '''

        # Scale is the slidebar to set the sensor trigger
        scale1 = tk.Scale(self, from_=0, to=100, length=200, tickinterval=25, orient=tk.HORIZONTAL)
        scale1.set(0)
        scale1.grid(row=6, column=0)

        ''''
        ALL SPINBOXES FOR CONTROLUNIT
        '''

        # Spinbox to set the minimal unrolling position of the sunshade
        spinbox1 = tk.Spinbox(self, from_=0, to=100)
        spinbox1.grid(row=2, column=0, sticky=tk.W)

        # Spinbox to set the maximum unrolling position of the sunshade
        spinbox2 = tk.Spinbox(self, from_=0, to=100)
        spinbox2.grid(row=4, column=0, sticky=tk.W)

        # Spinbox to set the custom unrolling position of the sunshade
        spinbox3 = tk.Spinbox(self, from_=0, to=100)
        spinbox3.grid(row=8, column=0, sticky=tk.W)

        ''''
        ALL BUTTONS FOR CONTROLUNIT
        '''

        # The Back button used to go back to the mainpage/frontpage
        but1 = ttk.Button(self, text="Terug", width=10,
                          command=lambda: controller.show_frame("Mainpage"))
        but1.grid(row=9, column=0, sticky=tk.W)

        # A apply button to apply the value that is set for
        # custom unrolling position of the sunshade
        but2 = ttk.Button(self, text="apply", width=10)
        but2.grid(row=8, column=0, sticky=tk.E)

        # Edit settings button
        but3 = ttk.Button(self, text="edit")
        but3.grid(row=0, column=0, sticky=tk.NE)


if __name__ == "__main__":
    root = SampleApp()
    root.title("Zeng Ltd Controller")   # GUI Title
    root.iconbitmap('Z.ico')            # GUI icon
    root.mainloop()
