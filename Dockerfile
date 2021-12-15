FROM python:3.8.3-slim 
WORKDIR /code
RUN python -m pip install --upgrade pip \
    && apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "python", "app.py" ]
