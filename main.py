from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.yaml")
    model = YOLO("yolov8n-seg.pt")
    model = YOLO("yolov8n-seg.yaml").load("yolov8n.pt")

    model.train(data="coco128-seg.yaml", epochs=100, imgsz=640)
