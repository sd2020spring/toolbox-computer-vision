""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np
import random

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
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

def blur_faces_webcam(cap, x_blur, y_blur):
    while True:
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
        kernel = np.ones((x_blur, y_blur), 'uint8')
        for (x, y, w, h) in faces:
            frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

def draw_face(frame, x, y, h, w):
    #  attempt to take avg color of face box pixels for better skin match than grey
    # red_sum = 0
    # green_sum = 0
    # blue_sum = 0
    # for i in range(x, x+w):
    #     for j in range(y, y+h):
    #         red_sum += frame[i, j][0]
    #         green_sum += frame[i, j][1]
    #         blue_sum += frame[i, j][2]
    # red_sum /= w*h
    # green_sum /= w*h    ct Toolboxes
    # blue_sum /= w*h
    # color = (red_sum, green_sum, blue_sum)

    angle = 0
    startAngle = 0
    endAngle = 360
    thickness = -1

    # face
    # center_coordinates = (x+w//2, y+h//2)
    # axesLength = (w//2, h//2)
    # color = (127, 127, 127)
    # cv2.ellipse(frame, center_coordinates, axesLength, angle,
    #         startAngle, endAngle, color, thickness)

    #  eyes
    center_coordinates1 = (int(x+w*.275), int(y+h*.35))
    center_coordinates2 = (int(x+w*.725), int(y+h*.35))
    axesLength = (w//10, h//10)
    color = (255, 255, 255)
    cv2.ellipse(frame, center_coordinates1, axesLength, angle,
            startAngle, endAngle, color, thickness)
    cv2.ellipse(frame, center_coordinates2, axesLength, angle,
            startAngle, endAngle, color, thickness)

    #  pupils
    center_coordinates1 = (int(x+w*.275), int(y+h*.375))
    center_coordinates2 = (int(x+w*.725), int(y+h*.375))
    axesLength = (w//32, h//32)
    color = (0, 0, 0)
    cv2.ellipse(frame, center_coordinates1, axesLength, angle,
            startAngle, endAngle, color, thickness)
    cv2.ellipse(frame, center_coordinates2, axesLength, angle,
            startAngle, endAngle, color, thickness)

    # mouth
    center_coordinates = (x+w//2, int(y+h*.7))
    axesLength = (w//4, h//8)
    angle = 0
    startAngle = 15
    endAngle = 165
    thickness = 10
    cv2.ellipse(frame, center_coordinates, axesLength, angle,
            startAngle, endAngle, color, thickness)

def draw_on_faces_webcam(cap, x_blur, y_blur):
    while True:
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20, 20))
        kernel = np.ones((x_blur, y_blur), 'uint8')
        for (x, y, w, h) in faces:
            frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))
            draw_face(frame, x, y, h, w)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                return

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

print('PRESS Q TO QUIT!')

# pick one mode at a time to use program with:
# webcam(cap)
# faces_webcam(cap)
# blur_faces_webcam(cap, 20,20)
draw_on_faces_webcam(cap, 20, 20)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
