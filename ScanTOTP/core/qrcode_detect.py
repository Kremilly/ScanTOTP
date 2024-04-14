#!/usr/bin/python3

import os, cv2, requests, pyperclip, base64

import numpy as np
from PIL import Image
from io import BytesIO

from pyzbar.pyzbar import decode as qr_decode

from classes.settings import Settings

class QRCodeDetect:
    
    @classmethod
    def detect_from_url(cls, image_url):
        response = requests.get(image_url)
        if response.status_code != 200:
            raise Exception('Error on download to image')
        
        image = Image.open(BytesIO(response.content))
        
        gray_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        
        decoded_qr = qr_decode(gray_img)
        if len(decoded_qr) > 0:
            return decoded_qr[0].data.decode('utf-8')
    
    @classmethod
    def detect_from_file(cls, image_path):
        image = cv2.imread(image_path)
        
        if image is None:
            raise Exception('Error loading image')

        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        decoded_qr = qr_decode(gray_img)
        
        if len(decoded_qr) > 0:
            return decoded_qr[0].data.decode('utf-8')

    @classmethod
    def detect_from_webcam(cls, webcam=None):
        qrcode_data = ''
        webcam_selected = Settings.get('general.webcam', 'int')
        
        if webcam:
            webcam_selected = webcam
        
        cap = cv2.VideoCapture(webcam_selected)
        detector = cv2.QRCodeDetector()
        
        print("Press 'Q' to quit Webcam mode")
        
        while True:
            _, img = cap.read()
            data, bbox, _ = detector.detectAndDecode(img)
            
            if bbox is not None:
                bbox = bbox[0].astype(int)
                
                for i in range(len(bbox)):
                    cv2.line(
                        img, tuple(bbox[i]), tuple(
                            bbox[(i+1) % len(bbox)]
                        ), color=(
                            255, 0, 0
                        ), thickness=2)
                    
                    pass
                
                if data:
                    qrcode_data = data

            cv2.imshow('img', img)
            if cv2.waitKey(1) == ord('q'):
                break
            
            if len(qrcode_data) > 0:
                return qrcode_data
    
    @classmethod
    def detect(cls, flags, show=False):
        mode = flags.mode.lower()
        
        match mode:
            case 'file':
                result = cls.detect_from_file(flags.input)
            case 'url':
                result = cls.detect_from_url(flags.input)
            case 'webcam':
                result = cls.detect_from_webcam(flags.webcam)
            case _:
                result = 'Error mode invalid'
                
        if show:
            return print(result)
        
        return result
