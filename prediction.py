import cv2
from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")
    model = YOLO("./weights/best.pt")

    video_path = "./media/test.mp4"

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model(frame)

            annotated_frame = results[0].plot()

            cv2.imshow("Test en video mp4", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
