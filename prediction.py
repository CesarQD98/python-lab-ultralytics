import cv2
import numpy as np
from ultralytics import YOLO
import time

if __name__ == "__main__":
    model = YOLO("yolov8m-seg.pt")
    model = YOLO("./runs/segment/modelo_chute1/weights/best.pt")

    video_path = "./media/chute_1/output.mp4"

    cap = cv2.VideoCapture(video_path)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_size = (frame_width, frame_height)
    fps = 30

    # output = cv2.VideoWriter(
    #     "./media/" + utils.date_filename_generator(),
    #     cv2.VideoWriter_fourcc("m", "p", "4", "v"),
    #     fps,
    #     frame_size,
    # )

    while cap.isOpened():
        success, frame = cap.read()

        if success:
            results = model(frame)

            print(results)
            print(len(results))
            print(type(results))

            # Guarda el resultado en variable masks
            masks = results[0].masks
            class_tensor = results[0].boxes.cls

            # Lista con las clases detectadas
            class_list = [int(elem) for elem in class_tensor]

            # Creacion de lista

            for mask in masks:
                # Genera imagen con pixels de blanco usando cv2.fillPoly
                img = np.zeros((frame_height, frame_width, 3), np.uint8)

                points = masks[0].xy[0].astype(int)
                data_points = [tuple(elem) for elem in points]

                cv2.fillPoly(img, np.array([data_points]), (255, 255, 255))

                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                white_pixels_count = cv2.countNonZero(img_gray)

            # for elem in points:
            #     data_points.append(tuple((elem)))

            t1 = time.time()
            print(t1)
            t2 = time.time()
            print(t2)

            # Contabiliza los pixeles blancos con cv2.countNonZero
            t3 = time.time()

            t4 = time.time()
            # TODO: Calcula el procentaje de cobertura con respecto a 1920x1080

            # TODO: Implementar loop entre todas las masks (objetos) detectadas

            # annotated_frame = results[0].plot()

            # output.write(annotated_frame)

            # cv2.imshow("Test en video mp4", annotated_frame)
            print("t1: %.2f" % (t2 - t1))
            print("t2: %.2f" % (t3 - t2))
            print("t3: %.2f" % (t4 - t3))
            print("tt: %.2f" % (t4 - t1))
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            break
        else:
            break

    cap.release()
    # output.release()
    cv2.destroyAllWindows()
