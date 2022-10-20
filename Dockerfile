FROM python:3.8-alpine
WORKDIR /data
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
VOLUME /data/history/
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
