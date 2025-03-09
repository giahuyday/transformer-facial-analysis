import cv2

def get_camera_frame():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không thể mở camera")
        return None
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None



def detect_faces(frame, face_cascade_path="haarcascade_frontalface_default.xml"):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces