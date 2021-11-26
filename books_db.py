from sqlite3 import *
def get():
    conn = connect('books.db')
    c = conn.cursor()
    