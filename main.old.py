
def add_result(result):
    global window
    window = Tk()
    room = Entry(window, font=('Malgun Gothic', 20, "roman"))
    b = Label(window, text="방", font=('Malgun Gothic', 20, "roman"))
    b.grid(row=0, column=49)
    room.grid(row=0, column=51)
    b = Label(window, text="방 내의 위치", font=('Malgun Gothic', 20, "roman"))
    place = Entry(window, font=('Malgun Gothic', 20, "roman"))
    b.grid(row=1, column=49)
    place.grid(row=1, column=51)
    b = Label(window, text="행", font=('Malgun Gothic', 20, "roman"))
    column = Entry(window, font=('Malgun Gothic', 20, "roman"))
    b.grid(row=2, column=49)
    column.grid(row=2, column=51)
    b = Label(window, text="열", font=('Malgun Gothic', 20, "roman"))
    row = Entry(window, font=('Malgun Gothic', 20, "roman"))
    b.grid(row=3, column=49)
    row.grid(row=3, column=51)

    def ading():
        start()
        data1 = room.get()
        data2 = row.get()
        data3 = column.get()
        data4 = place.get()
        return com(functions.add, isbn=result, row=data2, column=data3)

    frame = Frame(window)
    b = Button(frame, text="등록", font=('Malgun Gothic', 20, "roman"), command=ading)
    b.pack()
    frame.grid(row=4, column=50)
    window.mainloop()


def change():
    pass


def barcode():
    global window, root
    return add_result(com(scan.scan()))


def add():
    global root
    root.destroy()
    barcode()


def find_clicked():
    global entry, commands
    global window
    get = com(functions.find_from_csv, Entry.get(entry))
    window.destroy()
    window = Tk()
    found = {}

    def commandss(k):
        global found
        found = k

    for i in get:
        l = Button(window, text="제목:" + i['제목'], command=commandss(i), font=('Malgun Gothic', 20, "roman"))
        l.pack()
    window.destroy()
    window = Tk()
    label = Label(window, text="방:" + found['방'] + "\n장소:" + found['장소'] + "\n행:" + found['행'] + "\n열:" + found['열'],
                  font=('Malgun Gothic', 20, "roman"))
    label.pack()
    window.protocol("WM_DELETE_WINDOW", start)
    window.mainloop()


def find():
    global entry
    global window
    window = Tk()
    entry = Entry(window, font=('Malgun Gothic', 20, "roman"))
    entry.grid(row=0, column=0)
    b = Button(window, text="검색", command=find_clicked, font=('Malgun Gothic', 20, "roman"))
    b.grid(row=0, column=1)
    window.protocol("WM_DELETE_WINDOW", start)
    window.mainloop()
