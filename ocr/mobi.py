import urllib.request
import cv2
import numpy as np
import time

# Replace the URL with your own IPwebcam shot.jpg IP:port
# url='ftp://192.168.43.1:3721/demofile.txt'

while True:
    # print(url);
    # Use urllib to get the image and convert into a cv2 usable format
    with urllib.request.urlopen('ftp://10.100.0.57:3721/img/wallpaper.jpg') as url:
        imgResp = url.read()

    print(imgResp)
    # imgResp=urllib.urlopen(url)
    # imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    imgNp=np.array(bytearray(imgResp),dtype=np.uint8)
    # img=cv2.imdecode(imgNp,-1)
    f=open('a.png',mode='wb')
    f.write(imgNp)
    # put the image on screen
    # cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    time.sleep(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
