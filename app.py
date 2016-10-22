#!bin/python3

from flask import Flask,request
import sqlite3


app = Flask(__name__)


@app.route('/inputtext', methods=['POST'])
def do():
    text = request.form['text']
    return text

@app.route('/outputtext', methods=['GET'])
def output():
    return "world"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7778)