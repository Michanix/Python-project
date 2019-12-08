# import only neccessary stuff
import os
from getpass import getuser  # to username that currently logged in
from subprocess import call

from tkinter import Tk
from tkinter import ttk, Listbox, Menu
from tkinter import filedialog, messagebox

# my imports
#from controllers import use_existing_image, unlock
from takepicture import TakePicture
from findandrecognize import find_and_recognize

# set of directories that already secured


def get_paths_from_dir():
    with open('paths.txt', 'r') as f:
        data = f.readlines()
    return data


def write_path_to_file(path):
    # writing paths to file
    path_to_save = os.path.join(os.getcwd(), 'paths.txt')
    with open(path_to_save, 'a+') as f:
        f.write(path + '\n')


def remove_paths(path):
    data = get_paths_from_dir()
    data = [i.strip('\n') for i in data]
    data.remove(path)
    with open('paths.txt', 'w+') as f:
        for p in data:
            f.write(p + '\n')


class UI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Folder security")
        self.path_to_image = []
        # Main window
        self.mainframe = ttk.Frame(
            self.root, padding="4 4 12 12", width=480, height=320)
        self.mainframe.pack()
        # menu bar
        menubar = Menu(self.root)
        menubar.add_command(label='Take picture', command=TakePicture)
        menubar.add_command(label='Use existing image',
                            command=self.use_existing_image)
        menubar.add_command(label='Exit', command=self.close_program)
        self.root.config(menu=menubar)
        # Labels
        self.folder_label = ttk.Label(
            self.mainframe, text='Choose folder:', font=16)
        self.listbox_label = ttk.Label(
            self.mainframe, text='List of secured folder:', font=16)
        # Entries
        self.folder_entry = ttk.Entry(
            self.mainframe, width=90, text='', background='white')
        # List box
        self.folders_listbox = Listbox(
            self.mainframe, width=90, background='white')
        self.data = get_paths_from_dir()
        for path in self.data:
            self.folders_listbox.insert(1, path.strip('\n'))
        # Buttons
        self.browse = ttk.Button(
            self.mainframe, text='Browse...', command=self.get_folder_path)
        self.lock_btn = ttk.Button(
            self.mainframe, text='Lock', command=self.lock_directory)
        self.unlock_btn = ttk.Button(
            self.mainframe, text='Unlock', command=self.unlock_dir)
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
        self.browse = filedialog.askdirectory(
            initialdir=user_desk, title='Select folder')
        self.folder_entry.delete(0, 'end')
        self.folder_entry.insert(0, self.browse)

    def is_secured(self):
        active = self.browse
        with open('paths.txt') as f:
            data = f.readlines()
        for path in data:
            if active in path:
                return True
        return False

    def lock_directory(self):
        active_path = self.browse
        if self.is_secured():
            messagebox.showinfo(message='Already secured')
        else:
            self.folders_listbox.insert(0, active_path)
            messagebox.showinfo(message='Folder is locked')
            # applying only read and execute permission
            # thus we can still see directory, but actions permitted
            call(['chmod', '-R', '101', active_path])
            write_path_to_file(active_path)

    def use_existing_image(self):
        path = os.getcwd
        image = filedialog.askopenfilename(
            initialdir=path, title="Select file",
            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        image_path = os.path.realpath(image)
        self.path_to_image.append(image_path)

    def apply_changes(self, active_item):
        # gives back full control of directory
        call(['chmod', '-R', '777', active_item])
        self.folders_listbox.delete('active')
        messagebox.showinfo(message='Access granted.')

    def unlock_dir(self):
        active_item = self.folders_listbox.get('active')
        if len(self.path_to_image) == 0:
            try:
                access = find_and_recognize()
            except FileNotFoundError as err:
                messagebox.showinfo(message=err)
            else:
                if access:
                    self.apply_changes(active_item)
                else:
                    messagebox.showinfo(message='Access denied.')
        else:
            try:
                access = find_and_recognize(self.path_to_image[0])
            except FileNotFoundError as err:
                messagebox.showinfo(message=err)
            else:
                if access:
                    self.apply_changes(active_item)
                else:
                    messagebox.showinfo(message='Access denied.')
        try:
            remove_paths(active_item)
        except:
            pass


if __name__ == '__main__':
    print('Start programm...')
    main = UI()
    main.root.mainloop()
