# app/app.py
from flask import Flask
import socket

app = Flask(__name__)
HOSTNAME = socket.gethostname()

@app.route('/')
def hello():
    return f"Hello from Python service instance: {HOSTNAME}!\n"

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)