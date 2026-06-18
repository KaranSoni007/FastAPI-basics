from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "My first API is working"}


@app.get("/about")
def about():
    return {"project": "loan risk model", "version": 1.0}


@app.get("/contact")
def contact():
    return {"contact": 9999999999, "email": "ks.telecom999@gmail.com"}
