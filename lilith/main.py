# -*- coding: utf-8 -*-
import sys

from lilith.work import get_qrcode_by_text

__author__ = 'derobukal'
__time__ = '2017/8/2 23:17'


def show():
    args = sys.argv
    if len(args) == 1:
        print('Hi, it\'s Lilith!\nYou can use command \'lilith $$$$\' '
              'to generating a qrcode with info of \'$$$$\'.\nFor example, '
              '\'lilith http://nosuchfield\' can create a '
              'qrcode with value of \'http://nosuchfield\'.\nMore '
              'info: https://github.com/RitterHou/Lilith')
    else:
        text = args[1]
        qrcode = get_qrcode_by_text(text)
        print(qrcode)


if __name__ == '__main__':
    show()
