from sqlite3 import *


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


if __name__ == "__main__":
    print(get())
