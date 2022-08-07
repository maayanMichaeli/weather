FROM python:3.8-alpine
WORKDIR /home/project
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
