FROM python
RUN pip install flask
WORKSPACE /app
COPY . /app/
CMD ["flask run", "/app/app.py"]
