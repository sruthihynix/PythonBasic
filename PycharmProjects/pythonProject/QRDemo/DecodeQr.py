#

import cv2
import numpy as np
import sys
import time
if len(sys.argv)>1:
    inputImage = cv2.imread(sys.argv[1])
else:
    a11=input("nam1")
    s1=a11+".svg"

    inputImage = cv2.imread(s1)
# Display barcode and QR code location

qrDecoder = cv2.QRCodeDetector()

# Detect and decode the qrcode
data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
if len(data)>0:
    print("Decoded Data : {}".format(data))
