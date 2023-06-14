from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")
    model = YOLO("./runs/segment/train/weights/best.pt")

    results = model.predict(source="https://ultralytics.com/images/bus.jpg", save=True)
