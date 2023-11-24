##start with base image, which is python,'latest' tag refers to latest version
FROM python:latest

#install Google Chrome in Docker image
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

#updates package list and install stable version of Google Chrome
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#sets the working directory inside Docker container to /app
WORKDIR /app

#copy and install requirements.txt file into /app directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copies rest of code into container
COPY . .

#set environmental variable FLASK_APP into "main.py"
ENV FLASK_APP main.py

#expose port 5000 from container
EXPOSE 5000

#for testing purposes
#CMD [ "flask", "run","--host","0.0.0.0"]

#run
CMD [ "python", "main.py" ]