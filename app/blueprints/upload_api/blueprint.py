from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory, make_response, \
    Response
from werkzeug.utils import secure_filename
import tensorflow as tf
import random
import cv2
import os
import time

from models import products, cropped
from middlewares.yolo import detect
from middlewares.knn import get_neighbors

import re
import base64
import numpy as np

upload_api = Blueprint('upload_api', __name__)

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


import uuid

def parse_image(imgData):
    img_str = re.search(b"base64,(.*)", imgData).group(1)
    img_decode = base64.decodebytes(img_str)
    filename = "{}.jpg".format(uuid.uuid4().hex)
    with open('static/images/'+filename, "wb") as f:
        f.write(img_decode)
    return 'static/images/'+filename

@upload_api.route('/webcam_upload', methods =["POST"])
def webcam_upload():
    data = request.get_json()

    # Preprocess the upload image
    img_raw = data['data-uri'].encode()
    image_path = parse_image(img_raw)
    print(image_path)
    (categoryPredict, positions) = detect(image_path)
    print(categoryPredict)

    if len(categoryPredict) > 0:
        croppedDectection = []
        for i in range(len(categoryPredict)):
            croppedDectection.append('static/images/cropped-dectecion-{}.jpg'.format(i))

        croppedObject = cropped.list_object(zip(categoryPredict, croppedDectection))
    else: 
        croppedDectection = None

    objectDetection = 'static/images/object-detection.jpg'

    os.remove(image_path)

    return {"crop":croppedDectection,"full":objectDetection, "details": positions}
    

    # return {"status":"success"}