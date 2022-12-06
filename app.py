from flask import Flask, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploadedFiles'

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from werkzeug.utils import secure_filename
import os.path

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'Text Labeling API with LSTM and ANN model'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'This API for Text Labeling'),
    },
    host = LazyString(lambda: request.host),
)
swagger_config = {
    'headers': [],
    'specs': [
        {
        'endpoint': 'docs',
        'route': '/docs.json',
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route': '/docs/',
}
swagger = Swagger(app, template=swagger_template, 
                  config=swagger_config)


@swag_from('docs/annDocsAPI.yml', methods=['POST'])
@app.route('/ann-model', methods=['POST'])
def ANNpost_file():
    
    reqFile = request.files['upfile']
    fileName = secure_filename(reqFile.filename)
    reqFile.save(os.path.join(
                app.config['UPLOAD_FOLDER'],
                fileName
            ))
    with open(r"uploadedFiles/{}".format(reqFile.filename),"r+") as f:
        data = f.read()
    
    json_response = {
        'result': data,
    }
    
    response_data = jsonify(json_response)
    return response_data

@swag_from('docs/lstmDocsAPI.yml', methods=['POST'])
@app.route('/lstm-model', methods=['POST'])
def LSTMpost_file():
    
    reqFile = request.files['upfile']
    fileName = secure_filename(reqFile.filename)
    reqFile.save(os.path.join(
                app.config['UPLOAD_FOLDER'],
                fileName
            ))
    with open(r"uploadedFiles/{}".format(reqFile.filename),"r+") as f:
        data = f.read()
    
    json_response = {
        'result': data,
    }
    
    response_data = jsonify(json_response)
    return response_data



if __name__ == '__main__':
    app.run()