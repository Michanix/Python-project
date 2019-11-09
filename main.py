from tkinter import *
from tkinter import ttk, filedialog
import os

# my imports
from takepicture import TakePicture

class Main():
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Main programm")
        self.root.geometry('640x480')

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(self.mainframe).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(self.mainframe, text='Take picture', command=self.take_picture).grid(
            column=1, row=2, padx=10, pady=10)
        ttk.Button(self.mainframe, text='Upload picture', command=self.upload_picture).grid(column=3, row=2)

    def upload_picture(self):
        path = os.getcwd
        image = filedialog.askopenfilename(
            initialdir=path, title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    def take_picture(self):
        image = TakePicture()
        image.take_snapshot()

main = Main()
main.root.mainloop()
