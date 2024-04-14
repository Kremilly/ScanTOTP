#!/usr/bin/python3

import argparse

from core.qrcode_detect import QRCodeDetect
from core.decode_secret_key import DecodeSecretKey

class Startup:
    
    @classmethod
    def __init__(cls, desc, flags):
        cls.flags = cls.parser(desc, flags)
    
    @classmethod
    def parser(cls, desc, arguments):
        parser = argparse.ArgumentParser(description=desc)

        for arg in arguments:
            parser.add_argument(
                f"-{arg.pop('short', None)}", f"--{arg.pop('long', None)}", **arg
            )

        return parser.parse_args()
    
    @classmethod
    def run(cls):
        match cls.flags.action:
            case 'qrcode':
                QRCodeDetect.detect(cls.flags, True)
            case 'totp':
                DecodeSecretKey.decode(cls.flags)
            case _:
                print('Type is invalid')
