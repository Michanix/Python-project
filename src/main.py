from getpass import getuser
# import only neccessary stuff
from tkinter import Tk
from tkinter import ttk, Listbox
from tkinter import filedialog

# my imports
from controllers import use_existing_image, unlock
from takepicture import TakePicture


class UI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Folder security")

        # Main window
        self.mainframe = ttk.Frame(
            self.root, padding="4 4 12 12", width=480, height=320)
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Labels
        self.folder_label = ttk.Label(self.mainframe, text='Choose folder:')
        self.test_label = ttk.Label(self.mainframe, text='Test your image before applying changes')
        self.listbox_label = ttk.Label(self.mainframe, text='List of secured folder')
        # Entries
        self.folder_entry = ttk.Entry(self.mainframe, width=90, text='')
        # List box
        self.folders_listbox = Listbox(self.mainframe, width=90)

        # Buttons
        self.browse = ttk.Button(
            self.mainframe, text='Browse...', command=self.get_folder_path)
        # upload an image button
        # call method upload_existing_picture from controllers.py
        self.upload_image_btn = ttk.Button(
            self.mainframe, text='Use existing image', command=use_existing_image)
        # button to take picture
        # call method take_picture from takepicture.py
        self.take_pic_btn = ttk.Button(
            self.mainframe, text='Take picture', command=TakePicture)
        # button to test, if image is satisfy
        # call unlock method from controllers.py
        self.test_btn = ttk.Button(
            self.mainframe, text='Test', command=unlock)
        # exit button
        self.exit_btn = ttk.Button(
            self.mainframe, text='Exit', command=self.close_program)
        # delete item from list box
        self.delete_item = ttk.Button(self.mainframe, text='Remove', 
            command=lambda folders_listbox=self.folders_listbox: folders_listbox.delete(0)
            )
        self.lock_btn = ttk.Button(self.mainframe, text='Lock',
            command=lambda folders_listbox=self.folders_listbox: folders_listbox.insert(1, self.browse)
            )
        # Grigds
        # folder grid
        self.folder_label.grid(column=1, row=1)
        self.folder_entry.grid(column=2, row=1)
        # browser button grid
        self.browse.grid(column=3, row=1, padx=10, pady=10)
        # use existing image grid
        self.upload_image_btn.grid(column=1, row=3)
        # take picture grid
        self.take_pic_btn.grid(column=1, row=3, padx=10, pady=10)
        # test button grid
        self.test_btn.grid(column=1, row=4)
        # lock button grid
        self.lock_btn.grid(column=2, row=2)
        # exit button
        self.exit_btn.grid(column=1, row=5, padx=10, pady=10)
        # list box grid
        self.listbox_label.grid(column=1, row=2)
        self.folders_listbox.grid(column=2, row=3)
        self.delete_item.grid(column=2, row=4)
        
    def close_program(self):
        self.root.destroy()
        print('Terminated.')

    def get_folder_path(self):
        user_desk = '/home/{}/Desktop'.format(getuser())
        self.browse = filedialog.askdirectory(
            initialdir=user_desk, title='Select folder')
        self.folder_entry.delete(0, 'end')
        self.folder_entry.insert(0, self.browse)

print('Start programm...')
main = UI()
main.root.mainloop()
