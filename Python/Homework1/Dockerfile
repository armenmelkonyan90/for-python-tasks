FROM python
RUN pip install flask
WORKDIR /app
COPY . /app/
CMD ["export", "FLASK_APP=app.py"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
