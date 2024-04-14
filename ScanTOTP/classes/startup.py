#!/usr/bin/python3

from core.qrcode_detect import QRCodeDetect
from core.decode_secret_key import DecodeSecretKey

class Startup:
    
    @classmethod
    def __init__(cls, flags):
        cls.flags = flags
    
    @classmethod
    def run(cls):
        match cls.flags.action:
            case 'qrcode':
                QRCodeDetect.detect(cls.flags, True)
            case 'totp':
                DecodeSecretKey.decode(cls.flags)
            case _:
                print('Type is invalid')
