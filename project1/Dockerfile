FROM python:3.10.0-alpine3.15
WORKDIR /appp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /appp
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]


