"""
Tkinter tutorial Python

Author   : sentdex
Video URL: http://www.youtube.com/playlist?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk

This is Tkinter tutorial.
These codes are based on the video above.
"""

# Tkinter
import tkinter as tk
from tkinter import ttk # ttk: something like css in tkinter


# matplotlib
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# In the Part 6 Video (https://www.youtube.com/watch?v=A0gaXfM1UN0&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=2),
#
# from matplotlib.backends.backend_tkagg import NavigationToolbar2QT
#
# To run the code above, you need "pip install PyQt5"
# From Stack Overflow: https://stackoverflow.com/questions/50330320/what-to-use-instead-of-navigationtoolbar2tkagg
#      Matplotlib now wants you to use
#      NavigationToolbar2Tk
#      instead of NavigationToolbar2TkAgg.

from matplotlib.figure import Figure




# Font Configuration
LARGE_FONT = ("Verdana", 12)



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # In the Part 2 Video (https://www.youtube.com/watch?v=A0gaXfM1UN0&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=2)
        # tk.Tk.__init__(self, *args, **kwargs)
        super().__init__()

        super().wm_title('Tkinter Tutorial') # Not in the Tutorial as of Part 7
        super().geometry("800x500") # Not in the Tutorial as of Part 7

        # Container (Boss of Each Frame)
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Frame Holder
        self.frames = {}

        Pages = (
                 StartPage,
                 PageOne,
                 PageTwo,
                 PageThree
                )

        for FrameClass in Pages:
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Set Start Page Frame for Container
        self.show_frame(StartPage)

    # Show Up Frame
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        # In the Part 2 Video (https://www.youtube.com/watch?v=A0gaXfM1UN0&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=2)
        # super().__init__(self, parent)
        super().__init__(parent)

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        to_page_one_button = ttk.Button(self, text="Visit Page 1",
                                        command=lambda: controller.show_frame(PageOne))
        to_page_one_button.pack()

        to_page_two_button = ttk.Button(self, text="Visit Page 2",
                                command=lambda: controller.show_frame(PageTwo))
        to_page_two_button.pack()

        to_page_three_button = ttk.Button(self, text="Visit Graph Page",
                                command=lambda: controller.show_frame(PageThree))
        to_page_three_button.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)
        label = tk.Label(self, text="This is Page One!!", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        to_home_button = ttk.Button(self, text="Back To Home",
                            command=lambda: controller.show_frame(StartPage))
        to_home_button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)
        label = tk.Label(self, text="This is Page Two!!", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        to_home_button = ttk.Button(self, text="Back To Home",
                            command=lambda: controller.show_frame(StartPage))
        to_home_button.pack()


class PageThree(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)
        label = tk.Label(self, text="This is Page Three!!", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        to_home_button = ttk.Button(self, text="Back To Home",
                            command=lambda: controller.show_frame(StartPage))
        to_home_button.pack()

        figure = Figure(figsize=(5,5), dpi=10)
        graph = figure.add_subplot(111)
        graph.plot([1,2,3,4,5,6,7,8], [5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)




if __name__ == "__main__":
    app = SeaofBTCapp()
    app.mainloop()
