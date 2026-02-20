import cv2
import os
from PIL import Image
import numpy as np
# Load OpenCV's pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create a directory to save faces
output_dir = 'captured_faces'
os.makedirs(output_dir, exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)
# face_id = 0
name=input('Enter name:')
# print("Press 's' to save a face, 'q' to quit.")



while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles and show faces
    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame,str("Press 's' to save a face,'q' to quit."),(50,430),cv2.FONT_HERSHEY_COMPLEX,0.75,(255,255,0),1)
    cv2.imshow("Face Capture", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s') and len(faces) > 0:
        # Save first detected face
        (x, y, w, h) = faces[0]
        face_img = frame[y:y+h, x:x+w]
        small_frame = cv2.resize(face_img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame =cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB)
        face_filename = os.path.join(output_dir, f"{name}.jpg")
        cv2.imwrite(face_filename, rgb_small_frame)
        # cv2.putText(frame,'f"Saved {face_filename}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
        # print(")
        # face_id += 1

    elif key == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
