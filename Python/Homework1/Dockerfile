FROM python
RUN pip install flask
WORKDIR /app
COPY . .
#CMD ["export", "FLASK_APP=app"]
#CMD ["export", "FLASK_ENV=development"]
#CMD ["export", "FLASK_DEBUG=0"]
CMD ["python3", "app.py", "--host=0.0.0.0"]
