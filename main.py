# import only neccessary stuff
from tkinter import Frame, Label, Button, Tk
from tkinter import ttk
import time
# my imports
from controllers import get_user_path, take_picture, upload_existing_picture, unlock

start = time.time()
# Do I need class, tho ?
class Main:

    def __init__(self):
        self.root = Tk()
        self.root.title("Main programm")
        self.root.geometry('640x480')

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(self.mainframe).grid(column=2, row=2)
        take_pic_btn = ttk.Button(
            self.mainframe, text='Take picture', command=take_picture)
        take_pic_btn.grid(
            column=1, row=2, padx=10, pady=10)

        upload_image_btn = ttk.Button(
            self.mainframe, text='Upload existing picture', command=upload_existing_picture)
        upload_image_btn.grid(column=3, row=2)

        unlock_btn = ttk.Button(
            self.mainframe, text='Unlock', command=unlock)
        unlock_btn.grid(column=4, row=2, padx=10, pady=10)
    
print('Start programm...')
main = Main()
main.root.mainloop()
print('Terminated.')
print('second ', (time.time() - start))