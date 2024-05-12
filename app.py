import streamlit as st
import pickle 
import nltk
# #nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

import os
import subprocess



if not os.path.exists("subprocess_ran.flag"):
    # Run the subprocess
    subprocess.call("./setup.sh", shell=True)
    
    # Create the flag file to indicate that the subprocess has been run
    with open("subprocess_ran.flag", "w") as flag_file:
        pass

ps= PorterStemmer()
def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:] #cloning if we directly copy then y.clear will also clear text
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
        
    return " ".join(y)


tfidf = pickle.load(open('models/vectorizer.pkl','rb'))
model = pickle.load(open('models/model.pkl','rb'))
st.image('static/img/logo 2.png', output_format='PNG', width=100 )
st.title("Spam Detectitive - Trustworthy Spam Classifier")

input_sms= st.text_area("Enter the SMS or Email you want check for spam")

if st.button('PREDICT'):
    # 1. preprocess
    transformed_sms = transform_text(input_sms)
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result=model.predict(vector_input)[0]
    # 4. Display
    if result==1:
        st.header("Spam")
    else:
        st.header("Not Spam")