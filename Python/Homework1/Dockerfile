FROM python
RUN pip install flask
WORKDIR /app
COPY . /app/
CMD ["python3", "-m", "flask", "run", "app.py", "--host=0.0.0.0"]
