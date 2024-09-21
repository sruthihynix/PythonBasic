"""GENERATING QR-CODE AND SAVE IT IN .png format"""

import qrcode
import pyqrcode
# x=(D:\sruthi mob pics  2021\Tikku 7)
name=input('enter name : ')
img=qrcode.make(name+'9048133580,VIHAAN,3b')

QRCfile=name+'.png' #adding extension '.png' to filename

Qimage=qrcode.make(name)    # create qr code using make()
Qimage.save(QRCfile)        # saving file

