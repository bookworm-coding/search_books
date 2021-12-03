import open_api
import books_csv
import urllib.request
from log import LibraryError, LibraryMessage
from log import command as com
import books_db

def search_db(query):
    result:list=[]
    data=books_db.get()
    for i in data:
        if query in i[2]:
            result.append(i)
    return result
def search_csv(query):
    result = []
    a = 0
    for i in com(books_csv.get_from_csv):
        for j in dict.keys(i):
            if query in i[j]:
                result.append(a)
        a += 1
    if not result:
        raise LibraryMessage('없는 책 입니다.')
    return result


def add_db(isbn='', place=''):
    com(books_db.insert, isbn, place, open_api.isbn(isbn))


def add_csv(isbn='', d=''):
    data = com(open_api.isbn, isbn)
    data['위치'] = d
    com(books_csv.add_to_csv, data)
    return data


def delete_csv(query):
    com(books_csv.delete_to_csv, com(search_csv(query)))
    return


def show(isbn=0):
    if isbn != 0:
        return com(open_api.isbn, isbn)
    else:
        raise LibraryError('ISBN 값이 없습니다.')


def find_from_csv(query):
    get = com(books_csv.get_from_csv)
    num = com(search, query)
    result = []
    for i in num:
        result.append(get[i])
    return result


def change(dictionary):
    """
    change_value = {"TITLE": "제목", "VOL": "권차", "SERIES_TITLE": "시리즈명", "AUTHOR": "저자", "EA_ISBN": "ISBN",
                    "EA_ADD_CODE": "ISBN 부가기호", "SET_ISBN": "세트 ISBN", "SET_ADD_CODE": "세트 ISBN 부가기호",
                    "SET_EXPRESSION": "세트 표현", "PUBLISHER": "출판사", "EDITION_STMT": "판사항", "REAL_PRICE": "정가",
                    "KDC": "한국십진분류", "DDC": "듀이십진분류", "PAGE": "페이지수", "BOOK_SIZE": "책크기", "FORM": "발행제본형태",
                    "REAL_PUBLISH_DATE": "출판일", "SUBJECT": "주제", "EBOOK_YN": "전자책여부", "CIP_YN": "CIP 신청 여부",
                    "CONTROL_NO": "CIP 제어번호", "TITLE_URL": "표지이미지 URL", "BOOK_TB_CNT_URL": "목차",
                    "BOOK_INTRODUCTION_URL": "책소개", "BOOK_SUMMARY_URL": "책요약", "PUBLISHER_URL": "출판사 홈페이지 URL",
                    "INPUT_DATE": "등록날짜", "UPDATE_DATE": "수정날짜", "SERIES_NO": "총서편차", "PUBLISH_PREDATE": "출판 예정일",
                    "FORM_DETAIL": "제본 형태", "BIB_YN": "BIB 여부", "PRE_PRICE": "예상 가격", "DEPOSIT_YN": "DEPOSIT 여부",
                    "RELATED_ISBN": "관계 ISBN"}
    for i, j in list(dictionary.items()):
        if "_URL" in i and j != '' and i != "TITLE_URL" and i != "PUBLISHER_URL":
            k = urllib.request.urlopen(urllib.request.Request(j)).read().decode('ANSI')
            j = k
        dictionary[change_value[i]] = j
        del dictionary[i]
    """
    return dictionary["TITLE"]
