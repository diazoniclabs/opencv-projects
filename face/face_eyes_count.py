import cv2
a = cv2.imread('people.jpg')
model_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model_eye = cv2.CascadeClassifier('haarcascade_eye.xml')
demo_face = model_face.detectMultiScale(a,1.1,15)
demo_eye = model_eye.detectMultiScale(a,1.1,15)
count_f = str(len(demo_face))
count_e = str(len(demo_face))
print(f'People Count: {count_f}')
cv2.putText(a, f'People Count: {count_f}', (20, 25), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            1, (255, 255, 255), 1)
cv2.putText(a, f'Eye Count: {count_e}', (500, 25), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
            1, (255, 255, 255), 1)
count_face = 1
count_eyes = 1
for (x,y,w,h) in demo_face:

    cv2.rectangle(a,(x,y),(x+h,y+w),(255,100,0),5)
    cv2.putText(a, str(count_face), (x, y), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 255, 255), 3)
    count_face=count_face+1
    cv2.imshow('Wind', a)
    cv2.waitKey(500)

for (x,y,w,h) in demo_eye:
    cv2.rectangle(a,(x,y),(x+h,y+w),(0,255,255),5)
    cv2.putText(a, str(count_eyes), (x, y), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 255), 2)
    count_eyes=count_eyes+1
    cv2.imshow('Wind', a)
    cv2.waitKey(500)

cv2.waitKey(2000)
cv2.destroyAllWindows()
