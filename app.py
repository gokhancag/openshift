import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Selamlar!"

@app.route('/nasilsin')
def nasilsin():
    return 'iyiyim, sen nasilsin?'

@app.route('/hello')
def hello():
    return 'hello from OpenShift..'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)