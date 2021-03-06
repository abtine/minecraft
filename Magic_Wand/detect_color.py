# import the necessary packages

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np



# initialize the camera and grab a reference to the raw camera
# capture
camera = PiCamera()
#camera.resolution = (640, 480)
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
time.sleep(1)
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g


#inspired from https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/        

def detec(color,img):
    """Detect if there is a BLUE or RED object in the image
"""
    #Min and max values for detection
    if color=="RED":
        lower=[0, 0, 60],
        upper=[80, 80, 255]
    if color=="BLUE":
        lower =[65, 0, 0],
        upper=[255, 50, 60]
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    #Mask within the right values
    mask = cv2.inRange(img, lower, upper)
    output = cv2.bitwise_and(img, img, mask = mask)
    cv2.imshow("images", np.hstack([img, output]))
    blurred = cv2.GaussianBlur(output, (11, 11), 0)
    edged = cv2.Canny(blurred, 30, 150)
    (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #After 5sec detection the function return True
    t0=time.time()
##    while len(cnts)>=1:
##        t1=time.time()
##        if t1-t0>=5:
##            return True


##def PaintAndReturn(color,img):
##    """Paint image RED or BLUE if an object of same color is detected
##"""
##    global v
##    if color=="RED":
##        c=(0,0,255)
##        m="R"
##    if color=="BLUE":
##        c=(255,0,0)
##        m="B"
##    if detec(color,img):
##        img[0:240,0:120]=c
##        v=str(img)+m
##        return v


        
# capture frames from the camera
for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image
    frame = f.array   

    frameClone = frame.copy()
    #All frames are separated
    Left= frameClone[0:240,0:120]
    LU=Left[0:120,0:120]
    LD=Left[120:240,0:120]
    Mid=frameClone[0:240,120:200]
    Right= frameClone[0:240,200:320]
    RU=Right[0:120,0:120]
    RD=Right[120:240,0:120]


    detec("RED",LD)
# Don't work when all functions are used at same time
##    PaintAndReturn("RED",LD)
##    PaintAndReturn("RED",LU)
##    PaintAndReturn("RED",Mid)
##    PaintAndReturn("RED",RU)
##    PaintAndReturn("RED",RD)
##    PaintAndReturn("BLUE",LD)
##    PaintAndReturn("BLUE",LU)
##    PaintAndReturn("BLUE",Mid)
##    PaintAndReturn("BLUE",RU)
##    PaintAndReturn("BLUE",RD)
    
    
    #Stack images
    Right2=np.vstack([RU,RD])
    Left2=np.vstack([LU,LD])    
    All=np.hstack([Left2,Mid,Right2])
    #Red lines
    All[0:240,119:122]=(0,0,255)
    All[0:240,199:202]=(0,0,255)
    All[119:122,0:119]=(0,0,255)
    All[119:122,202:320]=(0,0,255)


    cv2.imshow("All",All)


    rawCapture.truncate(0)

    # if the 'q' key is pressed, stop the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
