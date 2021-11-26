import cv2
from barcode import Code128
from barcode.writer import ImageWriter
from log import LibraryError
from os import remove
from log import command as com


def make(h, w):
    if w > 26:
        raise LibraryError('책장의 가로의 길이가 너무 깁니다.')
    if h > 9:
        raise LibraryError('책장의 세로의 길이가 너무 깁니다. 가로와 세로를 바꾸어서 입력해 보세요.')
    l = []
    for i in range(65, 65 + w):
        for j in range(1, h + 1):
            with open(chr(i) + str(j) + '.png', 'wb') as f:
                Code128(chr(i) + str(j), writer=ImageWriter()).write(f)
            l.append(cv2.rectangle(cv2.imread(chr(i) + str(j) + '.png'), (0, 0), (194, 280), (0, 0, 0), 3))
            remove(chr(i) + str(j) + '.png')
    print(l)
    if len(l) > 144:
        raise LibraryError('이렇게 많은 칸의 책장을 아직은 지원하지 않습니다. 차후 지원 예정입니다.')
    elif len(l) > 12:
        i = 0
        while (i * 12 + 12) <= len(l):
            cv2.imwrite('file' + str(i) + '.png', cv2.hconcat(l[i * 12:i * 12 + 12]))
            i += 1
        lis = []
        for j in range(0, i):
            lis.append(cv2.imread('file' + str(j) + '.png'))
            remove('file' + str(j) + '.png')
        print(len(lis))
        for i in range(0, len(lis)):
            lis[i] = cv2.resize(lis[i], (2328, 280))
        result = cv2.vconcat(lis)
    else:
        result = cv2.hconcat(tuple(l))
    cv2.imwrite('print.png', result)


if __name__ == "__main__":
    make(int(input('h')), int(input('w')))
