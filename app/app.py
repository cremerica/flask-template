from flask import Flask, render_template, request
import requests
import json
import os


app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/test')
def test():
    return "This is the test"

@app.route('/msg')
def display_message():
    message_to_display = os.environ["PAGE_DISPLAY"]
    return message_to_display

if __name__ == '__main__':
    app.run(host='0.0.0.0')
