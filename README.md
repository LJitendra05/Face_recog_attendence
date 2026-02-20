# Face Recognition Based Attendance System

A real-time attendance system that uses **face recognition** to automatically mark attendance using a webcam. This project is implemented in **Python** using **OpenCV** and the **face_recognition** library with a CNN-based face detection model for improved accuracy.

---

## 📌 Features

* Real-time face detection using CNN model
* Automatic attendance marking
* High-accuracy face recognition
* Prevents proxy attendance
* CSV-based attendance record
* Easy to add/remove users
* Live webcam integration

---

## 🛠️ Technologies Used

* Python 3.x
* OpenCV
* face_recognition
* NumPy
* Pandas
* dlib

---

## 📂 Project Structure

$0

---

## 📦 requirements.txt

Create a `requirements.txt` file with the following:

```
opencv-python
face_recognition
numpy
pandas
Pillow
streamlit
streamlit-autorefresh
dlib
```

> Note: `os`, `csv`, `time`, and `datetime` are part of Python’s standard library and do not need to be included.

---

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/face-recognition-attendance-system.git
cd face-recognition-attendance-system
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If you face issues installing **dlib**, install using:

```bash
pip install cmake
pip install dlib
```

---

## 🧑‍💻 How to Use

### Step 1: Add Images

* Add clear front-facing images of users inside the `images/` folder.
* Image name should be the person's name (e.g., `Jitendra.jpg`).

### Step 2: Encode Faces

Run the encoding script:

```bash
python encode_faces.py
```

This will generate encoded facial features for recognition.

### Step 3: Run Attendance System

```bash
python attendance.py
```

* The webcam will open.
* When a registered face is detected, attendance will be marked automatically in `Attendance.csv`.

---

## 📝 Attendance Format

```
Name, Date, Time
Jitendra, 20-02-2026, 10:12:45
```

---

## 📷 Notes

* Ensure good lighting conditions for accurate detection.
* Use multiple images per person for better accuracy.
* CNN model may require GPU support for faster processing.

---

## 🚀 Future Improvements

* GUI integration
* Database support
* Mask detection
* Email notification
* Cloud storage

---

## 📄 License

This project is for educational purposes only.

---

## 🙌 Acknowledgements

* OpenCV
* face_recognition Library
* dlib

---

**Developed by:** L Jitendra Kumar
