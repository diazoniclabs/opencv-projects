# importing libraries
import streamlit as st
import cv2
from PIL import Image
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Here is the function for UI
st.title("Face Detection App")
image_file = st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])

if image_file:
    image = Image.open(image_file)
    if st.button("Process"):

            # result_img is the image with rectangle drawn on it (in case there are faces detected)
            # result_faces is the array with co-ordinates of bounding box(es)
             image = np.array(image.convert('RGB'))
             faces = face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=5)
             for (x, y, w, h) in faces:
                 cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
             st.image(image, use_column_width=True)
             st.success("Found {} faces\n".format(len(faces)))

