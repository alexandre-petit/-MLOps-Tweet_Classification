# -MLOps-Tweet_Classification

In this project we are going to compare text features extraction models and compare the results using MLFlow.

Once the best model is selected, it will be deployed on the cloud. A local app will be use to call the model API

## 1. Finding the best models and saving experiments

Three models will be compared
- Logistic Regression
- BERT
- A custom neural network

## 2. Deploying the model on the cloud

The API and the final will be deployed on Azure WebApp. At the moment, the API is tested locally. The API randomly send 0 or 1 to see if the streamlit app works correctly.

A second endpoint receive the feedback from the user after the prediction. This feedback is a binary value and must be stored in a file to monitor the model.

## 3. Local App

The Application has a simple layout with a title, a text input widget, and a predict button. Once the predict button is clicked. The POST request is sent and the prediction will be processed by the local app.

A thumbs widget will appear to give a feedback to the model. This feedback will then be send to the API.

## 4. Model monitoring system

## 5. Blog Article (In progress)

The project requires a blog article to summarize all the work done and explaining the MLOps methodology
