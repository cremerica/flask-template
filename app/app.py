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
   
    return "This is the test"

@app.route('/sql-check')
def checkDB():

    #first we need to check if the database exists, so we'll try connecting to the postgres database and check the catalog
    conn = None
    db_exists = False
    try:
        conn = psycopg2.connect(database="postgres", user='postgres', password='postgres', host='postgresql-service', port= '5432')
        message_to_display = "Connectend to Database <br>"
    except:
        message_to_display = "There was a problem connecting to the database <br>"
    if conn is not None:
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database;")
        database_list = cur.fetchall()
        database_name = 'appdirectdb'
        message_to_display += "The following databases are on the list <br>"
        for database in database_list:
            message_to_display += str(database) + "<br>"
            if (database_name,) == str(database):
               db_exists = True
        if db_exists:    
            message_to_display += "AppDirect Database already exists <br>"
        else:
            message_to_display += "AppDirect Database not found, will need to create one <br>"
            try:
                cur.execute("CREATE database " + database_name)
                message_to_display += "database created! <br>"
            except:
                message_to_display += "There was an error creating the datbase... <br>"
            
    return message_to_display
@app.route('/sql-create')
def addData():
    message_to_display = ""
    conn = None

    sql_command = (

        """
        CREATE TABLE tblRecords (
           Data VARCHAR(250)
        )
        """
    )
    try:
        conn = psycopg2.connect(database="appdirectdb", user='postgres', password='postgres', host='postgresql-service', port= '5432')
        message_to_display = "Connectend to Database <br>"
        cur = conn.cursor()
        cur.execute("""CREATE TABLE tblRecords (Data VARCHAR(250))""")
        cur.execute("""INSERT INTO tblRecords (Data) VALUES(s%);""",(str(request.date) + " - " + str(request.headers)))
    except:
        message_to_display ="Unable to connect to the Database. Try browsing /sql-check to see if the Database exists <br>"
    finally:
        cur.close()
        conn.close()

    return message_to_display
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
