from tkinter import Toplevel, Text, Scrollbar

def get_text_from_file():
    with open('help.txt') as f:
        text = f.read()
    return text

class HelpPage:
    def __init__(self):
        root = Toplevel()
        root.title('Help')
        scroll = Scrollbar(root)
        mainframe = Text(root, width=100)
        scroll.pack(side='right', fill='y')
        mainframe.pack(side='left', fill='y')
        scroll.config(command=mainframe.yview)
        mainframe.config(yscroll=scroll.set)
        text = get_text_from_file()
        mainframe.insert('end', text)
        mainframe.pack()
