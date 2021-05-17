from flask import Flask, request, jsonify
from flask_cors import CORS
from api.util.img_util import validate_img, allowed_img, delete_img
from api.cifar10.model import pred_cifar_10
import os

app = Flask(__name__)
CORS(app)

IMG_FOLDER = './static'
app.config['IMG_FOLDER'] = IMG_FOLDER


@app.route('/cifar10', methods=['POST'])
def cifar10():
    img = request.files['file']
    filename = validate_img(img)
    path = os.path.join(app.config['IMG_FOLDER'], filename)
    path = os.path.abspath(path)
    print("path-img ", path)

    res = pred_cifar_10(path)
    response = {"prediction": res}

    delete_img(filename)

    return jsonify(response), 200


if(__name__ == '__main__'):
    app.run(debug=True)
