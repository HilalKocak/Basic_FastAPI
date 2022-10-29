import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

#Create the app object
app=FastAPI()
pickle_in=open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

#Index route, opends automatically on http://127.0.0.0:8000
@app.get('/')
def index():
    return {'message': 'Hello Stranger'}

@app.get('/name')
def get_name(name: str):
    return {'Hello':f'{name}'}

#Expose the prediction functionality, make a prediction from the passed
# JSON data and return the predicted Bank Note with the confidence

@app.post('/predict')
def predict_banknote(data:BankNote):
    data=data.dict()
    print(data)
    print("Hello")
    variance=data['variance']
    print(variance)
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    print(classifier.predict([[variance, skewness,curtosis,entropy]]))
    prediction=classifier.predict([[variance, skewness, curtosis, entropy]])
    if (prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="It is a bank note"
    return {
        'prediction':prediction
    }



#Run the API with the uvicorn
#Will run on http://127.0.0.1:8000
if __name__== '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload
# uvicorn python_script_name: fastapi_object_name --reload