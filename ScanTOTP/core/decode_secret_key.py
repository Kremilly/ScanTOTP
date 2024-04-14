#!/usr/bin/python3

import re, pyotp, pyperclip

from classes.settings import Settings

from core.qrcode_detect import QRCodeDetect

class DecodeSecretKey(QRCodeDetect):
    
    @classmethod
    def decode(cls, flags):
        copied = False
        qrcode_data = cls.detect(flags)
        
        match_issuer = re.search(r'issuer=([\w]+)', qrcode_data)
        match_secret_key = re.search(r'secret=([A-Z2-7]+)', qrcode_data)
        
        issuer = match_issuer.group(1)
        secret_key = match_secret_key.group(1)
        
        output_otp = pyotp.TOTP(secret_key).now()
        
        if Settings.get('general.auto_copy_code', 'boolean'):
            pyperclip.copy(output_otp)
            copied = True
        
        if Settings.get('advanced.hide_otp_code', 'boolean'):
            output_otp = str('*' * len(output_otp))
        
        print('Issuer:', issuer)
        print('Current OTP Code:', output_otp)

        if copied is True:
            print('-' * 36)
            print('Code OTP copied')
