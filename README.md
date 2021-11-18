# About
A Face Mask Detection System based on YOLO

![face 1 47 06 PM](https://user-images.githubusercontent.com/69899426/142359428-77bd8e4e-3471-402c-ab63-195024d5710b.jpeg)

# Dataset
Download dataset from [Google Drive](https://drive.google.com/drive/folders/1aAXDTl5kMPKAHE08WKGP2PifIdc21-ZG)

The dataset for this pre-trained network is provided by https://github.com/VictorLin000/YOLOv3_mask_detect which contains 678 images of people with and without masks.

# Database
Firebase database is used and a testing database is created for this case. User can create their own

# Classes

- NONE - No mask at all.
- BAD - Partial covered face.
- GOOD - Mask coveres the essential parts.


# Model
To download the models just run the download-models.sh in /models or use the following links:

- [mask-yolov3-tiny-prn.cfg](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov3-tiny-prn.cfg)
- [mask-yolov3-tiny-prn.weights](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov3-tiny-prn.weights)
- [mask-yolov4-tiny-prn.cfg](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4-tiny.cfg)
- [mask-yolov4-tiny-prn.weights](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4-tiny.weights)
- [mask-yolov4.cfg](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4.cfg)
- [mask-yolov4.weights](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4.weights)

The full size YOLOv3 pre-trained network, can be found at : https://github.com/VictorLin000/YOLOv3_mask_detect

# Demo images and videos

[Google Drive](https://drive.google.com/drive/folders/1tbqElh98EyqO7uXSVx5wrNaKg_Tpn6QG?usp=sharing)

# Run
To run the demo, please first install all the dependencies (requirements.txt) into a virtual environment and download the model and weights into the model folder 

- GitClone the project
- Create empty folder named saved_image
- Go to Database Page to upload images or videos
- Go to Homepage for live video stream face mask detection







