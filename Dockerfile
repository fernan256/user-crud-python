
FROM python:2.7
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y \
	python-pip && \
	pip install -r requirements.txt
EXPOSE 5000
ENV FLASK_CONFIG=development
ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1
CMD flask run -h 127.0.0.1 -p 5000
#CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

