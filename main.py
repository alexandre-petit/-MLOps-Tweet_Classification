from fastapi import FastAPI
from pydantic import BaseModel
import random
import pandas as pd
from datetime import datetime as dt

# Initialize the FastAPI app
app = FastAPI()

# Create a simple request body model for the POST request
class RequestData(BaseModel):
    message: str  # The body can contain any data; here we're using "message" for illustration

class FeedbackData(BaseModel):
    feedback: dict


# Define the POST endpoint
@app.post("/random")
async def get_random(data: RequestData):
    # Return either 0 or 1 randomly
    return {"random_value": random.choice([0, 1])}

@app.post("/feedback")
async def get_feedback(data: dict):
    
    timestamp = dt.now()
    
    #data = data.dict()
    data['datetime'] = timestamp
    
    
    try:
        feedback_df = pd.read_csv("feedback.csv")
        l = feedback_df.shape[0]
        
        feedback_df.loc[l] = data
    except:
        
        columns = [
            "datetime",
            "tweet",
            "sentiment",
            "feedback"
        ]
        feedback_df = pd.DataFrame(columns=columns)
        feedback_df.loc[0] = data
        
    feedback_df.to_csv("feedback.csv", index=False)