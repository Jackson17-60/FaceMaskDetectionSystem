
import os
from datetime import datetime
import time, sched
import cv2
import pyrebase
import pytz
from flask import Flask, flash, request, redirect, url_for, render_template, Response
from pynput.keyboard import Controller
import threading
import upload


keyboard = Controller()

from yolo import YOLO

firebaseConfig = {
    'apiKey': "AIzaSyBNpEAEnL3pviyeubFvLot3UGFfk6WxohQ",
    'authDomain': "testing-1c6cd.firebaseapp.com",
    'projectId': "testing-1c6cd",
    'storageBucket': "testing-1c6cd.appspot.com",
    'messagingSenderId': "65765630850",
    'appId': "1:65765630850:web:5d27e89aaead57b192259b",
    'measurementId': "G-1WZETH63TV",
    'databaseURL': "https://testing-1c6cd-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/jun/Desktop/yolo-mask-detection-main/testing-1c6cd-firebase-adminsdk-u3bau-7568fbdf2d.json"
db_url = "https://testing-1c6cd-default-rtdb.asia-southeast1.firebasedatabase.app/"
directory = "/Users/jun/Desktop/yolo-mask-detection-main/saved_image"
from google.cloud import storage
from firebase import firebase

firebase = firebase.FirebaseApplication(db_url, None)
client = storage.Client()
bucket = client.get_bucket('testing-1c6cd.appspot.com')
imageBlob = bucket.blob("/")

saved_image_path = "/Users/jun/Desktop/yolo-mask-detection-main/saved_image"

classes = ["good", "bad", "none"]
app = Flask(__name__)
app.secret_key = "secret key"
yolo = YOLO("models/mask-yolov3-tiny-prn.cfg", "models/mask-yolov3-tiny-prn.weights", classes)
yolo.network = 'prn'
yolo.device = int(0)
yolo.size = int(416)
yolo.confidence = float(0.5)

colors = [(0, 255, 0), (0, 165, 255), (0, 0, 255)]

app = Flask(__name__, template_folder="templates")
vc = cv2.VideoCapture(0)

s = sched.scheduler(time.time, time.sleep)


def save_img(c, f):
    cv2.imwrite('/Users/jun/Desktop/yolo-mask-detection-main/saved_image/{}.jpg'.format(c), f)
    time.sleep(10)
    today = datetime.today()
    current_date = today.strftime("%d-%m-%Y")
    for file in os.listdir(directory):
        file_name = file
        image_path = "/Users/jun/Desktop/yolo-mask-detection-main/saved_image/" + file_name
        image_blob = bucket.blob(file_name)
        image_blob.upload_from_filename(image_path)  # Upload your image
        image_blob.make_public()
        print(image_blob.public_url)
        data = {
            "date_time": file,
            "url": image_blob.public_url
        }
        db.child(current_date).push(data)
        os.remove(os.path.join(directory, file))


def generate_frames():
    t = None
    counter = 0

    while True:

        rval, frame = vc.read()

        if not rval:
            break
        else:

            width, height, inference_time, results = yolo.inference(frame)
            for detection in results:
                id, name, confidence, x, y, w, h = detection
                cx = x + (w / 2)
                cy = y + (h / 2)

                # draw a bounding box rectangle and label on the image
                color = colors[id]

                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                text = "%s (%s)" % (name, round(confidence, 2))
                cv2.putText(frame, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, color, 2)

                if name == "none":
                    if t is None or not t.is_alive():
                        counter = counter + 1
                        print(counter)
                        current_date_time = datetime.now(tz=pytz.timezone('Asia/Singapore'))
                        date_time_ = current_date_time.strftime("%d-%m-%Y %I:%M:%S %p")
                        cropped_image = frame[y:y + h, x:x + w]
                        t = threading.Thread(target=save_img, args=(date_time_, cropped_image))
                        t.start()

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    if t is not None:
        t.join()


@app.route('/database.html')
def database():
    return render_template('database.html')


@app.route('/database.html', methods=['GET', 'POST'])
def upload_image():
    image = True
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and upload.allowed_file(file.filename):
        filename = upload.secure_filename(file.filename)
        if file.content_type == "video/mp4":
            image = False
            dir = os.listdir("static/videos")
            if len(dir) != 0:
                for check_file in os.listdir("static/videos"):
                    os.remove(os.path.join("static/videos", check_file))
            else:
                pass
            file.save(os.path.join(upload.app.config['VIDEOS_FOLDER'], filename))
            filename = upload.save(image)
            return render_template('database.html', filename=filename, image_value=image)

        else:
            image = True
            file.save(os.path.join(upload.app.config['IMAGES_FOLDER'], filename))
            upload.save(image)
            return render_template('database.html', filename=filename, image_value=image)
    else:
        flash('Allowed file types are - png, jpg, jpeg, mp4')
        return redirect(request.url)


@app.route('/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='images/' + filename, code=301))


@app.route('/<filename>')
def display_video(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='videos/' + filename, code=301))


@app.route('/home.html')
def home():
    return render_template('home.html')


@app.route('/home')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.secret_key = "secret key"
    app.run(debug=True, host="127.0.0.1", port=8888)
