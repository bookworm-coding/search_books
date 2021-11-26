from tkinter import *
from log import command as com
tk = None
value = ""


def scan():
    global tk, value
    value = ""
    tk = Tk()
    tk.title("바코드 스캔")
    def click(e):
        global value
        global tk
        if e.keysym == 'Return':
            return value
        else:
            value += e.keysym
    tk.bind("<Key>", click)
    tk.mainloop()
