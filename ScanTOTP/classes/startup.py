#!/usr/bin/python3

import argparse

from core.qrcode_detect import QRCodeDetect
from core.decode_secret_key import DecodeSecretKey

class Startup:
    
    @classmethod
    def __init__(cls, desc, flags):
        cls.flags = cls.parser(desc, flags)
    
    @classmethod
    def parser(cls, desc, args):
        parser = argparse.ArgumentParser(description=desc)

        for arg in args:
            parser.add_argument(
                f"-{arg.pop('short', None)}", f"--{arg.pop('long', None)}", **arg
            )

        return parser.parse_args()
    
    @classmethod
    def run(cls):
        print('-' * 42)
        print(f'--> {cls.flags.input} <--')
        print('-' * 42)
        
        match cls.flags.action:
            case 'qrcode':
                QRCodeDetect.detect(cls.flags, True)
            case 'otp':
                DecodeSecretKey.decode(cls.flags)
            case _:
                print('Type is invalid')
