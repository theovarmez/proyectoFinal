FROM python:3.11

WORKDIR /code

#test
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000
