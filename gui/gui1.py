from tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='hello you are the big SB!')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('gui.py')
root.mainloop()