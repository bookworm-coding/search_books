from sqlite3 import *
def get(column='*', where=''):
    conn = connect('books.db')
    c = conn.cursor()
    if where=='':
        c.execute('SELECT ' + column + ' FROM books')
    else:
        c.execute('SELECT ' + column + ' FROM books WHERE ' + where)
    a=c.fetchall()
    conn.close()
    return a
def insert(isbn, place, title):
