FROM python
RUN pip install flask
WORKDIR /app
COPY . .
CMD ["export FLASK_APP=Python/Homework1/app"]
#CMD ["export", "FLASK_ENV=development"]
#CMD ["export", "FLASK_DEBUG=0"]
CMD ["flask", "run"]
