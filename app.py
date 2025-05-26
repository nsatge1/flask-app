from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, DevSecOps on AWS!"

@app.route("/test")
def test():
    return "I have a new Service is healthy!"
