import cv2
import numpy as np
import face_recognition
img1_bgr=face_recognition.load_image_file("Images/swa1.jpg")
img1_rgb=cv2.cvtColor(img1_bgr,cv2.COLOR_BGR2RGB)
train_encode=face_recognition.face_encodings(img1_rgb)[0]
test=face_recognition.load_image_file("Images/swa2.jpg")
test_rgb=cv2.cvtColor(test,cv2.COLOR_BGR2RGB)
test_encode=face_recognition.face_encodings(test_rgb)[0]
print(face_recognition.compare_faces([train_encode],test_encode))