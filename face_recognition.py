import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = ["Ben Afflek", "Elton John","Jerry Seinfield", "Madonna", "Mindy Kaling"]
# features = np.load("features.npy")
# labels = np.load("labels.npy")

faces_recognizer = cv.face.LBPHFaceRecognizer_create()
faces_recognizer.read("face_trained.yml")

DIR = r'C:\Users\carlo\Dropbox (Kansai University)\programing\openCV_python\opencv_lesson\Faces\val\elton_john\1.jpg'
img = cv.imread(DIR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("person", gray)

#detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y: y + h, x: x + w]

    label, confidence = faces_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
    
cv.imshow("Detected face", img)

cv.waitKey(0)
