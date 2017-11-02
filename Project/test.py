import tkinter as tk
from tkinter import font  as tkfont


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
        for F in (Hoofdpagina, Overzicht):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Hoofdpagina")

    def show_frame(self, page_name):
        #Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class Hoofdpagina(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        but1 = tk.Button(self, text="Oprollen")
        but1.grid(row=1, column=0)

        but2 = tk.Button(self, text="Uitrollen")
        but2.grid(row=2, column=0)

        but3 = tk.Button(self, text="Overzicht",
                            command=lambda: controller.show_frame("Overzicht"))
        but3.grid(row=3, column=0)


class Overzicht(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Overzicht", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Terug",
                           command=lambda: controller.show_frame("Hoofdpagina"))
        button.pack()


if __name__ == "__main__":
    root = SampleApp()
    root.mainloop()