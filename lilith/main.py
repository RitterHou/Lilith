# -*- coding: utf-8 -*-
import sys

from lilith.work import get_qrcode_by_text

__author__ = 'derobukal'
__time__ = '2017/8/2 23:17'

alert = 'Hi, it\'s Lilith!\nYou can use command \'lilith text\' ' \
        'to generating a qrcode with info of \'text\'.\nMore ' \
        'info: https://github.com/RitterHou/Lilith'


def show():
    args = sys.argv
    if len(args) == 1:
        print(alert)
    elif len(args) == 2:
        text = args[1]
        qrcode = get_qrcode_by_text(text)
        print(qrcode)


if __name__ == '__main__':
    show()
