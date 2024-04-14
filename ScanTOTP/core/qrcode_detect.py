#!/usr/bin/python3

import cv2, requests

import numpy as np
from PIL import Image
from io import BytesIO

from pyzbar.pyzbar import decode as qr_decode

class QRCodeDetect:
    
    @classmethod
    def detect_from_url(cls, image_url):
        response = requests.get(image_url)
        if response.status_code != 200:
            raise Exception('Error on download to image')
        
        image = Image.open(BytesIO(response.content))
        
        gray_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        
        decoded_qr = qr_decode(gray_img)
        return decoded_qr[0].data.decode('utf-8')
    
    @classmethod
    def detect_from_file(cls, image_path):
        image = cv2.imread(image_path)
        
        if image is None:
            raise Exception('Error loading image')

        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        decoded_qr = qr_decode(gray_img)
        return decoded_qr[0].data.decode('utf-8')

    @classmethod
    def detect_from_webcam(cls):
        qrcode_data = ''
        
        cap = cv2.VideoCapture(0)
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
    def detect(cls, flags):
        mode = flags.mode.lower()
        
        match mode:
            case 'file':
                return cls.detect_from_file(flags.image)
            case 'url':
                return cls.detect_from_url(flags.image)
            case 'area':
                return 'TODO: area mode'
            case 'webcam':
                return cls.detect_from_webcam()
            case _:
                return 'Error mode invalid'
