from tkinter import filedialog
from controllers import get_user_path

def upload_existing_picture():
    path = get_user_path()
    image = filedialog.askopenfilename(
        initialdir=path, title="Select file",
        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    return image

a = upload_existing_picture()
print(type(a))