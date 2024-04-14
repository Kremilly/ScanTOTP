#!/usr/bin/python3

import pyotp, pyperclip

from helper.regex import Regex

from classes.settings import Settings

from core.qrcode_detect import QRCodeDetect

class DecodeSecretKey:
    
    @classmethod
    def decode(cls, flags):
        copied = False
        qrcode_data = QRCodeDetect.detect(flags)
        
        if qrcode_data != None:
            issuer = Regex.get(qrcode_data, r'issuer=([\w]+)')
            secret_key = Regex.get(qrcode_data, r'secret=([A-Z2-7]+)')
            
            otp = pyotp.TOTP(secret_key).now()
            
            if Settings.get('general.auto_copy_code', 'boolean') or flags.copy:
                pyperclip.copy(otp)
                copied = True
            
            if Settings.get('advanced.hide_otp_code', 'boolean') or flags.hide_key:
                otp = str('*' * len(otp))
            
            print('Issuer:', issuer)
            print('Current OTP Code:', otp)

            if copied is True:
                print(' |-> Code OTP copied')
            
            return True

        print('QR Code invalid')
