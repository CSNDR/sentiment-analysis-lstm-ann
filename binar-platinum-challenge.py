from flask import Flask, request, jsonify
import re
import pandas as pd
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
import pickle
import numpy as np

app =  Flask(__name__)
app.json_encoder = LazyJSONEncoder

@app.route("/model_ann/v1", methods=['POST'])



@app.route("/upload_file_ann/v1", methods=['POST'])
def post_file():
    file = request.files["file"]


@app.route("/model_lstm/v1", methods=['POST'])



@app.route("/upload_file_lstm/v1", methods=['POST'])
def post_file():
    file = request.files["file"]


if __name__ == "__main__":
    app.run(port=1234, debug=True)