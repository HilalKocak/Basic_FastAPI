import uvicorn
from fastapi import FastAPI


#Create the app object
app= FastAPI()

#Index route, opends automatically on http://127.0.0.0:8000
@app.get('/')
def index():
    return {'message': 'Hello Stranger'}

#Route with a single parameter,returns the parameter within a message
#Located at: http:127.0.0.1:8000/AnyNameHere

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to Hilals Channel':f'{name}'}

#Run the API with the uvicorn
#Will run on http://127.0.0.1:8000
if __name__== '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn main:app --reload
# main: python script name
#app : fast api object name