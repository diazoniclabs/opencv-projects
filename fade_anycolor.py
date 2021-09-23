import cv2
import numpy as np
from matplotlib import colors
color = ['red','green','blue','olive','cyan']
img = np.ones([600,1000,3],dtype='uint8')

def func(r0,g0,b0,c):
        for i in range(0,101,1):
            r= (i * r0 + (100 - i) * 255) / 100
            g= (i * g0 + (100 - i) * 255) / 100
            b= (i * b0 + (100 - i) * 255) / 100
            p = int(r),int(g),int(b)
            print(p)
            img[:,:] = [b,g,r]
            cv2.putText(img,c,(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
            cv2.putText(img,str(p),(10,40),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
            cv2.imshow('Color',img)
            cv2.waitKey(4)#white to color
        
        for i in range(100,0,-1):
            r= (i * r0 + (100 - i) * 255) / 100
            g= (i * g0 + (100 - i) * 255) / 100
            b= (i * b0 + (100 - i) * 255) / 100
            p = int(r),int(g),int(b)
            print(p)
            img[:,:] = [b,g,r]
            cv2.putText(img,c,(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
            cv2.putText(img,str(p),(10,40),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)
            cv2.imshow('Color',img)
            cv2.waitKey(4)#color to white

for i in color:
        op = np.array(colors.to_rgb(i))*255
        op = np.array(op,dtype='int')
        print(op)
        func(op[0],op[1],op[2],i.upper())


cv2.waitKey()
cv2.destroyAllWindows()


