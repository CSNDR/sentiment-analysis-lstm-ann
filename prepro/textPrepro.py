import re
import pickle
import pandas as pd
import csv
import os
# from nltk.corpus import stopwords

from keras_preprocessing.sequence import pad_sequences

class TextProcessing():
    def __init__(self) -> None:
        with open(os.path.join("models", "count_vect.pkl"), 'rb') as f:
            self.count_vect = pickle.load(f)

        with open(os.path.join("models", "tf_transformer.pkl"), 'rb') as f:
            self.tf_transformer = pickle.load(f)

        with open(os.path.join("models", 'tokenizer.pkl'), 'rb') as f:
            self.tokenizer = pickle.load(f)

        self.dfAlay = csv.reader(open(os.path.join("dataset", "new_kamusalay.csv"), 'r'))
        self.dfAlay = pd.DataFrame(self.dfAlay, columns=['original', 'replacement'])
        
        pass

    # remove kata alay
    def normalize_alay(self, line) -> str:
        alay_dict_map = dict(
            zip(self.dfAlay['original'], self.dfAlay['replacement']))
        return ' '.join([alay_dict_map[word] if word in alay_dict_map else word for word in line.split(' ')])

    # remove punctuation
    def remove_punctuation(self, line) -> str:
        return re.sub(r'[^\w\s]', ' ', line)

    # # remove stopword
    # def remove_stopword(self, line) -> str:
    #     stopword_list = set(stopwords.words('indonesian'))
    #     return ' '.join([word for word in line.split(' ') if word not in stopword_list])

    def get_bow(self, text):
        text = text.lower()
        text = self.normalize_alay(text)
        text = self.remove_punctuation(text)
        # text = self.remove_stopword(text)
        clean_text = text
        new_df = pd.DataFrame([text], columns=['text'])
        target_predict = self.count_vect.transform(new_df['text'])
        target_predict = self.tf_transformer.transform(target_predict)
        return clean_text, target_predict

    def get_tokenizer(self, text) -> list:
        text = text.lower()
        text = self.normalize_alay(text)
        text = self.remove_punctuation(text)
        # text = self.remove_stopword(text)
        clean_text = text
        text = self.tokenizer.texts_to_sequences([text])
        return clean_text, pad_sequences(text, maxlen=200)
