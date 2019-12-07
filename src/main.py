import os
# import only neccessary stuff
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog

# my imports
from controllers import use_existing_image, unlock
from takepicture import TakePicture

class UI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Main programm")
        self.root.geometry('480x300')

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        label = ttk.Label(self.mainframe, text='Choose folder:')
        label.grid(column=1, row=1)
        self.folder = ttk.Entry(self.mainframe, text='')
        self.folder.grid(column=2, row=1)
        self.browse = ttk.Button(
            self.mainframe, text='Browse...', command=self.get_folder)
        self.browse.grid(column=3, row=1, padx=10, pady=10)
        # upload an image button
        # call method upload_existing_picture from controllers.py
        upload_image_btn = ttk.Button(
            self.mainframe, text='Use existing image', command=use_existing_image)
        upload_image_btn.grid(column=1, row=2)
        # button to take picture
        # call method take_picture from takepicture.py
        take_pic_btn = ttk.Button(
            self.mainframe, text='Take picture', command=TakePicture)
        take_pic_btn.grid(
            column=1, row=3, padx=10, pady=10)
        # button to test, if image is satisfy
        # call unlock method from controllers.py
        test_btn = ttk.Button(
            self.mainframe, text='Test', command=unlock)
        test_btn.grid(column=1, row=4)
        # exit button
        exit_btn = ttk.Button(
            self.mainframe, text='Exit', command=self.close_program)
        exit_btn.grid(column=1, row=5, padx=10, pady=10)

    def close_program(self):
        self.root.destroy()
        print('Terminated.')
    
    def get_folder(self):
        self.browse = filedialog.askdirectory(title='Select folder')
        self.folder.delete(0, 'end')
        self.folder.insert(0, self.browse)

print('Start programm...')
main = UI()
main.root.mainloop()
