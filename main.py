from tkinter import *

import log
import scan
import functions
from log import command as com
root: Tk = None
window: Tk = None
entry: Entry = None
entry2: Entry = None
def find():
    global window, root, entry, entry2
    window=Tk()
    entry=Entry(window, font=('Malgun Gothic', 20, "roman"))
    entry.grid(row=0, column=1)
    l=Label(window, text="찾으려는 책의 제목을 입력하세요.")
    l.grid(row=0, column=0)
    def next_com(*args, **kwargs):
        global window
        data=entry.get()
        window.destroy()
        search:list=functions.search_db(data)
        if search == [] or search==None:
            window=Tk()
            l=Label(window, text="찾으려는 책이 없습니다.")
            l.pack()
            window.mainloop()
        else:
            window=Tk()

            for i, j in search, range(0, len(search)):
                l=Label(window, text=i[2]+"라는 책이 "+i[1]+"에 있습니다.\n")
                l.pack()
            window.mainloop()
    window.bind("<Return>", next_com)

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
        global entry, window, entry, t2, entry2
        data1 = entry.get()
        window = Tk()
        entry2 = Entry(window, font=('Malgun Gothic', 20, "roman"))
        entry2.grid(row=0, column=1)
        t2 = Label(window, text="위치 코드를 입력하거나 스캔하세요", font=('Malgun Gothic', 20, "roman"))
        t2.grid(row=0, column=0)

        def next_com_com(*args):
            global window, data1, data2, t, entry
            data2 = entry2.get()
            com(functions.add_db, isbn=entry.get(), d=entry2.get())
            window.destroy()

        window.bind("<Return>", next_com_com)

    window.bind("<Return>", next_com)


def start():
    global root, window, entry, a
    try:
        window.destroy()
    except:
        pass
    root = Tk()
    root.Title = "도서검색 프로그램"
    a = Button(root, text="신규 등록", command=add, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=1)
    #a = Button(root, text="기존 책 뽑기", command=out, font=('Malgun Gothic', 20, "roman"))
    #a.grid(row=0, column=2)
    #a = Button(root, text="기존 책 꼽기", command=into, font=('Malgun Gothic', 20, "roman"))
    #a.grid(row=0, column=3)
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
    #a = Button(root, text="기존 책 뽑기"""", command=out""", font=('Malgun Gothic', 20, "roman"))
    #a.grid(row=0, column=2)
    #a = Button(root, text="기존 책 꼽기"""", command=into""", font=('Malgun Gothic', 20, "roman"))
    #a.grid(row=0, column=3)
    a = Button(root, text="책 검색", command=find, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=4)
    root.mainloop()
