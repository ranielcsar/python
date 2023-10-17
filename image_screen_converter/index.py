from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from .converter import resize_images_to_screen_sizes


app = Flask(__name__)
CORS(app, origins=r"/*")


@app.route("/")
def is_alive():
    return "true"


@app.route("/convert", methods=["POST"])
def convert_images():
    image = request.files["image"]

    resized_images = resize_images_to_screen_sizes(image)
    print(jsonify(resized_images))
    return "funcionou"


if __name__ == "__main__":
    app.run()
