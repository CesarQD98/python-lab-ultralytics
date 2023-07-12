import cv2
from ultralytics import YOLO

import utils

if __name__ == "__main__":
    model = YOLO("yolov8m-seg.pt")
    model = YOLO("./runs/segment/modelo_chute4/weights/best.pt")

    video_path = "./media/chute_4/output.mp4"

    cap = cv2.VideoCapture(video_path)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_size = (frame_width, frame_height)
    fps = 30

    output = cv2.VideoWriter(
        "./media/" + utils.date_filename_generator(),
        cv2.VideoWriter_fourcc("m", "p", "4", "v"),
        fps,
        frame_size,
    )

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model(frame)

            annotated_frame = results[0].plot()

            output.write(annotated_frame)

            cv2.imshow("Test en video mp4", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    output.release()
    cv2.destroyAllWindows()
