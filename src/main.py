# import only neccessary stuff
import os
from getpass import getuser # to username that currently logged in
from subprocess import call

from tkinter import Tk
from tkinter import ttk, Listbox, Menu
from tkinter import filedialog, messagebox

# my imports
#from controllers import use_existing_image, unlock
from takepicture import TakePicture
from findandrecognize import find_and_recognize

# set of directories that already secured
set_of_paths = set()

class UI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Folder security")
        self.path_to_image = []

        # Main window
        self.mainframe = ttk.Frame(
            self.root, padding="4 4 12 12", width=480, height=320)
        self.mainframe.grid(column=0, row=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        # menu bar
        menubar = Menu(self.root)
        menubar.add_command(label='Take picture', command=TakePicture)
        menubar.add_command(label='Use existing image', command=self.use_existing_image)
        menubar.add_command(label='Exit', command=self.close_program)
        self.root.config(menu=menubar)
        # Labels
        self.folder_label = ttk.Label(self.mainframe, text='Choose folder:', font=16)
        self.listbox_label = ttk.Label(self.mainframe, text='List of secured folder:', font=16)
        # Entries
        self.folder_entry = ttk.Entry(self.mainframe, width=90, text='')
        # List box
        self.folders_listbox = Listbox(self.mainframe, width=90)

        # Buttons
        self.browse = ttk.Button(self.mainframe, text='Browse...', command=self.get_folder_path)
        self.lock_btn = ttk.Button(self.mainframe, text='Lock', command=self.lock_directory)
        self.unlock_btn = ttk.Button(self.mainframe, text='Unlock', command=self.unlock_dir)
        # Grigds
        # folder grid
        self.folder_label.grid(column=1, row=1)
        self.folder_entry.grid(column=2, row=1)
        # browser button grid
        self.browse.grid(column=3, row=1, padx=10, pady=10)
        # lock button grid
        self.lock_btn.grid(column=3, row=2)
        # unlock
        self.unlock_btn.grid(column=3, row=3)
        # list box grid
        self.listbox_label.grid(column=1, row=2)
        self.folders_listbox.grid(column=2, row=3)
        
    def close_program(self):
        self.root.destroy()
        print('Terminated.')

    def get_folder_path(self):
        user_desk = '/home/{}/Desktop'.format(getuser())
        self.browse = filedialog.askdirectory(initialdir=user_desk, title='Select folder')
        self.folder_entry.delete(0, 'end')
        self.folder_entry.insert(0, self.browse)

    def lock_directory(self):
        if self.browse in set_of_paths:
            messagebox.showinfo(message='Already in list')
        else:
            self.folders_listbox.insert(1, self.browse)
            messagebox.showinfo(message='Folder is locked')
            call(['chmod', '-R', '101', self.folders_listbox.get('active')])
            set_of_paths.add(self.browse)

    def use_existing_image(self):
        path = os.getcwd
        image = filedialog.askopenfilename(
            initialdir=path, title="Select file",
            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        image_path = os.path.realpath(image)
        self.path_to_image.append(image_path)

    def unlock_dir(self):
        if len(self.path_to_image) == 0:
            try:
                access = find_and_recognize()
            except FileNotFoundError as err:
                messagebox.showinfo(message=err)
            else:
                if access:
                    call(['chmod', '-R', '777', self.folders_listbox.get('active')])
                    self.folders_listbox.delete(0)
                    set_of_paths.discard(self.browse)
                    messagebox.showinfo(message='Access granted.')
                else:
                    messagebox.showinfo(message='Access denied.')
        else:
            try:
                access = find_and_recognize(self.path_to_image[0])
            except FileNotFoundError as err:
                messagebox.showinfo(message=err)
            else:
                if access:
                    call(['chmod', '-R', '777', self.folders_listbox.get('active')])
                    self.folders_listbox.delete(0)
                    set_of_paths.discard(self.browse)
                    messagebox.showinfo(message='Access granted.')
                else:
                    messagebox.showinfo(message='Access denied.')

print('Start programm...')
main = UI()
main.root.mainloop()
