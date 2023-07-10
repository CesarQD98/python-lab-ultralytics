from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("/models/yolov8m-seg.pt")

    model.train(data="data_config.yaml", epochs=200)
