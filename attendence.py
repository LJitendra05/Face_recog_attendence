import cv2
import face_recognition
from PIL import Image
import os
import numpy as np
import pandas as pd
from datetime import datetime
import csv
import time

# Load known face encodings
known_faces_dir = 'captured_faces'
known_encodings = []
known_names = []

for filename in os.listdir(known_faces_dir):
    if filename.endswith(('.jpg', '.png')):
        img_path = os.path.join(known_faces_dir, filename)
        # image=load_valid_image(img_path)
        # cv2.imwrite('converted_gray.jpg', image)
        image=face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(filename)[0])  # Use filename (without extension) as name

student=known_names.copy()
face_locations=[]
face_encodings=[]
s=True
vid_cap=cv2.VideoCapture(0)
now=time.time()
curr_date=datetime.fromtimestamp(now).strftime('%d-%m-%Y')
attendance_file = 'Attendence/attendence_'+curr_date+'.csv'
if not os.path.exists(attendance_file):
    pd.DataFrame(columns=["Name", "Time"]).to_csv(attendance_file, index=False)
f=open(attendance_file,'a+',newline='')
lnwriter=csv.writer(f)
frame_count=0
frame_count_fac=40
while True:
    _, frame = vid_cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    frame_count+=1
    rgb_small_frame =cv2.cvtColor(small_frame,cv2.COLOR_BGR2RGB) # Convert BGR to RGB
    face_names=[]
    cv2.putText(frame,str("Press 'q' to quit."),(50,430),cv2.FONT_HERSHEY_COMPLEX,0.75,(255,255,0),1)
    if s and frame_count%frame_count_fac==0 : 
        face_locations = face_recognition.face_locations(rgb_small_frame,model='cnn')
        if not face_locations:
            continue  # No face found, skip frame

        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]

            face_names.append(name)

            if name in student:
                now = time.time()
                curr_time = datetime.fromtimestamp(now).strftime('%H:%M:%S')
                lnwriter.writerow([name, curr_time])
                student.remove(name)  # Prevent duplicate entry
                # print(f"{name} marked present at {curr_time}")

    # Display result
    for (top,right,bottom,left), name in zip(face_locations, face_names):
        # Scale back up 
        top *= 4 
        right *= 4 
        bottom *= 4
        left *= 4
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid_cap.release()
cv2.destroyAllWindows()
f.close()