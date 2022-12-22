import sqlite3

from flask import Flask, jsonify
from prepro.textPrepro import TextProcessing
from inference.predict import PredictSentiment

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from werkzeug.utils import secure_filename
import os.path

TP = TextProcessing()
predict_model = PredictSentiment()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploadedFiles'


app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info={
        'title': LazyString(lambda: 'Text Labeling API with LSTM and ANN model'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'This API for Text Labeling'),
    },
    host=LazyString(lambda: request.host),
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


def get_db_connection():
    conn = sqlite3.connect(os.path.join("database", "platChallange.db"))
    conn.row_factory = sqlite3.Row
    return conn

def mapping_result(result_prediction):
    if result_prediction == 0:
        return "neutral"
    elif result_prediction == 1:
        return "positive"
    else:
        return "negative"


@swag_from('docs/annDocsAPI.yml', methods=['POST'])
@app.route('/ann-model', methods=['POST'])
def ANNpost_file():
    
    conn = get_db_connection()
    
    reqFile = request.files['upfile']
    fileName = secure_filename(reqFile.filename)
    reqFile.save(os.path.join(
        app.config['UPLOAD_FOLDER'],
        fileName
    ))
    
    with open(r"uploadedFiles/{}".format(reqFile.filename), "r+") as f:
        data = f.read()
        f.seek(0)
        cleanText, bow = TP.get_bow(data)
        result_prediction = predict_model.predict_ann(bow)
        for i, x in enumerate(result_prediction):
            if(i == 0 and x == 1):
                hasil = "neutral"
            elif(i == 1 and x == 1):
                hasil = "positive"
            elif(i == 2 and x == 1):
                hasil = "negative"
        f.write(cleanText)
        f.write('|')
        f.write(hasil)
        f.truncate()

    conn.execute('INSERT INTO annModel (oriText, cleanText, label) VALUES (?, ?, ?)', (data, cleanText, hasil))
    conn.commit()
    conn.close()
    
    json_response = {
        'text': cleanText,
        'sentiment result': hasil,
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from('docs/annDocsAPI_2.yml', methods=['POST'])
@app.route('/ann-model-text', methods=['POST'])
def ANNtextpredict():
    
    conn = get_db_connection()
    
    text = request.form.get('text')
    clean_text,bow = TP.get_bow(text)
    result_prediction = predict_model.predict_ann(bow)
    for i, x in enumerate(result_prediction):
        if(i == 0 and x == 1):
            hasil = "neutral"
        elif(i == 1 and x == 1):
            hasil = "positive"
        elif(i == 2 and x == 1):
            hasil = "negative"
    
    conn.execute('INSERT INTO annModel (oriText, cleanText, label) VALUES (?, ?, ?)', (text, clean_text, hasil))
    conn.commit()
    conn.close()
    
    return jsonify({"text":clean_text, "result_sentiment":hasil})


@swag_from('docs/lstmDocsAPI.yml', methods=['POST'])
@app.route('/lstm-model', methods=['POST'])
def LSTMpost_file():

    conn = get_db_connection()
    
    reqFile = request.files['upfile']
    fileName = secure_filename(reqFile.filename)
    reqFile.save(os.path.join(
        app.config['UPLOAD_FOLDER'],
        fileName
    ))
    
    with open(r"uploadedFiles/{}".format(reqFile.filename), "r+") as f:
        data = f.read()
        f.seek(0)
        clean_text, input_ids = TP.get_tokenizer(data)
        result_prediction = predict_model.predict_lstm(input_ids)
        result_prediction = mapping_result(result_prediction)
        f.write(clean_text)
        f.write('|')
        f.write(result_prediction)
        f.truncate()

    conn.execute('INSERT INTO lstmModel (oriText, cleanText, label) VALUES (?, ?, ?)', (data, clean_text, result_prediction))
    conn.commit()
    conn.close()
    
    json_response = {
        'text': clean_text,
        'sentiment result': result_prediction,
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from('docs/lstmDocsAPI_2.yml', methods=['POST'])
@app.route('/lstm-model-text', methods=['POST'])
def LSTMtextpredict():
    
    conn = get_db_connection()
    
    text = request.form.get('text')
    clean_text,input_ids = TP.get_tokenizer(text)
    result_prediction = predict_model.predict_lstm(input_ids)
    result_prediction = mapping_result(result_prediction)
    
    conn.execute('INSERT INTO lstmModel (oriText, cleanText, label) VALUES (?, ?, ?)', (text, clean_text, result_prediction))
    conn.commit()
    conn.close()
    
    return jsonify({"text":clean_text, "result_sentiment":result_prediction})

if __name__ == '__main__':
    app.run(debug=True, port=1234)