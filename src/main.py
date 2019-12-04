# import only neccessary stuff
from tkinter import Tk
from tkinter import ttk
import time
# my imports
from controllers import take_picture, upload_existing_picture, unlock

start = time.time()
class Main:

    def __init__(self):
        self.root = Tk()
        self.root.title("Main programm")
        self.root.geometry('480x300')

        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Label(self.mainframe).grid(column=2, row=2)
        # button to take picture
        # call method take_picture from takepicture.py
        take_pic_btn = ttk.Button(
            self.mainframe, text='Take picture', command=take_picture)
        take_pic_btn.grid(
            column=1, row=2, padx=10, pady=10)
        # upload an image button
        # call method upload_existing_picture from controllers.py
        upload_image_btn = ttk.Button(
            self.mainframe, text='Upload existing picture', command=upload_existing_picture)
        upload_image_btn.grid(column=3, row=2)
        # button to test, if image is satisfy
        # call unlock method from controllers.py
        test_btn = ttk.Button(
            self.mainframe, text='Test', command=unlock)
        test_btn.grid(column=4, row=2, padx=10, pady=10)
        # exit button
        exit_btn = ttk.Button(
            self.mainframe, text='Exit', command=self.close_program)
        exit_btn.grid(column=5, row=2)

    def close_program(self):
        self.root.destroy()

print('Start programm...')
main = Main()
main.root.mainloop()
print('Terminated.')
print('second\n', (time.time() - start))