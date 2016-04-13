from tkinter import *

root = Tk()
LARGE_FONT = ("Verdana", 12)

class dqsLearn(Frame): # include inheritance as parameters
    def __init__(self, *args, **kwargs): # args(arguments) = any number of variables kwargs(kewyword arguments) = passing dictionaries/data structures
        # tk.Tk.__init__(self, *args, **kwargs)
        Frame.__init__(self, *args, **kwargs) # Initialise the frame
        container = Frame(self) # Assign container as a frame which we can alter

        # allow the container to expand into the entire window
        container.pack(side="top", fill="both", expand=True)

        # set up the containing window
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # collection of frames i.e. login, menu, lesson, test
        self.frames = {}

        # set the current frame
        frame = Login(container, self) # Assign the login screen to the first frame to be passed

        self.frames[Login] = frame # Set initial frame to the login screen

        frame.grid(row=0, column=0, sticky="nsew") # nsew stretches everything to all edges, fits to size of window

        self.show_frame(Login)

    def show_frame(self, cont): # cont = controller (unused)
        frame = self.frames[cont] # retrieves the frame with key "cont" from frames dictionary
        frame.tkraise() # Moves called frame to top

class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Login Page", font=LARGE_FONT)
        label.pack(padx=10, pady=10)
        #testing

# Application window
root.title("DQS - Learn")

# can change value of app to change screen??
app = dqsLearn(root)
root.mainloop()