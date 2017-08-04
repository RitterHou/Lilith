# -*- coding: utf-8 -*-
import qrcode
import sys

__author__ = 'derobukal'
__time__ = '2017/8/2 23:31'

STEP = 10  # 步长


def get_qrcode_by_text(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=STEP,
        border=0,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    return get_ascii(img)


def get_ascii(image):
    string = ''
    image = image.convert('L')  # 转为灰白模式
    width, height = image.size

    pix = image.load()
    for i in range(0, width, STEP):
        for j in range(0, height, STEP):
            p = pix[i, j]
            p = '██' if p > 0 else '  '
            string += p
        string += '\n'
    return string


if __name__ == '__main__':
    text = get_qrcode_by_text('http://nosuchfield.com')
    sys.stdout.write(text)
