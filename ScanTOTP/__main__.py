#!/usr/bin/python3

from classes.flags import Flags

from core.qrcode_detect import QRCodeDetect

flags = Flags.parser('E.g.: python scantotp -m file -i ./qrcode.png', [
    {'short': 'm', 'long': 'mode', 'help': 'Mode of scan', 'required': True},
    {'short': 'i', 'long': 'image', 'help': 'Location of image', 'required': False},
    {'short': 't', 'long': 'type', 'help': 'Type of use', 'default': 'totp', 'required': False},
])

if __name__ == '__main__':
    print(QRCodeDetect.detect(flags))
    pass
