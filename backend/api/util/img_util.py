from flask import current_app as app, jsonify
from werkzeug.utils import secure_filename
import os
import datetime


def allowed_img(filename):
    data = '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ['jpg', 'jpeg', 'png']
    return data


def validate_img(file):
    if file and allowed_img(file.filename):
        filename = "img_" + file.filename
        filename = secure_filename(filename)
        file.save(os.path.join(app.config['IMG_FOLDER'], filename))
        return filename


def delete_img(filename):
    path = os.path.join(app.config['IMG_FOLDER'], filename)
    os.remove(path)
