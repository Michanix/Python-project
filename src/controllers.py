import os
from getpass import getuser
from tkinter import filedialog, messagebox

from findandrecognize import find_and_recognize
from takepicture import TakePicture

path_to_image = []

def get_user_path():
    username = getuser()
    path = '/home/{}/Desktop'.format(username)
    return path


def upload_existing_picture():
    path = get_user_path()
    image = filedialog.askopenfilename(
        initialdir=path, title="Select file",
        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    image_path = os.path.realpath(image)
    path_to_image.append(str(image_path))

def take_picture():
    return TakePicture()


def unlock():
    if len(path_to_image) == 0:
        try:
            access = find_and_recognize()
        except:
            print('Something went wrong.')
        else:
            if access:
                messagebox.showinfo(message='Access granted.')
            else:
                messagebox.showinfo(message='Access denied.')
    else:
        try:
            access = find_and_recognize(path_to_image[0])
        except:
            print('Something went wrong 2.')
        else:
            if access:
                messagebox.showinfo(message='Access granted.')
            else:
                messagebox.showinfo(message='Access denied.')