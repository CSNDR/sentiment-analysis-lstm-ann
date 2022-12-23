from io import StringIO
import streamlit as st
import pandas as pd
import requests
    
def call_api(text, path):
    url = f"http://127.0.0.1:5000/{path}"
    data = {'text': text}
    response = requests.post(url, data=data)
    return response.json()['result_sentiment']

# call api for file upload
def call_api_file(upfile, path):
    url = f"http://127.0.0.1:5000/{path}"
    files = {'upfile': upfile}
    response = requests.post(url, files=files)
    return response.json()['sentiment result']
    
st.title("Predict Sentiment Analysis in Bahasa Indonesia")
st.subheader("Binar Platinum Challenge Projects")


option = st.selectbox(
    'Which machine learning model to use??',
    ('LSTM', 'ANN'))
text = st.text_input('Enter a sentence/word in Bahasa Indonesia')

if text:
    if option == 'LSTM':
        path = 'lstm-model-text'
        result = call_api(text,path)
    else:
        path = "ann-model-text"
        result = call_api(text,path)
    st.write("Sentimentt: ", result)
    
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if option == 'LSTM':
        path = 'lstm-model'
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio.getvalue())
        result = call_api_file(stringio.getvalue(),path)
    else:
        path = "ann-model"
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio.getvalue())
        result = call_api_file(stringio.getvalue(),path)
    st.write("Sentiment: ", result)

    
