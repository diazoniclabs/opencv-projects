import requests

url = "https://api-us.faceplusplus.com/facepp/v3/detect?api_key='' &api_secret=' '&image_url=https://images-na.ssl-images-amazon.com/images/I/71vp8Lec9JL._UL1500_.jpg"


response = requests.request("POST", url)

values = response.json()

import json

with open("sample.json", "w") as outfile:  
    json.dump(values, outfile)

with open("sample.json") as outfile:  
    x = json.load(outfile)
a = x['faces'][0]['face_rectangle']
a

left= []
top= []
width=[]
height = []
for i in x['faces']:
  left.append(i['face_rectangle']['left'])
  top.append(i['face_rectangle']['top'])
  width.append(i['face_rectangle']['width'])
  height.append(i['face_rectangle']['height'])
print(left,top,width,height)


from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
#left, top, width,height
import cv2
img = cv2.imread('/content/71vp8Lec9JL._UL1500_.jpg')
for i in range(len(left)):
  cv2.rectangle(img,(left[i],top[i]),(left[i]+width[i],top[i]+height[i]),(255,0,0),5)
cv2_imshow(img)
