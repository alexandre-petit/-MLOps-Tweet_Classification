import streamlit as st
import requests
import time
from config import api_key

st.title("Tweet prediction interface")

st.info("Paste the Tweet in the textbox below and click 'Predict sentiment'")

tweet = st.text_input("Paste the tweet here")

# Initialisation de l'état de session pour stocker le feedback

if "tweet" not in st.session_state:

    st.session_state.tweet = "Ceci est un exemple de tweet"


if "prediction_feedback" not in st.session_state:

    st.session_state.prediction_feedback = ""


# Bouton pour afficher le tweet

if st.button("Afficher le tweet"):

    st.session_state.show_tweet = True  # On active l'affichage du tweet


# Affichage du tweet si le bouton a été cliqué

if st.session_state.get("show_tweet", False):

    st.write(tweet)

    st.write("How was the prediction?")

    feedback = st.feedback("thumbs")
    
    if feedback in (0,1) and feedback != st.session_state.prediction_feedback:
        st.session_state.prediction_feedback = feedback


    if st.session_state.prediction_feedback in (0,1):
        st.write(feedback)
    
    
