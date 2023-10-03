🎭 Face Mask Detection System based on YOLO
face mask detection demo

📦 Dataset
You can download the dataset from Google Drive.

This dataset for the pre-trained network is provided by YOLOv3_mask_detect and contains 678 images of individuals both with and without masks.

🗃️ Database
A Firebase database is utilized. We've created a testing database for this project, but users are free to create their own.

🏷️ Classes
NONE - No mask at all.
BAD - Face is partially covered.
GOOD - Mask covers the essential parts of the face.
🤖 Model
To download the models, you can either run download-models.sh in the /models directory or use the following direct links:

mask-yolov3-tiny-prn.cfg
mask-yolov3-tiny-prn.weights
mask-yolov4-tiny-prn.cfg
mask-yolov4-tiny-prn.weights
mask-yolov4.cfg
mask-yolov4.weights
For the full-sized YOLOv3 pre-trained network, please visit here.

📺 Demo Images and Videos
Available on Google Drive.

🔧 How to Run
Clone the project.
Create an empty folder named saved_image.
Navigate to the Database Page to upload images or videos.
Visit the Homepage for a live video stream of face mask detection.
Note: Before running the demo, ensure you've installed all the dependencies listed in requirements.txt into a virtual environment and have downloaded the necessary model and weight files into the model folder.

