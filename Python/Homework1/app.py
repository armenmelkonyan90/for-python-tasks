#!/usr/bin/python3
import argparse
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pass debug variable')
    parser.add_argument('--deb', required=True, type=bool, help='boolean debug argument')
    args = parser.parse_args()
    app.debug = args.deb
    app.run(host="0.0.0.0", port="5050")    
