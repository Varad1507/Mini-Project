import streamlit as st
import joblib
import re

model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

def clean(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = re.sub(r'\@\w+|\#','', text)
    text = re.sub(r'[^A-Za-z\s]', '', text.lower())
    return text

st.title("Twitter Sentiment Analyzer")

user_input = st.text_area("Enter a tweet:")
if st.button("Analyze"):
    clean_input = clean(user_input)
    vect_input = vectorizer.transform([clean_input])
    prediction = model.predict(vect_input)
    st.write(f"**Sentiment:** {prediction[0]}")
 