
import glob
from flask import Flask
import cv2

from yolo import YOLO
import datetime
from os.path import join
from glob import glob
from werkzeug.utils import secure_filename
app = Flask(__name__)
IMAGES_FOLDER = "static/images"
VIDEOS_FOLDER = "static/videos"

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "secret key"
app.config['VIDEOS_FOLDER'] = VIDEOS_FOLDER
app.config['IMAGES_FOLDER'] = IMAGES_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


classes = ["good", "bad", "none"]

yolo = YOLO("models/mask-yolov4-tiny.cfg", "models/mask-yolov4-tiny.weights", classes)
yolo.network = 'normal'
yolo.device = int(0)
yolo.size = int(416)
yolo.confidence = float(0.5)

colors = [(0, 255, 0), (0, 165, 255), (0, 0, 255)]


def save(image):
    if image:
        yolo = YOLO("models/mask-yolov4.cfg", "models/mask-yolov4.weights", classes)
        conf_sum = 0
        detection_count = 0
        files = []
        for ext in ('*.png', '*.jpg','*.jpeg'):
            files.extend(glob(join("static/images", ext)))
        for file in files:
            print("file : " + file)

            mat = cv2.imread(file)

            width, height, inference_time, results = yolo.inference(mat)

            for detection in results:
                id, name, confidence, x, y, w, h = detection
                cx = x + (w / 2)
                cy = y + (h / 2)

                conf_sum += confidence
                detection_count += 1

                color = colors[id]
                cv2.rectangle(mat, (x, y), (x + w, y + h), color, 2)
                text = "%s (%s)" % (name, round(confidence, 2))
                cv2.putText(mat, text, (x, y - 5), cv2.FONT_HERSHEY_DUPLEX,
                            0.5, color, 1)
                cv2.imwrite('/Users/jun/Desktop/FYP/{}'.format(file), mat)
    else:
        yolo = YOLO("models/mask-yolov3-tiny-prn.cfg", "models/mask-yolov3-tiny-prn.weights", classes)

        files = []
        for ext in ('*.mp4', '*.mov'):
            files.extend(glob(join("static/videos", ext)))
        for file in files:

            vc = cv2.VideoCapture(file)
            width = int(vc.get(3))
            height = int(vc.get(4))
            fps = int(vc.get(5))
            filename = 'static/videos/output_{0}.mp4'.format(datetime.datetime.now().strftime("%I:%M:%S-%p"))
            fourcc = cv2.VideoWriter_fourcc(*'H264')
            out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
            vc.grab()

            if vc.isOpened():
                rval, frame = vc.read()
            else:
                rval = False

            while rval:

                width, height, inference_time, results = yolo.inference(frame)
                for detection in results:
                    id, name, confidence, x, y, w, h = detection
                    cx = x + (w / 2)
                    cy = y + (h / 2)
                    color = colors[id]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    text = "%s (%s)" % (name, round(confidence, 2))
                    cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, color, 2)
                    out.write(frame)

                rval, frame = vc.read()
            return filename


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    app.run()
