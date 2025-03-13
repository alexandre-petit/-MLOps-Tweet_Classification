import streamlit as st
import requests
import time
from config import api_key

api_url = "https://mango-tree-08b7ad603.6.azurestaticapps.net" #"http://127.0.0.1:8000"


prediction_as_text = {0: "Negative", 1: "Positive"}

st.title("Tweet prediction interface")

st.info("Paste the Tweet in the textbox below and click 'Predict sentiment'")

tweet = st.text_input("Paste the tweet here")
st.session_state.tweet = tweet
feedback = None
# Initialisation de l'état de session pour stocker le feedback

if "tweet" not in st.session_state:

    st.session_state.tweet = "Ceci est un exemple de tweet"


#if "prediction_feedback" not in st.session_state:

st.session_state.prediction_feedback = None
st.session_state.prediciton = None
st.session_state.response = None
st.session_state.feeback_returned = None

# Predict button and post request
if st.button("Predict tweet sentiment"):

    st.session_state.show_tweet = True  # On active l'affichage du tweet
    
    st.session_state.response = requests.post(api_url + "/random", json={"message": "Send me a random number!"})
    response = st.session_state.response
    
    if response.status_code == 200:
        prediction = response.json().get("random_value")
        st.write(f"Received random value: {prediction}")
    else:
        st.error("Failed to get random value.")
    
    st.session_state.prediction = prediction


# Showing tweet after sending predicting and displaying feedback widget

if st.session_state.get("show_tweet", False) and st.session_state.response:

    st.write(f"The sentiment of this tweet is {prediction_as_text[prediction]}")

    

st.write("How was the prediction?")
feedback = st.feedback("thumbs")
print(feedback)
    
if feedback in (0,1) and feedback != st.session_state.prediction_feedback:
    st.session_state.prediction_feedback = feedback
        
    post_feedback = {
            "tweet": st.session_state.tweet,
            "sentiment": st.session_state.prediction,
            "feedback": feedback
        }
        
    requests.post(api_url + "/feedback", json=post_feedback)
    print("feedback sent")

if st.session_state.prediction_feedback in (0,1):
    st.write(prediction_as_text[feedback])
    
    
