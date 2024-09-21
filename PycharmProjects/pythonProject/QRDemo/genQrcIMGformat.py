"""GENERATING QR-CODE AND SAVE IT IN .png format"""

import qrcode
import pyqrcode
# x=(D:\sruthi mob pics  2021\Tikku 7)
# name=input('enter name : ')
# img=qrcode.make('VINOD T.S,Mob:9847898146,e-mail : vinodhynix@gmai.com')
# img.save('Vinod TS.jpg')

# img=qrcode.make(name+'9048133580,VIHAAN,3b')
# img.save("VIH.jpg")


img=qrcode.make('Hai....\n Have a Nice Day')
img.save("hai.jpg")
# print(type(img))
# print(img.box_size)