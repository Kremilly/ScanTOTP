#!/usr/bin/python3

from classes.flags import Flags
from classes.startup import Startup

flags = Flags.parser('E.g.: python scantotp -a qrcode -m file -i qrcode.png', [
    {'short': 'm', 'long': 'mode', 'help': 'Mode of scan', 'required': True},
    {'short': 'i', 'long': 'image', 'help': 'Location of image', 'required': False},
    {'short': 'a', 'long': 'action', 'help': 'Action of runing', 'default': 'qrcode', 'required': True},
])

if __name__ == '__main__':
    Startup(flags).run()
