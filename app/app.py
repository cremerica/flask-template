from flask import Flask, render_template, request
import requests
import json
import os
import psycopg2


app = Flask(__name__)


@app.route('/')
#this method renders an html file located in the AppDirect/app/templates directory.
def index():
    
    return render_template("index.html")

@app.route('/test')
# this was simply a test to see how to display a message by using a different route.
def test():
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='postgres', host='postgresql-service', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database test123''';

    #Creating a database
    cursor.execute(sql)

    #Closing the connection
    conn.close()
    return "This is the test"

@app.route('/support')
# This creates a file and dumps all environment variables. Used as an example of creating a file for support to troubleshoot.
def create_support_file():
    file_path = 'app/'
    file_name = 'env_vars.txt'
    file_name_w_path = os.path.join(file_path, file_name)
    
    file_to_write = open(file_name_w_path, "w")
    file_content = os.environ
    file_content_str = str(file_content)
    file_to_write.write(file_content_str)
    file_to_write.close()
    return "Check the App directory for a file called env_var.txt"


@app.route('/msg')
# This displays a message that can be passed as an evironment variable PAGE_MESSAGE
def display_message():
    message_to_display = os.environ["PAGE_MESSAGE"]
    return message_to_display

if __name__ == '__main__':
    app.run(host='0.0.0.0')
