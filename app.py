import psutil
from flask import Flask

app = Flask(__name__) #A flask App created

@app.route('/') #Whenever a user comes in the home path is run 

def index(): #Run this when useer comes at / path
    cpu_percent = psutil.cpu_percent #Holds value of CPU Usage
    mem_percent = psutil.virtual_memory().percent  #Get the Memory Usage
    Message = None

    if cpu_percent > 80 or mem_percent > 80: #When the cpu or mem > 80% then needs ot scale up 
        Message = "High CPU or Memory Utilization Detected. Need to Scale Up IMmediately"
    return f"CPU Utilization:{cpu_percent} and Memory Utilized:{mem_percent}"

if __name__ == '__main__': #To run on our Local Machine
    app.run(debug=True,host='0.0.0.0')