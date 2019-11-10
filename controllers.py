from getpass import getuser
from tkinter import messagebox, filedialog
from takepicture import TakePicture
from findandrecognize import find_and_recognize


def get_user_path():
    username = getuser()
    path = '/home/{}/Desktop'.format(username)
    return path


def upload_existing_picture():
    path = get_user_path()
    image = filedialog.askopenfilename(
        initialdir=path, title="Select file",
        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    return image


def take_picture():
    return TakePicture()


def unlock():
    path_to_exist_image = upload_existing_picture
    try:
        access = find_and_recognize()
    except:
        print('Something went wrong...')
    else:
        if access:
            messagebox.showinfo(message='Access granted.')
        else:
            messagebox.showinfo(message='Access denied.')
