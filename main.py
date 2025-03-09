import cv2
from facexformer_pipeline import FacexformerPipeline
from services.data_processing import detect_faces
from services.facexformer_services import agc_detection 
from services.opencv_camera import get_camera_frame

def live_video_detection():
    cap = cv2.VideoCapture(0)  # Mở camera

    if not cap.isOpened():
        print("Cannot open your camera")
        return

    detected_result = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro when read data frame")
            break

        if detected_result:
            text = f"Age: {detected_result['age']} | Gender: {detected_result['gender']} | Race: {detected_result['race']}"
            cv2.putText(frame, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Hiển thị frame
        cv2.imshow("Live Demo - Age, Gender, Race Detection", frame)

        # Nhấn 'c' để capture 1 frame và chạy nhận diện
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            detected_result = agc_detection(frame)  # Nhận diện từ model

        # Nhấn 'q' để thoát
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    live_video_detection()
