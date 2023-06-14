from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")
    model = YOLO("./runs/segment/train3/weights/best.pt")

    results = model.predict(source="test2.png", save=True)
