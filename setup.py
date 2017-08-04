# -*- coding: utf-8 -*-
from setuptools import setup

__author__ = 'derobukal'
__time__ = '2017/8/2 23:14'

setup(
    name='lilith',
    version='0.0.1',
    url='https://github.com/RitterHou/Lilith',
    author='derobukal',
    author_email='derobukal@gmail.com',
    description='show qrcode in terminal',
    license='GPL3',
    packages=['lilith'],
    entry_points={
        'console_scripts': [
            'lilith=lilith.main:show'
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'olefile==0.44',
        'Pillow==4.2.1',
        'qrcode==5.3',
        'six==1.10.0'

    ],
)
