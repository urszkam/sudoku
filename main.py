#main.py

class HerokuApp:
    app_url = "https://fierce-spire-87558.herokuapp.com/"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"start": "1970-01-01"}


    