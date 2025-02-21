import streamlit as st
import requests

def test_feedback(tweet: str):
    
    test_feedback = {
            "tweet": tweet,
            "sentiment": 1,
            "feedback": 1
        }
    st.session_state.feedback_returned = requests.post("http://127.0.0.1:8000/feedback", json=test_feedback)
    feedback_returned = st.session_state.feedback_returned
    
    if feedback_returned.status_code == 200:
        st.write(f"The feedback was stored by the API")
    else:
        st.error("Failed to receive feedback")
