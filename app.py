import tkinter as tk


LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        # In the Part 2 Video (https://www.youtube.com/watch?v=A0gaXfM1UN0&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=2)
        # tk.Tk.__init__(self, *args, **kwargs)
        super().__init__()

        # Container (Boss of Each Frame)
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Frame Holder
        self.frames = {}

        # Start Page Frame
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, sticky=tk.NSEW)
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

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(self, parent)
        label = tk.Label(self, text="Back to Home", font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



if __name__ == "__main__":
    app = SeaofBTCapp()
    app.mainloop()
