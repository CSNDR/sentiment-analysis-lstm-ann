# ANN and LSTM Sentiment Analysis

Team Members :  Ridha, Novitasari, Dwiky

Sentiment analysis is a process identify feelings and opinion in the text. Sentiment analysis using NLP to identify sentiment and give interpretation of the results.

BACKGROUND of the STUDY : 
- The use of social media in Indonesia is high, it provides a lot of data for sentiment analysis.
- Natural language processing (NLP) technology has growing to ease sentiment analysis on social media.
- Sentiment analysis on social media in Indonesia is popular because it can provide insight about customer feedback and public opinion.

GOAL :
Sentiment analysis on social media can help find out customer response to services, understand public opinion, and identify strengths and service weakness.

METHODOLOGY :


![image](https://user-images.githubusercontent.com/114272161/223031547-6ce70740-25bc-48b4-871d-239316ba0805.png)

DATA : 
https://github.com/CSNDR/binar-platinum-challenge/blob/main/dataset/train_preprocess.tsv

![image](https://user-images.githubusercontent.com/114272161/223032027-0d6320a6-39eb-4fe2-83d1-c2b057464cf0.png)

We handled imbalance data by drop sentiment positive and add neutral data. We collect the sentiment neutral by translated the wikipedia dataset on Kaggle into Indonesia.

![image](https://user-images.githubusercontent.com/114272161/223032866-37f37d6d-3af2-486b-8f18-30596fe53aeb.png)

AVERAGE CHARACTER & WORD Per SENTIMENT :
More average users wrote a lot of words in positive reviews than when writing negative and neutral reviews.

![image](https://user-images.githubusercontent.com/114272161/223033014-f85fcc2b-8d30-44de-8b7e-60c3938b0a86.png)

WORD CLOUD :
![image](https://user-images.githubusercontent.com/114272161/223033187-0befbd7e-90fc-4b46-8ba9-1e0541524eb5.png)

![image](https://user-images.githubusercontent.com/114272161/223033353-df77e073-d88f-4c9a-a51e-e1db28ff1711.png)

![image](https://user-images.githubusercontent.com/114272161/223033429-0ecead72-caea-4310-bb29-b0b17223aff8.png)\

FEATURE EXTRACTION :
 - TFIDF <br />
  A method to express the word weight in text documents by using that formula measure the frequency of occurrence word in the document and throughout available documents.
 - Train Test Split <br />
  The technique of dividing the dataset into training data and data testing to build and evaluate learning models machine.
 - Tokenization and Change Label to Categorical <br />
  Tokenization breaks text into small token, while Change Label to Categorical changes the text labels to categories to prepare text data for machine learning models.
  
  MODEL :
  - LSTM <br />
    LSTM (Long Short-Term Memory) is a type of network artificial nerves that can remember term information long and ignore irrelevant information.
   - ANN <br />
    ANN (Artificial Neural Network) is a neural network an imitation consisting of connected neurons each other and can set how to use information to predict output or take decision.
    
![image](https://user-images.githubusercontent.com/114272161/223037381-c6feb680-de6a-42f4-a0f7-7ac60b3d8639.png)
![image](https://user-images.githubusercontent.com/114272161/223037712-e8b05ca8-eed6-431b-9b93-bbcbff1a7f06.png)
![image](https://user-images.githubusercontent.com/114272161/223037756-1b0dec1f-08ee-42c9-a6d1-2647ca67577d.png)
![image](https://user-images.githubusercontent.com/114272161/223037832-a3c7469d-1e37-4a47-8ce8-4bf20f32534f.png)
![image](https://user-images.githubusercontent.com/114272161/223037910-55b94fdc-afa7-4622-a202-9febc7ad88c1.png)
![image](https://user-images.githubusercontent.com/114272161/223038233-e22e3dd4-724f-4bd4-a8d2-4d560f5a8344.png)


PREDICTION RESULT : <br />
![image](https://user-images.githubusercontent.com/114272161/223038046-008f1977-ce00-478e-a255-1d1d5813d775.png)
![image](https://user-images.githubusercontent.com/114272161/223038149-aa1caae7-5bd9-4157-a0fa-c3838c6cc41f.png)


CONCLUSION :<br />
    - ANN (Artificial Neural Network) and LSTM (Long Short-Term Memory) methods respectively gives good results in text classification. However, in the same case, ANN gives better results than LSTM.<br />
    - Balancing data has a significant influence on the classification results. In the same case, Balanced data gives better results than unbalanced data.
    - Precision, recall, and f1-score in each class are quite high, indicating that the method is used is able to classify text into the right class with the same level of accuracy tall.<br />
    
 RECOMENDATION :<br />
  - To improve the accuracy of text classification, it is recommended to do balancing on the data used. This can be done by adding data to minority class or reduce the data of the majority class.<br />
  - Optimize the hyperparameters used for better classification results.<br />
  - Consider to using another method besides ANN and LSTM, especially if the desired result has not been achieved.<br />
  
  
  THANK YOU ^.^

note: <br />
Since we can't upload more than 100mb, use this link to download the model . <br />
- https://drive.google.com/file/d/1DRRy1xGF7s8c3_7sj3uFYunA7cS1pOVb/view?usp=sharing
