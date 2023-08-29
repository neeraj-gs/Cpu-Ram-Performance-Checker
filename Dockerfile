FROM python:3.9-slim-buster  
#Created a Base IMage

WORKDIR /app
#Defiend a working DIrectry where our apllication wil lrun

COPY requirements.txt .
#Copied the requireemtns to the workign dir[app] 

RUN pip3 install --no-cache-dir -r requirements.txt
#Run commnds to install all into image

COPY . . 
#Copy the code in app.py intot he image

ENV FLASK_RUN_HOST=0.0.0.0
#Set an envirnment variable

EXPOSE 5000
#Expost the Variable port

CMD ["flask","run"]
#Run the Commands to start the flask app 