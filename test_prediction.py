from ultralytics import YOLO
import cv2
import utils

if __name__ == "__main__":
    model = YOLO("yolov8n-seg.pt")
    model = YOLO("./weights_techinn/best.pt")

    test_image = cv2.imread("./media/test.png")

    print(type(test_image))

    # res = model.predict(source=test_image, save=True, save_txt=True)
    res = model(test_image)

    res_plotted = res[0].plot()
    res_boxes = res[0].boxes
    print("Cantidad de boxes -> ", len(res_boxes))

    utils.save_images(res, test_image)

    cv2.imshow("result", res_plotted)
    cv2.waitKey(0)
