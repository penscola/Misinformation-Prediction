import streamlit as st
import streamlit.components.v1 as com
#import libraries
from transformers import AutoModelForSequenceClassification,AutoTokenizer, AutoConfig
import numpy as np
#convert logits to probabilities
from scipy.special import softmax


#import the model
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

model_path = f"penscola/news-d-bert"
config = AutoConfig.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
#Set the page configs
st.set_page_config(page_title='Fake News Detection',page_icon='😎',layout='wide')

#welcome Animation
st.markdown('<h1> Fake News Detection </h1>',unsafe_allow_html=True)

#Create a form to take user inputs
with st.form(key='tweet',clear_on_submit=True):
    text=st.text_area('Copy and paste the news or type one')
    submit=st.form_submit_button('submit')

#create columns to show outputs
col2,col3=st.columns(2)
col2.title('Fake or Legit')
col3.title('Confidence of this prediction')

if submit:
    print('submitted')
    #pass text to preprocessor
    def preprocess(text):
    #initiate an empty list 
        new_text = []
        #split text by space
        for t in text.split(" "):
            #set username to @user
            t = '@user' if t.startswith('@') and len(t) > 1 else t  
            #set tweet source to http
            t = 'http' if t.startswith('http') else t 
            #store text in the list
            new_text.append(t)
            #change text from list back to string
        return " ".join(new_text) 
    

    #pass text to model

    #change label id 
    config.id2label = {0: 'Fake', 1: 'Legit'}

    text = preprocess(text)

    # PyTorch-based models
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    #Process scores
    ranking = np.argsort(scores)
    ranking = ranking[::-1]  
    l = config.id2label[ranking[0]]
    s = scores[ranking[0]]

    #output
    if l==1:
        col2.write('Legit')
        col3.write(f'{s}%')
    else:
        col2.write('Fake')
        col3.write(f'{s}%')