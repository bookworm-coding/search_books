from tkinter import *
from tkinter.messagebox import showinfo
import books_db
import functions
import open_api
import make_barcode
from os import system

root: Tk = None
window: Tk = None
entry: Entry = None
entry2: Entry = None
button: Button = None
data1: str = ""
data2: str = ""


def reset():
    global root, window, entry, entry2, data1, data2, button

    def end():
        global root, window, entry, entry2, data1, data2, button
        make_barcode.make(int(entry.get()), int(entry2.get()))
        showinfo('초기 세팅 완료', '다음 창에 뜨는 이미지를 출력하여 잘라서 책장의 칸마다 붙이세요.')
        system('print.png')
        window.destroy()

    window = Tk()
    window.title('초기 설정하기')
    l = Label(window, text="책장의 가로와 세로를 입력하세요", font=('Malgun Gothic', 20, "roman"))
    l.pack()
    frame1 = Frame(window)
    frame1.pack()
    frame2 = Frame(window)
    frame2.pack()
    l = Label(frame1, text="가로:", font=('Malgun Gothic', 20, "roman"))
    l.grid(row=0, column=0)
    entry = Entry(frame1, font=('Malgun Gothic', 20, "roman"))
    entry.grid(row=0, column=1)
    l = Label(frame2, text="세로:", font=('Malgun Gothic', 20, "roman"))
    l.grid(row=0, column=0)
    entry2 = Entry(frame2, font=('Malgun Gothic', 20, "roman"))
    entry2.grid(row=0, column=1)
    button = Button(window, text="완료", command=end, font=('Malgun Gothic', 20, "roman"))
    button.pack()
    window.mainloop()


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
            text = ""
            for i in search:
                text += str(i[2]) + "라는 책이 " + str(i[1]) + "에 있습니다.\n"
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
        global entry, window, entry, t2, entry2, data1, data2
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
            functions.add_db(isbn=data1, place=data2)
            showinfo(open_api.isbn(data1) + "도서 등록 완료", open_api.isbn(data1) + " 도서 등록이 완료되었습니다.")
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
    a = Label(root, text="도서검색 프로그램 v1.0", font=('Malgun Gothic', 20, "roman"), width=20)
    a.pack(side="top")
    frame = Frame(root)
    frame.pack(side="bottom")
    a = Button(frame, text="신규 등록", command=add, font=('Malgun Gothic', 20, "roman"), width=10)
    a.grid(row=0, column=0)
    # a = Button(root, text="기존 책 뽑기"""", command=out""", font=('Malgun Gothic', 20, "roman"))
    # a.grid(row=0, column=2)
    # a = Button(root, text="기존 책 꼽기"""", command=into""", font=('Malgun Gothic', 20, "roman"))
    # a.grid(row=0, column=3)
    a = Button(frame, text="책 검색", command=find, font=('Malgun Gothic', 20, "roman"), width=10)
    a.grid(row=0, column=1)
    a = Button(frame, text="도서 목록 초기화", command=books_db.reset, font=('Malgun Gothic', 20, "roman"))
    a.grid(row=0, column=2)
    # a=Button(frame, text="초기 설정 하기", command=reset, font=('Malgun Gothic', 20, "roman"))
    # a.grid(row=0, column=3)
    root.mainloop()
