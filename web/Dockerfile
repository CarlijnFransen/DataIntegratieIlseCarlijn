FROM python:3.6
ADD app.py /
ENV FLASK_APP app.py
ENV FLASK_FUN_HOST 0.0.0.0
#COPY requirements.txt requirements.txt
COPY /templates/home.html /templates/home.html
COPY /templates/results.html /templates/results.html
RUN pip install flask
RUN pip install werkzeug==0.16.1
CMD ["python","./app.py"]