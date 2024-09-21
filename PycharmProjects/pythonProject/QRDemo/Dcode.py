import cv2
import DecodeQr
import image

import qrcode
# name=input('enter a png file name: ')
# filename='hari.png'
filename=input('enter a png file name: ')
image = cv2.imread(filename)
detector = cv2.QRcodeDetector()
data,vertices_arrey,binary_qrcode=detector.detectAndDdecode(image)
if vertices_arrey is not None:
    print('Qrcode data')
    print(data)
else:
    print("there was something error")


