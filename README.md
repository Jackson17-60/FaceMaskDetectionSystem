# 🎭Face Mask Detection System based on YOLO
![face 1 47 06 PM](https://user-images.githubusercontent.com/69899426/142359428-77bd8e4e-3471-402c-ab63-195024d5710b.jpeg)

# 📦 Dataset
Download dataset from [Google Drive](https://drive.google.com/drive/folders/1aAXDTl5kMPKAHE08WKGP2PifIdc21-ZG)

The dataset for this pre-trained network is provided by https://github.com/VictorLin000/YOLOv3_mask_detect which contains 678 images of people with and without masks.


# 🗃️ Database
A Firebase database is utilized. We've created a testing database for this project, but users are free to create their own.

# 🏷️ Classes
NONE - No mask at all.
BAD - Face is partially covered.
GOOD - Mask covers the essential parts of the face.

# 🤖 Model
To download the models, you can either run download-models.sh in the /models directory or use the following direct links:

- [mask-yolov3-tiny-prn.cfg](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov3-tiny-prn.cfg)
- [mask-yolov3-tiny-prn.weights](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov3-tiny-prn.weights)
- [mask-yolov4-tiny-prn.cfg](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4-tiny.cfg)
- [mask-yolov4-tiny-prn.weights](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4-tiny.weights)
- [mask-yolov4.cfg](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4.cfg)
- [mask-yolov4.weights](https://github.com/cansik/yolo-mask-detection/releases/download/pre-trained/mask-yolov4.weights)
  
For the full-sized YOLOv3 pre-trained network, please visit here.

# 📺 Demo Images and Videos
[Google Drive](https://drive.google.com/drive/folders/1tbqElh98EyqO7uXSVx5wrNaKg_Tpn6QG?usp=sharing)

# 🔧 How to Run
1. Clone the project.
2. Create an empty folder named saved_image.
3. Navigate to the Database Page to upload images or videos.
4. Visit the Homepage for a live video stream of face mask detection.
   
Note: Before running the demo, ensure you've installed all the dependencies listed in requirements.txt into a virtual environment and have downloaded the necessary model and weight files into the model folder.

