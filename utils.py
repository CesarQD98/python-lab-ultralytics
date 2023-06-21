from ultralytics import YOLO
import cv2
import numpy

from datetime import datetime


def save_images(res: list, img: numpy.ndarray):
    for result in res:
        boxes = result.boxes.cpu().numpy()
        for i, box in enumerate(boxes):
            r = box.xyxy[0].astype(int)
            crop = img[r[1] : r[3], r[0] : r[2]]
            cv2.imwrite(str(i) + ".jpg", crop)


def date_filename_generator():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
