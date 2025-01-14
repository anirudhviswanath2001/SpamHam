import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
ps=PorterStemmer()
nltk.download('all')

def transfrom_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


st.title("Email Spam Classifier")

input_sms=st.text_input("Enter your Message: ")


if st.button('Predict'):
    transformed_sms=transfrom_text(input_sms)
    vector_input=tfidf.transform([transformed_sms])
    result=model.predict(vector_input)[0]
    if result==1:
      st.header("Spaammm!!")
    elif result==0:
      st.header("Not a Spam")

