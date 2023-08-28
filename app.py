import psuitl
from flask import Flask

app = Flask(__name__) #A flask App created

@app.route('/') #Whenever a user comes in the home path is run 

def index(): #Run this when useer comes at / path
    cpu_percent = psuitl.cpu_percent #Holds value of CPU Usage
    mem_percent = psuitl.virtual_memory().percent  #Get the Memory Usage
    
