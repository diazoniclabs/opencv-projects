path = '/content/pieces-classic-italian-pepperoni-pizza-black-background-top-view-high-quality-photo_275899-625.jpg'
img = cv2.imread(path)
edge = cv2.Canny(img, 100, 200)
_,thresh = cv2.threshold(edge, 130, 255, cv2.THRESH_BINARY)

import numpy as np

kernel = np.ones((3,3),np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) #Close
morph = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel)

cnts,_ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
count =0
for c in cnts:
  if cv2.contourArea(c) > 200: # ignore small objects
    cv2.drawContours(img, [c], -1,(255,255,255), 2)
    count = count+1

text = 'Number of slices detected: {}'.format(count)
cv2.putText(img,text,(150,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
cv2_imshow(img)
cv2.contourArea(c)
