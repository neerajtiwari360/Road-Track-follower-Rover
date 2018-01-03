import cv2
from scipy import misc
import RPi.GPIO as ras
cap=cv2.VideoCapture(0)
r,frame=cap.read()
while(r):
    ras.setmode(ras.BOARD)
    ras.setup(15, ras.OUT)
    ras.setup(19, ras.OUT)
    ras.setup(3, ras.OUT)
    ras.setup(5, ras.OUT)
    ras.setup(7, ras.OUT)
    
    r,frame=cap.read()
    g=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("frame.jpg",g)
    R=misc.imread("frame.jpg",flatten=True)
    

    A=misc.imread('imageS.jpg',flatten=True)
    
    L1=misc.imread('imageL1.jpg',flatten=True)
   
    L2=misc.imread('imageL2.jpg',flatten=True)
 
    R1=misc.imread('imageR1.jpg',flatten=True)
   
    R2=misc.imread('imageR2.jpg',flatten=True)
   
    DS=abs(R-A).sum()/30720
    DL1=abs(R-L1).sum()/30720
    DL2=abs(R-L2).sum()/30720
    DR1=abs(R-R1).sum()/30720
    DR2=abs(R-R2).sum()/30720
    mi=min(DS,DL1,DL2,DR1,DR2)
    #print(DS,'--',DL1,'--',DL2,'--',DR1,'--',DR2)
    if(mi==DS):
       ras.output(15,ras.LOW)
       ras.output(19,ras.LOW)
       ras.output(7,ras.HIGH)
       ras.output(5,ras.LOW)
       ras.output(3,ras.LOW)
       #print('GO_STRAIGHT') 
    if(mi==DL1):
       ras.output(15,ras.LOW)
       ras.output(19,ras.HIGH)
       ras.output(7,ras.LOW)
       ras.output(5,ras.LOW)
       ras.output(3,ras.LOW)
       #print('TURN_LEFT')
    if(mi==DL2):
       ras.output(15,ras.HIGH)
       ras.output(19,ras.LOW)
       ras.output(7,ras.LOW)
       ras.output(5,ras.LOW)
       ras.output(3,ras.LOW)
       #print('TURN_SHARP_LEFT')
    if(mi==DR1):
       ras.output(15,ras.LOW)
       ras.output(19,ras.LOW)
       ras.output(7,ras.LOW)
       ras.output(5,ras.HIGH)
       ras.output(3,ras.LOW)
       #print('TURN_RIGHT')
    if(mi==DR2):
       ras.output(15,ras.LOW)
       ras.output(19,ras.LOW)
       ras.output(7,ras.LOW)
       ras.output(5,ras.LOW)
       ras.output(3,ras.HIGH)
       #print('TURN_SHARP_RIGHT')
       ras.cleanup()
    cv2.imshow('frame',g)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
    
