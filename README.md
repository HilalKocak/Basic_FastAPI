## FAST API Machine Learning Web Application

-  This application is a machine learning application that uses the BankNote_Authentication.csv dataset with variance, skewness, curtosis and entropy features to make binary classifications of 1 and 0 as real banknotes and fake banknotes.

- Before running the project, you must have the BankNote_Authentication.csv and classifier.pkl files in the project directory.

- If you run the ModelTraining.ipynb file step by step, you will get the classifier.pkl file in the project directory.

✓ To download the libraries used by the project, use
```
pip install -r requirements.txt
```

✓ To run a simple example made with Fast API, use
```
uvicorn main:app --reload
```

✓ To run a basic machine learning application made with Fast API, use
```
uvicorn app:app --reload
```

- You can try the web application by logging into Swagger with http://127.0.0.1:8000/docs 