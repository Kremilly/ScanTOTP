#!/usr/bin/python3

from classes.flags import Flags

flags = Flags.parser('E.g.: python scantotp -m screen', [
    {'short': 'm', 'long': 'mode', 'help': 'Mode of scan', 'required': True},
])

if __name__ == '__main__':
    pass
