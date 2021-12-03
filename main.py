from tkinter import *
from tkinter.messagebox import showinfo
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
    window = Tk()
    entry = Entry(window, font=('Malgun Gothic', 20, "roman"))
    entry.grid(row=0, column=1)
    l = Label(window, text="찾으려는 책의 제목을 입력하세요.", font=('Malgun Gothic', 20, "roman"))
    l.grid(row=0, column=0)
    window.title('도서 검색')
    def next_com(*args, **kwargs):
        global window
        data = entry.get()
        window.destroy()
        search: list = functions.search_db(data)
        print(search)
        if search == [] or search == None:
            showinfo("존재하지 않는 책", "찾으시려는 책이 없습니다.")
        else:
            text=""
            for i in search:
               text+=str(i[2]) + "라는 책이 " + str(i[1]) + "에 있습니다.\n"
            showinfo("책 찾음", text)

    window.bind("<Return>", next_com)
    window.mainloop()


def add():
    global window, entry
    window = Tk()
    window.title("ISBN 입력")
    entry = Entry(window, font=('Malgun Gothic', 20, "roman"))
    entry.grid(row=0, column=1)
    t2 = Label(window, text="ISBN을 입력하거나 스캔하세요", font=('Malgun Gothic', 20, "roman"))
    t2.grid(row=0, column=0)
    data1 = None
    data2 = None

    def next_com(*args):
        global entry, window, entry, t2, entry2
        data1 = entry.get()
        window.destroy()
        window = Tk()
        window.title("위치 코드 입력")
        entry2 = Entry(window, font=('Malgun Gothic', 20, "roman"))
        entry2.grid(row=0, column=1)
        t2 = Label(window, text="위치 코드를 입력하거나 스캔하세요", font=('Malgun Gothic', 20, "roman"))
        t2.grid(row=0, column=0)
        def next_com_com(*args):
            global window, data1, data2, t, entry
            data2 = entry2.get()
            functions.add_db(isbn=entry.get(), place=entry2.get())
            showinfo("도서 등록 완료", "신규 도서 등록이 완료되었습니다.")
            window.destroy()

        window.bind("<Return>", next_com_com)
        window.mainloop()
    window.bind("<Return>", next_com)
    window.mainloop()


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
    # a = Button(root, text="기존 책 뽑기", command=out, font=('Malgun Gothic', 20, "roman"))
    # a.grid(row=0, column=2)
    # a = Button(root, text="기존 책 꼽기", command=into, font=('Malgun Gothic', 20, "roman"))
    # a.grid(row=0, column=3)
    a = Button(root, text="책 검색", command=find, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=4)
    root.mainloop()


if __name__ == "__main__":
    try:
        window.destroy()
    except:
        pass
    root = Tk()
    root.title("도서 검색 프로그램")
    a = Button(root, text="신규 등록", command=add, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=1)
    # a = Button(root, text="기존 책 뽑기"""", command=out""", font=('Malgun Gothic', 20, "roman"))
    # a.grid(row=0, column=2)
    # a = Button(root, text="기존 책 꼽기"""", command=into""", font=('Malgun Gothic', 20, "roman"))
    # a.grid(row=0, column=3)
    a = Button(root, text="책 검색", command=find, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=4)
    root.mainloop()
