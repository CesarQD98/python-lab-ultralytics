import argparse

from ultralytics import YOLO


def args_parser():
    parser = argparse.ArgumentParser(
        description="Initializes training on a specific YOLOv8 model"
    )
    parser.add_argument(
        "-m", "--model", help="Path to pre-trained YOLOv8 model", required=True
    )
    parser.add_argument(
        "-c", "--config", help="Path to the training config file (.yml)", required=True
    )

    args = parser.parse_args()

    return args


def main():
    args = args_parser()
    model_file_path = args.model
    training_config_path = args.config

    # model = YOLO(model_file_path)

    print(args)


if __name__ == "__main__":
    main()
