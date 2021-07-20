
# Imports the flask module 
from flask import Flask

# App object created out of Flask 
app = Flask(__name__)

# What does the app do? 
# If / is found return "Hello internet"
@app.route('/')
def hello_internet():
    return "Hello Internet!"

# Allow the code to be run by command line using app.py
if __name__=='__main__':
    app.run(debug=True)

# Access the app with python3 app.py
