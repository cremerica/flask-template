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

@app.route('/support')
def create_support_file():
    file_path = 'app/'
    file_name = 'env_vars.txt'
    file_name_w_path= = os.path.join(file_path, file_name)
    
    file_to_write = open(file_name_w_path, "w")
    file_content = os.environ
    file_to_write.write(file_content)
    file_to_write.close()

@app.route('/msg')
def display_message():
    message_to_display = os.environ["PAGE_MESSAGE"]
    return message_to_display

if __name__ == '__main__':
    app.run(host='0.0.0.0')
