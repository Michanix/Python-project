from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

# my imports
from takepicture import TakePicture
from findandrecognize import find_and_recognize


class Main:

    def __init__(self):
        self.root = Tk()
        self.root.title("Main programm")
        self.root.geometry('640x480')

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(self.mainframe).grid(column=2, row=2, sticky=(W, E))
        take_pic_btn = ttk.Button(
            self.mainframe, text='Take picture', command=self.take_picture)
        take_pic_btn.grid(
            column=1, row=2, padx=10, pady=10)

        upload_image_btn = ttk.Button(
            self.mainframe, text='Upload picture', command=self.upload_picture)
        upload_image_btn.grid(column=3, row=2)

        unlock_btn = ttk.Button(
            self.mainframe, text='Unlock', command=self.unlock)
        unlock_btn.grid(column=4, row=2, padx=10, pady=10)

    def upload_picture(self):
        path = os.getcwd
        image = filedialog.askopenfilename(
            initialdir=path, title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    def take_picture(self):
        return TakePicture()

    def unlock(self):
        unlock = find_and_recognize()
        if unlock:
            messagebox.showinfo(message='Access granted.')
        else:
            messagebox.showinfo(message='Access denied.')


print('Start programm...')
main = Main()
main.root.mainloop()
print('Terminated.')
