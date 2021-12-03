from sqlite3 import *
from tkinter.messagebox import askyesno, showinfo

def get(column='*', where=''):
    conn = connect('books.db')
    c = conn.cursor()
    if where == '':
        c.execute('SELECT ' + column + ' FROM books')
    else:
        c.execute('SELECT ' + column + ' FROM books WHERE ' + where)
    a = c.fetchall()
    conn.close()
    return a


def insert(isbn, place, title):
    conn = connect('books.db')
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (:isbn, :place, :title)",
              {"isbn": isbn, "place": place, "title": title})

    conn.commit()
    conn.close()
    return
def reset():
    if askyesno("도서 목록 초기화", "도서 목록 초기화 하시겠습니까?"):
        showinfo("도서 목록 초기화 완료", "도서 목록 초기화 완료됨")
        conn = connect('books.db')
        c = conn.cursor()
        c.execute('DROP TABLE "books"')
        c.execute('CREATE TABLE "books" ("isbn" TEXT NOT NULL,"place" TEXT NOT NULL, "title" TEXT NOT NULL)')
        conn.commit()
        conn.close()
    else:
        pass
    return

if __name__ == "__main__":
    print(get())
