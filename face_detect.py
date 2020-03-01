""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

def webcam(cap):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))

        # Display the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return

def faces_webcam(cap):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

def blur_faces_webcam(cap, x_blur, y_blur):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))

        kernel = np.ones((x_blur, y_blur), 'uint8')
        for (x, y, w, h) in faces:
            frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

def draw_on_faces_webcam(cap):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))

        # kernel = np.ones((x_blur, y_blur), 'uint8')
        for (x, y, w, h) in faces:
            # frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))

            # TODO: add more shit here

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

webcam(cap)
# faces_webcam(cap)
# blur_faces_webcam(cap, 20,1)
# draw_on_faces_webcam(cap)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
