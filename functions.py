import open_api
import books_db


def search_db(query):
    result: list = []
    data = books_db.get()
    for i in data:
        if query in i[2]:
            result.append(i)
    return result


def add_db(isbn='', place=''):
    books_db.insert(isbn, place, open_api.isbn(isbn))


def show(isbn=0):
    if isbn != 0:
        return open_api.isbn(isbn)


def change(dictionary):
    return dictionary["TITLE"]
