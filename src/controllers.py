import os
from tkinter import filedialog, messagebox

from findandrecognize import find_and_recognize

path_to_image = []

def use_existing_image():
    path = os.getcwd
    image = filedialog.askopenfilename(
        initialdir=path, title="Select file",
        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    image_path = os.path.realpath(image)
    path_to_image.append(str(image_path))

def unlock():
    if len(path_to_image) == 0:
        try:
            access = find_and_recognize()
        except FileNotFoundError as err:
            messagebox.showinfo(message=err)
        else:
            if access:
                messagebox.showinfo(message='Access granted.')
            else:
                messagebox.showinfo(message='Access denied.')
    else:
        try:
            access = find_and_recognize(path_to_image[0])
        except FileNotFoundError as err:
            messagebox.showinfo(message=err)
        else:
            if access:
                messagebox.showinfo(message='Access granted.')
            else:
                messagebox.showinfo(message='Access denied.')