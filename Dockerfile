FROM python:3.11

WORKDIR /code


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
