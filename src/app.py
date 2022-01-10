import datetime
import requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def fetch_data():
  # --- Call KaaS REST endpoint ---
  req = requests.get('https://api.kanye.rest/')
  resp = req.content
  return resp