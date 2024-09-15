import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pyttsx3

path = 'Images'
images = []
mylist = os.listdir(path)

# Loading images and ensuring they are correctly loaded
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is None:
        print(f"Error loading image: {path}/{cl}")
    else:
        images.append(curImg)

def findEncodings(images):
    encodeList = []
    for img in images:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img_rgb)
        if encodings:  # Check if encodings were found
            encoded_face = encodings[0]
            encodeList.append(encoded_face)
        else:
            print("No face encodings found for an image.")
    return encodeList

encoded_face_train = findEncodings(images)

def markEntry1(name, facialDistances):
    with open('unknown.csv', 'a') as f:
        now = datetime.now()
        time = now.strftime('%I:%M:%S %p')
        date = now.strftime('%d-%B-%Y')
        distances_str = ",".join(map(str, facialDistances))
        f.writelines(f'{name}, {time}, {date}, {distances_str}\n')

# Initializing text-to-speech engine
text = pyttsx3.init()
text.say("Please come in front of the camera")
text.runAndWait()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from camera.")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    landmarks = face_recognition.face_landmarks(imgS, faces_in_frame)

    for face_landmark in landmarks:
        nose_tip = face_landmark['nose_tip']
        top_lip = face_landmark['top_lip']
        bottom_lip = face_landmark['bottom_lip']
        left_eye = face_landmark['left_eye']
        right_eye = face_landmark['right_eye']

        # Calculate distances between facial points
        nose_top_lip_distance = np.linalg.norm(np.array(nose_tip[0]) - np.array(top_lip[0]))
        nose_bottom_lip_distance = np.linalg.norm(np.array(nose_tip[0]) - np.array(bottom_lip[0]))
        left_eye_right_eye_distance = np.linalg.norm(np.array(left_eye[0]) - np.array(right_eye[0]))

        facial_distances = [nose_top_lip_distance, nose_bottom_lip_distance, left_eye_right_eye_distance]

        markEntry1("Unknown person", facial_distances)

    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Text-to-speech notifications
text_speech = pyttsx3.init()
text_speech.say("Unknown person has come to visit")
text_speech.runAndWait()

text_speech.say("Please mention the purpose of visit")
text_speech.runAndWait()
