FROM python
RUN pip install flask
WORKDIR /app
COPY . .
CMD ["export", "FLASK_APP=app.py"]
CMD ["export", "FLASK_ENV=development"]
CMD ["export", "FLASK_DEBUG=0"]
CMD ["flask", "run", "--host=0.0.0.0"]
