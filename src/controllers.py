import os
from getpass import getuser
from tkinter import filedialog, messagebox

from findandrecognize import find_and_recognize
from takepicture import TakePicture


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
    return image_path


def take_picture():
    return TakePicture()


def unlock():
    try:
        access = find_and_recognize()
    except:
        print('Something went wrong.')
    else:
        if access:
            messagebox.showinfo(message='Access granted.')
        else:
            messagebox.showinfo(message='Access denied.')
