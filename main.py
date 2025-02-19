from fastapi import FastAPI
from pydantic import BaseModel
import random

# Initialize the FastAPI app
app = FastAPI()

# Create a simple request body model for the POST request
class RequestData(BaseModel):
    message: str  # The body can contain any data; here we're using "message" for illustration

# Define the POST endpoint
@app.post("/random")
async def get_random(data: RequestData):
    # Return either 0 or 1 randomly
    return {"random_value": random.choice([0, 1])}