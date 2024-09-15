import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pyttsx3
import pickle
import dlib
import speech_recognition as sr
from gtts import gTTS
path='Images'
images = []
classNames = []
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encodeList.append(encoded_face)
    return encodeList
encoded_face_train = findEncodings(images)
def markEntry(name):
    with open('Entry.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'n{name}, {time}, {date}')
def markEntry1(name,encoded_faces):
    with open('unknown.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            encode = encoded_faces
            f.writelines(f'n{name}, {time}, {date},{encode}')
def markEntry2(encoded_face):
    with open('e.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            encode = encoded_faces
            f.writelines(f'n{name}, {time}, {date},{encode}')
detector = dlib.get_frontal_face_detector()
new_path ="D:/BMSIT PAST/PBL2/PBL2/save_images/"
def save(img,name, bbox, width=180,height=227):
    x, y, w, h = bbox
    down_width=width
    down_height=height
    down_points = (down_width, down_height)
    imgCrop = img[y:h, x: w]
    imgCrop = cv2.resize(imgCrop, down_points, interpolation= cv2.INTER_LINEAR)#we need this line to reshape the images
    now = datetime.now()
    time = now.strftime('%I%M%S%p')
    date = now.strftime('%d%B%Y')
    name=name+date+time
    cv2.imwrite(name+".jpg",imgCrop)

text = pyttsx3.init()
text.say("Please come in front of camera")
# play the speech
text.runAndWait()
cap  = cv2.VideoCapture(0)
count =0
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
    for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)
        print(matchIndex)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper().lower()
            y1,x2,y2,x1 = faceloc
            # since we scaled down by 4 times
            y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            markEntry(name)
        else:
            name="Unknown person"
            markEntry1(name,encoded_faces)
            gray = cv2.cvtColor(imgS, cv2.COLOR_RGB2GRAY)
            faces = detector(gray)
            for counter, face in enumerate(faces):
                print(counter)
                x1, y1 = face.left(), face.top()
                x2, y2 = face.right(), face.bottom()
                # cv2.rectangle(frame, (x1, y1), (x2, y2), (220, 255, 220), 1)
                # MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0, 250, 0), 3)
                # save(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit))
                save(gray, new_path, (x1, y1-20, x2, y2))


    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

text_speech = pyttsx3.init()
text_speech.say(name+"has come to visit")
# play the speech
text_speech.runAndWait()
if name=="Unknown person":
    text_speech = pyttsx3.init()
    text_speech.say("Please mention the purpose of visit")
    text_speech.runAndWait()


    def get_audio():
        r = sr.Recognizer();
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""
            try:
                said = r.recognize_google(audio)
                print(said)
            except Exception as e:
                print("Exception " + str(e))
        return said


text = get_audio()
if "delivery" in text:
    text_speech = pyttsx3.init()
    text_speech.say("Please keep delivery at the doorstep")
    text_speech.runAndWait()
if "parcel" in text:
    text_speech = pyttsx3.init()
    text_speech.say("Please keep parcel at the doorstep")
    text_speech.runAndWait()