import streamlit as st
import requests
import time

st.title("Tweet prediction interface")

st.info("Paste the Tweet in the textbox below and click 'Predict sentiment'")

tweet = st.text_input("Paste tweet here")

#response = requests.get()


def print_feedback():
    global user_feedback
    print(user_feedback)

def predict_tweet():
    print(tweet)


button = st.button("Predict sentiment")#, on_click=predict_tweet)

if button:
    st.text(tweet)
    print(tweet)
    
    st.text("How was the prediction?")
    user_feedback = st.feedback("stars", on_change=print_feedback)

    #Resetting the button to None once the data are sent to the API
    #button = None
    
    if user_feedback:
        print(user_feedback)
        st.text(user_feedback)
        st.text("Feedback have been sent to the server")
        
    
    
