import streamlit as st
import pandas as pd
import re
import string
from html.parser import HTMLParser
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import nltk
import sd_algorithm

df = pd.read_csv("mined_news.csv")

sd = sd_algorithm.SDAlgorithm()

stopwords_eng = stopwords.words('english')

# Loading the model
pickle_in = open("newscluster_model.sav", "rb")
model = pickle.load(pickle_in)

# Loading the tokenizer
pickle_n = open("tokenizer.pickle", "rb")
tokenizer = pickle.load(pickle_n)

# Get news content from url
def website_content(url):
    sd.url = url
    content = sd.analyze_page()
    return content

def list_to_String(content): 
    strings = " "   
    return (strings.join(content))

# Function to clean texts
def clean_content(content):
  # Removing html characters
  content = HTMLParser().unescape(content)
  content = content.lower()
  
  # clean by removing urls and hashtags
  content = re.sub(r'https?:\/\/.\S+', "", content)
  content = re.sub(r'#', '', content)
  content = re.sub(r'^RT[\s]+', '', content)

  content_tokens = content.split()
  content_list=[]
  for word in content_tokens:
    if word not in stopwords_eng:
      content_list.append(word)

  # Remove punctuations
  clean_content = []
  for word in content_list:
    if word not in string.punctuation:
      clean_content.append(word)

  return clean_content

def predict_news(url):
    content = website_content(url)
    content = clean_content(list_to_String(content[3]))
    encoded_text = tokenizer.texts_to_sequences([content])
    max_length = 2
    padded_text = pad_sequences(encoded_text, maxlen=max_length, padding='post')
    y_pred = model.predict(padded_text)
    return y_pred


st.title("Model For News Category")
html_temp = """
<div style="background-color:black;padding:10px">
<h3 style="color:white;">Insert the link to the article, and I'll do the rest of the magic..</h3>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

result = ""
categori = ""
related = []
url = st.text_input("Fill in the field below", "")

if st.button("Classify News"):
    result = predict_news(url)
    if result == [0]:
        categori = 'Business'
        related = df[df['content_category']=='business']["link"]
    elif result == [1]:
        categori = 'Entertainment'
        related = df[df['content_category']=='entertainment']["link"]
    elif result == [2]:
        categori = 'Politics'
        related = df[df['content_category']=='politics']["link"]
    elif result == [3]:
        categori = 'Sports'
        related = df[df['content_category']=='sports']["link"]
st.success('The article category prediction is: {}'.format(categori))

# front end elements of the web page 
html_temp = """ 
<div style ="background-color:black;padding:10px"> 
<h1 style ="color:white;">Articles that are related</h1> 
</div> 
""" 
st.markdown(html_temp, unsafe_allow_html=True)
st.write(related)
