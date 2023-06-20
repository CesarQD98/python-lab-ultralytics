from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")

    model.train(data="data_config.yaml", epochs=100)
