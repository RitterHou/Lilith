from setuptools import setup

__author__ = 'derobukal'
__time__ = '2017/8/2 23:14'

setup(
    name='tqrcode',
    version='0.0.1',
    url='http://nosuchfield.com',
    author='derobukal',
    author_email='derobukal@gmail.com',
    description='show qrcode in terminal',
    license='GPL3',
    packages=['tqrcode'],
    entry_points={
        'console_scripts': [
            'tqrcode=tqrcode.main:show'
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: GPL3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'qrcode>=5.3',
    ],
)
