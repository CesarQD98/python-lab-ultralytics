from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8m-seg.pt")

    model.train(data="data_config_chute4.yaml", epochs=100)
