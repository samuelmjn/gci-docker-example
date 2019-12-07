FROM python:3.7
EXPOSE 5000
ADD . /app
WORKDIR  /app
RUN pip install -r requirements.txt
CMD python manage.py