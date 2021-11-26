from tkinter import *
import scan
import functions
from log import command as com

root: Tk = None
window: Tk = None
entry = None
entry2 = None


def add():
    global window, entry
    window = Tk()
    entry = Entry(window, font=('Malgun Gothic', 20, "roman"))
    entry.grid(row=0, column=1)
    t2 = Label(window, text="ISBN을 입력하거나 스캔하세요", font=('Malgun Gothic', 20, "roman"))
    t2.grid(row=0, column=0)
    data1 = None
    data2 = None

    def next_com(*args):
        global entry, window, entry, t2
        data1 = entry.get()
        window.destroy()
        window = Tk()
        entry = Entry(window, font=('Malgun Gothic', 20, "roman"))
        entry.grid(row=0, column=1)
        t2 = Label(window, text="위치 코드를 입력하거나 스캔하세요", font=('Malgun Gothic', 20, "roman"))
        t2.grid(row=0, column=0)

        def next_com_com(*args):
            global window, data1, data2, t, entry
            data2 = entry.get()
            window.destroy()
            com(functions.add, isbn=data1, d=data2)

        window.bind("<Return>", next_com_com)

    window.bind("<Return>", next_com)


def start():
    global root, window, entry
    try:
        window.destroy()
    except:
        pass
    root = Tk()
    root.Title = "도서검색 프로그램"
    a = Button(root, text="신규 등록", command=add, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=1)
    a = Button(root, text="기존 책 뽑기", command=out, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=2)
    a = Button(root, text="기존 책 꼽기", command=into, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=3)
    a = Button(root, text="책 검색", command=find, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=4)
    root.mainloop()


if __name__ == "__main__":
    try:
        window.destroy()
    except:
        pass
    root = Tk()
    root.Title = "도서검색 프로그램"
    a = Button(root, text="신규 등록", command=add, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=1)
    a = Button(root, text="기존 책 뽑기"""", command=out""", font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=2)
    a = Button(root, text="기존 책 꼽기"""", command=into""", font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=3)
    a = Button(root, text="책 검색"""", command=find""", font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=4)
    root.mainloop()
