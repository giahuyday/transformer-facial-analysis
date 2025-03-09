import cv2
from image_input_handler import UniversalImageInputHandler


def image_processing(img_path):
    # Xử lý hình ảnh đầu vào
    uih = UniversalImageInputHandler(img_path, debug=False)
    img = uih.img
    
    return img

def detect_faces(frame, face_cascade_path="haarcascade_frontalface_default.xml"):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + face_cascade_path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces