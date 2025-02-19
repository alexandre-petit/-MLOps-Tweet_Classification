import streamlit as st
import requests
import time
from config import api_key


prediction_as_text = {0: "Bad", 1: "Good"}

st.title("Tweet prediction interface")

st.info("Paste the Tweet in the textbox below and click 'Predict sentiment'")

tweet = st.text_input("Paste the tweet here")

# Initialisation de l'état de session pour stocker le feedback

if "tweet" not in st.session_state:

    st.session_state.tweet = "Ceci est un exemple de tweet"


if "prediction_feedback" not in st.session_state:

    st.session_state.prediction_feedback = ""

st.session_state.response = None
# Bouton pour afficher le tweet

if st.button("Afficher le tweet"):

    st.session_state.show_tweet = True  # On active l'affichage du tweet
    
    st.session_state.response = requests.post("http://127.0.0.1:8000/random", json={"message": "Send me a random number!"})
    response = st.session_state.response
    
    
    if response.status_code == 200:
        prediction = response.json().get("random_value")
        st.write(f"Received random value: {prediction}")
    else:
        st.error("Failed to get random value.")


# Affichage du tweet si le bouton a été cliqué

if st.session_state.get("show_tweet", False) and st.session_state.response:

    st.write(prediction_as_text[prediction])

    st.write("How was the prediction?")

    feedback = st.feedback("thumbs")
    
    if feedback in (0,1) and feedback != st.session_state.prediction_feedback:
        st.session_state.prediction_feedback = feedback


    if st.session_state.prediction_feedback in (0,1):
        st.write(prediction_as_text[feedback])
    
    
