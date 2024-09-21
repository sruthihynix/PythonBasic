import qrcode
import base64
with open("C:\\Users\HP\\Pictures\\Sruthi 01.jpg",'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())
    qr = qrcode.QRCode()
    qr.add_data(encoded_string)
    qr.make()